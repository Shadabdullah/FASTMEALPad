KEY = 'Cgqn94edOGXaCPrr76Zv9JMNNK9XLv4E'
url = `https://www.mapquestapi.com/directions/v2/route?${KEY}=KEY&from=Clarendon Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA`

// Replace 'YOUR_API_ENDPOINT' with the actual API endpoint URL
const apiEndpoint = 'YOUR_API_ENDPOINT';

// Make a GET request to the API
fetch(url)
  .then(response => {
    // Check if the response status is OK (status code 200)
    if (response.ok) {
      // Parse the JSON response
      return response.json();
    } else {
      // Handle error responses
      throw new Error(`HTTP Error: ${response.status}`);
    }
  })
  .then(data => {
    // Handle the JSON data from the API
    console.log('API Response:', data);
    
    // Perform any additional processing or rendering here
  })
  .catch(error => {
    // Handle errors, e.g., network errors or invalid JSON
    console.error('API Error:', error);
  });
