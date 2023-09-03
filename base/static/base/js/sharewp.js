
function shareHandler(){
        // Get the parent <tr> element of the button
    var trElement = this.closest('tr');
    
    // Get all <td> elements within the <tr> element
    var tdElements = trElement.querySelectorAll('td');
    

    const order ={
    }
    var arr = []
    for (var i = 0; i <9; i++) {
        arr.push(tdElements[i].textContent)

    }

order["RESTAURANT NAME"] = arr[0];
order["CUSTOMER NAME"] = arr[1];
order["ITEM"] = arr[2];
order["ORDER NO"] = arr[3];
order["PHONE"] = arr[4];
order["PRICE"] = arr[5];
order["ADDRESS"] = arr[6];
order["PAYMENT TYPE"] = arr[7];
order["STATUS"] = arr[8];




function generatePlainTextOrder(orderData) {
  let orderText = " :::: ORDER DETAILS ::::\n\n";

  for (const key in orderData) {
    orderText += `${key}: ${orderData[key]}\n`;
   
  }

  return orderText;
}

const plainTextOrder = generatePlainTextOrder(order);
console.log(plainTextOrder);

    var encodedData = encodeURIComponent(plainTextOrder);

    var whatsappURL = 'https://api.whatsapp.com/send?text=' + encodedData;
 
    window.open(whatsappURL, '_blank');


     
    
}
  const shareBtn = document.getElementById("generatePDF")
  shareBtn.addEventListener('click' , shareHandler)
  

