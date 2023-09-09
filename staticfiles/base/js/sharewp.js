
// order["RESTAURANT NAME"] = arr[0];
// order["CUSTOMER NAME"] = arr[1];
// order["ITEM"] = arr[2];
// order["ORDER NO"] = arr[3];
// order["PHONE"] = arr[4];
// order["PRICE"] = arr[5];
// order["ADDRESS"] = arr[6];
// order["PAYMENT TYPE"] = arr[7];
// order["STATUS"] = arr[8];







// }





document.addEventListener('DOMContentLoaded', function () {
  // Find all "share" buttons by their class name
  var shareButtons = document.querySelectorAll('.share-button');

  // Add click event listeners to each "share" button
  shareButtons.forEach(function (shareButton) {
    shareButton.addEventListener('click', function () {
      // Find the parent <tr> element of the clicked button
      var parentRow = this.closest('tr');

      // Extract data from the <td> elements within the <tr>
      var column1Data = parentRow.querySelector('td:nth-child(1)').textContent;
      var column2Data = parentRow.querySelector('td:nth-child(2)').textContent;
      var column3Data = parentRow.querySelector('td:nth-child(3)').textContent;
      var column4Data = parentRow.querySelector('td:nth-child(4)').textContent;
      var column5Data = parentRow.querySelector('td:nth-child(5)').textContent;
      var column6Data = parentRow.querySelector('td:nth-child(6)').textContent;
      var column7Data = parentRow.querySelector('td:nth-child(7)').textContent;
      var column8Data = parentRow.querySelector('td:nth-child(8)').textContent;
      var column9Data = parentRow.querySelector('td:nth-child(9)').textContent;
      // API Request 
      const KEY = 'Cgqn94edOGXaCPrr76Zv9JMNNK9XLv4E';
      const fromLocation = 'Jaleeb Al-Shuyoukh Kuwait'


      const toLocation = column7Data

      // Construct the URL with the API key and locations
      const url = `https://www.mapquestapi.com/directions/v2/route?key=${KEY}&from=${fromLocation}&to=${toLocation}`;

      

      // API END 



      var order = {

      }
      order["RESTAURANT NAME"] = column1Data
      order["CUSTOMER NAME"] = column2Data;
      order["ITEM"] = column3Data;
      order["ORDER NO"] = column4Data;
      order["PHONE"] = column5Data;
      order["PRICE"] = column6Data
      order["ADDRESS"] = column7Data
      order["PAYMENT TYPE"] = column8Data;
      order["STATUS"] = column9Data;



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

    });
  });
});

