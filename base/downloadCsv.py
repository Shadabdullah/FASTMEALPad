import csv
from django.http import HttpResponse
from .models import Restaurant

def download_csv(request, pk):
    # Fetch the restaurant data based on the provided primary key (pk)
    restaurant = Restaurant.objects.get(id=pk)

    # Fetch related orders for the restaurant
    orders = restaurant.order_set.all()

    # Prepare the data for CSV
    data = []

    for order in orders:
        data.append({
            'Booking Time': order.booking_time,
            'Delivery Time': order.delivery_time.strftime('%H:%M'),  # Format as HH:MM
            'Customer Name': order.customer_name,
            'Item Name': order.item_name,
            'Phone Number': order.phone_number,
            'Order Number': order.order_number,
            'Amount': order.amount,
            'Address': order.address,
            'Prepaid/Postpaid': order.prepaid_postpaid
        })

    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write CSV header
    writer.writerow(data[0].keys())

    # Write data rows
    for item in data:
        writer.writerow(item.values())

    return response
