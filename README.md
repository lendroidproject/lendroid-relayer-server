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
3. The commnad will also start an instance of the google cloud datastore emulator at:
  * [http://localhost:8889/](http://localhost:8889/)

### Interacting with the app
1. To fetch all existing offers:
  * `GET http://localhost:8090/orders`
2. TO create an offer:
  * `POST http://localhost:8090/orders`
  * `curl` Example:
    ```
    curl -v 'http://localhost:8090/orders' \
    -H 'Content-Type: application/json;charset=UTF-8' \
    -H 'Accept: application/json, text/plain, */*' \
    --data-binary '{"exchangeContractAddress":"0x12459c951127e0c374ff9105dda097662a027093","maker":"0x9e56625509c2f60af937f23b7b532600390e8c8b","taker":"0xa2b31dacf30a9c50ca473337c01d8a201ae33e32","makerTokenAddress":"0x323b5d4c32345ced77393b3530b1eed0f346429d","takerTokenAddress":"0xef7fff64389b814a946f3e92105513705ca6b990","feeRecipient":"0xb046140686d052fff581f63f8136cce132e857da","makerTokenAmount":"10000000000000000","takerTokenAmount":"20000000000000000","makerFee":"100000000000000","takerFee":"200000000000000","expirationUnixTimestampSec":"42","salt":"67006738228878699843088602623665307406148487219438534730168799356281242528500","ecSignature":"0x61a3ed31b43c8780e905a260a35faefcc527be7516aa11c0256729b5b351bc33"}'
    ```

### Deployment Instructions

1. Include all the files created by running `npm build` or `yarn build` into the `templates` folder.
2. Deploy the project in one of the following ways:
  * Using gcloud: `gcloud app deploy --project [YOUR_PROJECT_ID] app.yaml index.yaml` (More reference available [here](https://cloud.google.com/appengine/docs/standard/python/getting-started/deploying-the-application "GAE deployment using gcloud").)
  * Using GAE Launcher: Hit the "Deploy" button available on the App Engine GUI.

<i>Note: User should be provided App Engine Admin rights to deploy the project.</i>
