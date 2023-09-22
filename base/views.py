from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Restaurant , Order
from .forms import OrderForm ,CreateUserForm
from .filters import OrderFilter
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
import time
from .email import send_order_confirmation_email
from django.contrib.auth.models import User
from .orderNotification import send_welcome_message_async
import asyncio
from telegram import Bot

# Create your views here.
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

def is_rest(user):
    return user.groups.filter(name='Restraunt').exists()





@login_required(login_url='login/')
@user_passes_test(is_admin)
def  registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name='Restraunt')
            user.groups.add(group)
            restaurant = Restaurant.objects.create(user=user)
            restaurant.name = username
            restaurant.email = email
            restaurant.save()
            messages.success(request,"Registered Succefully") 
            return redirect('admin-dashboard')
        else:
            error_msg= form.errors
            messages.error(request, error_msg)
            

    context = {'form': form}
    return render(request, 'base/admindashboard/register.html', context)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('dashRedirec')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request , username= username , password =password)
            if user is not None:
                login(request, user)
                print(user)
                print('redirect')
                return redirect('/')
            else:
                print('Invalid')
        return render(request , 'base/login.html')


@login_required(login_url='login/')
def userLogout(request):
    logout(request)
    return redirect('/')
    
@login_required(login_url='login/')
@user_passes_test(is_admin)
def adminDashboard(request):
    if request.method == 'POST':
        print('request----------')
    orders = Order.objects.all()
    customers = Restaurant.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending  = orders.filter(status='Pending').count()
    outfor  = orders.filter(status='out for delivery').count()
    context = {'outfor':outfor, 'orders':orders , 'customers':customers,"total_orders":total_orders,'pending':pending,'delivered':delivered}


    return render(request , 'base/admindashboard/dashboard.html',context)

@login_required(login_url='login/')
@user_passes_test(is_rest)
def clientDashboard(request):
    orders = request.user.restaurant.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending  = orders.filter(status='Pending').count()
    outfor  = orders.filter(status='out for delivery').count()
    context ={ 'outfor':outfor, 'orders':orders,"total_orders":total_orders,'pending':pending,'delivered':delivered}

    return render(request,'base/client/dashboard.html',context)

@login_required(login_url='login/')
@user_passes_test(is_rest)
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            restaurant = request.user.restaurant
            order = form.save(commit=False)
            order.restaurant = restaurant
            order.status = 'Pending'
            order.save()

            # notification
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(send_welcome_message_async(restaurant))

            # Notification
            messages.success(request, 'Your order has been placed successfully. Let us handle the rest.')
            return redirect('user-dashboard')
        else:
            error_msg = form.errors
            messages.error(request, error_msg)
            messages.error(request, "Something went wrong while placing your order")
    else:
        form = OrderForm()

    context = {'form': form}
    return render(request, 'base/client/order.html', context)

    
@login_required(login_url='login/')
@user_passes_test(is_admin)
def customersDetails(request,pk):
    customer = Restaurant.objects.get(id=pk)
    orders =  customer.order_set.all()
    orderCount = orders.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending  = orders.filter(status='Pending').count()
    outfor  = orders.filter(status='out for delivery').count()
    myFilter = OrderFilter(request.GET , queryset=orders)
    orders = myFilter.qs

    context = {'customer':customer, 'orders':orders,"orderCount":orderCount,'myFilter':myFilter,"total_orders":total_orders,'pending':pending,"outfor":outfor ,"delivered" : delivered}
    return render(request, 'base/admindashboard/detailView.html',context)

@login_required(login_url='login/')
@user_passes_test(is_admin)
def viewRestaurant(request):

    customers = Restaurant.objects.all()
    customer_data = []
    for customer in customers:
        restaurant = Restaurant.objects.get(id=customer.id)
        orders = restaurant.order_set.all()
        order_count = orders.count()
        onway_count = orders.filter(status='out for delivery').count()
        pending_count = orders.filter(status='Pending').count()
        delivered_count = orders.filter(status='Delivered').count()
        cancelled = orders.filter(status='Cancelled').count()
        customer_data.append({
            'id':customer.id,
            'customer': customer.name,
            'order_count': order_count,
            'onway_count': onway_count,
            'pending_count': pending_count,
            "delivered_count":delivered_count,
            "cancelled":cancelled

        })

    context = {'customers': customers, "customer_data":customer_data}
    return render(request ,'base/admindashboard/viewCustomer.html',context)



@login_required(login_url='login/')
@user_passes_test(is_admin)
def deleteOrder(request , pk):
    order = Order.objects.get(id=pk)
    if request.method =='POST':
        order.delete()
        messages.success(request ,'Deleted Succesfully')
        return  redirect('admin-dashboard')
    context = {'order':order}
    print('Not Entering')
    return render( request ,'base/admindashboard/del.html')

def redirectDash(request):
    user = request.user
    user_role ='admin' if user.groups.filter(name='Admins').exists() else 'user'
    if user_role =='admin':
        return redirect('admin-dashboard')
    else:
        return redirect('user-dashboard')

    

def unauthor(request):
    return HttpResponse("Not Auhtorised")

@login_required(login_url='login/')
@user_passes_test(is_admin)
def update(request, pk):
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=pk)
            # Update only the incoming data from the form
            incoming_data = request.POST.get('status')  # Replace 'incoming_data' with the actual field name
            if incoming_data is not None:
                order.status = incoming_data
                order.save()
                messages.success(request ,"Order Updated Succesfully")
                return redirect('admin-dashboard')  # Redirect to the desired page after the update
            else:
                # Handle the case where incoming_data is not provided in the form
                messages.error(request, "UPDATE Required")
        except Order.DoesNotExist:
            # Handle the case where the order with the given ID doesn't exist
            messages.error(request, "Order does not exist.")
    
    return render(request, 'base/admindashboard/updatemodal.html')