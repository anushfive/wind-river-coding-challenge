#### prerequisites:
    
    * docker

## **Build the docker image**
sudo docker build --tag wind-river-code-challenge .

## Start the docker container to run the app
sudo docker run --name wind-river-code-challenge -p 5001:5001 wind-river-code-challenge

##API Endpoints
* /api/health
* /api/encrypt
* /api/decrypt

Once the app is up and running, use postman or any other testing tool to test the enpoints.

sample endpoint:
* http://0.0.0.0:5001/api/health
* http://0.0.0.0:5001/api/decrypt

**payload sample:** 
`{
    "Input": "gtegtegteg"
}`

**sample response:**

`{
    "Input": "gtegtegteg",
    "Message": "decryption successful",
    "Output": "fsdfsdfsdf",
    "Status": "success"
}`
* http://0.0.0.0:5001/api/decrypt

**payload sample:** 
`{
    "Input": "fsdfsdfsdf"
}`

**sample response:**

`{
    "Input": "fsdfsdfsdf",
    "Message": "encryption successful",
    "Output": "gtegtegteg",
    "Status": "success"
}`