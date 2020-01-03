## my-retail REST API service provides the client application ability to:

    1. Retrieve Product and Price information by Product Id

    2. Send request to update the price information in the database
    
### Instructions to Setup
--------------------- 
1. Clone the code from git repository - https://github.com/patelb10/my-retail.git
2. Make sure you are in the MyRetail directory
3. Use docker-compose to build this application.
 - `docker-compose build`
4. Run application to start app with mongo database
 - `docker-compose up`
5. Open browser to list of products in databse
`http://localhost:5000/products`

 ### Get Product Information from Database and External API:
-----------------------

Input: 
The client application does a GET request at the path "/products/{id}" for a product 
 
When the API receives the request, The price is retrieved from a data store, it also sends a request to "redsky.target.com" and retrieves the product information. The price information is now combined with the required product information to provide only the 
required product information to the user.

Output: 
For a product with product id '13860428', the sample JSON output is as shown below

{
    "current_price": {
        "currency_code": "USD",
        "value": 13.49
    },
    "id": 13860428,
    "name": "The Big Lebowski (Blu-ray)"
}

Validations: 
Appropriate error messages are provided after validating the data.

### Update Product Price in the Mongo database:
-------------------------------------

Input: 
client application can do a PUT request with input similar to the response received in GET and should be able
to modify the price in the datastore. The request is done at the same path "/products/{id}"

Sample Input: 
{"id":13860428,"current_price":{"value": 15.67,"currency_code":"USD"}}

When the API receives PUT request, it does some validations to see if the product is in datastore with valid id or not. If it is, the price for the product is modified 
in the data store.

Output: 
updated product information returned if the price modification is done.
{
    "current_price": {
        "currency_code": "USD",
        "value": 15.67
    },
    "id": 13860428,
}


