from google.appengine.ext import ndb

class OrderModel(ndb.Model):
    exchangeContractAddress = ndb.StringProperty(required=True)
    maker = ndb.StringProperty(required=True)
    taker = ndb.StringProperty(required=True)
    makerTokenAddress = ndb.StringProperty(required=True)
    takerTokenAddress = ndb.StringProperty(required=True)
    feeRecipient = ndb.StringProperty(required=True)
    makerTokenAmount = ndb.StringProperty(required=True)
    takerTokenAmount = ndb.StringProperty(required=True)
    makerFee = ndb.StringProperty(required=True)
    takerFee = ndb.StringProperty(required=True)
    expirationUnixTimestampSec = ndb.StringProperty(required=True)
    salt = ndb.StringProperty(required=True)
    ecSignature = ndb.JsonProperty(required=True)
