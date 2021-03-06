### Framework

This project is written using the [Google App Engine](https://cloud.google.com/appengine) IaaS (Infrastructure as a Service) framework.

The frontend is developed using the [React](https://github.com/facebookincubator/create-react-app) web framework.

### Installation and setup

1. Install requirements into the `lib` folder
   * `pip install -t lib -r requirements.txt`

<i>Note: Project settings are already configured in `app.yaml`, and the environment is setup to serve the build files generated from React.</i>

### Running app
1. To start the server, simply run the docker-compose command below:
  * `docker-compose up`
2. The command will start and instance of the python server accessible at:
  * [http://localhost:8090/](http://localhost:8090/)
3. The command will also start an instance of the google cloud datastore emulator at:
  * [http://localhost:8889/](http://localhost:8889/)

### Interacting with the app
1. To create an order:
  * `POST http://localhost:8090/orders`
  * **curl** example:
    ```bash
    curl -v -POST 'http://localhost:8090/orders' \
    -H 'Content-Type: application/json;charset=UTF-8' \
    -H 'Accept: application/json, text/plain, */*' \
    --data-binary @- <<BODY
    {"lenderAddress":"0x2Fd5d34162fA812E7D71BD5305954F4733E9271C",
    "loanCostTokenAddress":"0x2956356cd2a2bf3202f771f50d3d14a367b48070",
    "loanCostTokenAmount":"444499940000000000000000000",
    "loanCostTokenSymbol":"ETH",
    "loanInterestTokenAddress":"0x2956356cd2a2bf3202f771f50d3d14a367b48070",
    "loanInterestTokenAmount":"32994912300000000000000000000000000000",
    "loanInterestTokenSymbol":"ETH",
    "loanTokenAddress":"0xd26114cd6ee289accf82350c8d8487fedb8a0c07",
    "loanTokenAmount":"99482814550005300000000000000000000",
    "loanTokenSymbol":"OMG",
    "market":"OMG/ETH",
    "wranglerAddress":"0x12459c951127e0c374ff9105dda097662a027093",
    "ecSignature": "0xcde62d3400f56f168ffbab13e4e59c5e4b518c21357e495d66f2"}
    BODY
    ```
2. To fetch orders:
  * `GET http://localhost:8090/orders`
  * **curl** Example:
    ```http
    > GET /orders HTTP/1.1
    > Host: localhost:8090
    > User-Agent: curl/7.54.0
    > Accept: */*
    >
    < HTTP/1.1 200 OK
    < content-type: application/json
    < Server: Development/2.0
    < Date: Fri, 09 Feb 2018 02:57:44 GMT
    <
    {
      "orders": [
        {
          "ecSignature": "0x61a3ed31b43c8780e905a260a35faefcc527be7516aa11c0256729b5b351bc33",
          "exchangeContractAddress": "0x12459c951127e0c374ff9105dda097662a027093",
          "expirationUnixTimestampSec": "42",
          "feeRecipient": "0xb046140686d052fff581f63f8136cce132e857da",
          "maker": "0x9e56625509c2f60af937f23b7b532600390e8c8b",
          "makerFee": "100000000000000",
          "makerTokenAddress": "0x323b5d4c32345ced77393b3530b1eed0f346429d",
          "makerTokenAmount": "10000000000000000",
          "salt": "67006738228878699843088602623665307406148487219438534730168799356281242528500",
          "taker": "0xa2b31dacf30a9c50ca473337c01d8a201ae33e32",
          "takerFee": "200000000000000",
          "takerTokenAddress": "0xef7fff64389b814a946f3e92105513705ca6b990",
          "takerTokenAmount": "20000000000000000"
        }
      ]
    ```
  
### Deployment Instructions

1. Include all the files created by running `npm build` or `yarn build` into the `templates` folder.
2. Deploy the project in one of the following ways:
  * Using gcloud: `gcloud app deploy --project [YOUR_PROJECT_ID] app.yaml index.yaml` (More reference available [here](https://cloud.google.com/appengine/docs/standard/python/getting-started/deploying-the-application "GAE deployment using gcloud").)
  * Using GAE Launcher: Hit the "Deploy" button available on the App Engine GUI.

<i>Note: User should be provided App Engine Admin rights to deploy the project.</i>
