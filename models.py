from google.appengine.ext import ndb

class OrderModel(ndb.Model):
    exchangeContractAddress = ndb.StringProperty(required=True)
    maker = ndb.StringProperty(required=True)
    taker = ndb.StringProperty(required=True)
    makerTokenAddress = ndb.StringProperty(required=True)
    takerTokenAddress = ndb.IntegerProperty(required=True)
    feeRecipient = ndb.StringProperty(required=True)
    makerTokenAmount = ndb.StringProperty(required=True)
    takerTokenAmount = ndb.StringProperty(required=True)
    makerFee = ndb.StringProperty(required=True)
    takerFee = ndb.StringProperty(required=True)
    expirationUnixTimestampSec = ndb.StringProperty(required=True)
    salt = ndb.StringProperty(required=True)
    ecSignature = ndb.JsonProperty(required=True)

# [{
#   "exchangeContractAddress": "0x12459c951127e0c374ff9105dda097662a027093",
#   "maker": "0x9e56625509c2f60af937f23b7b532600390e8c8b",
#   "taker": "0xa2b31dacf30a9c50ca473337c01d8a201ae33e32",
#   "makerTokenAddress": "0x323b5d4c32345ced77393b3530b1eed0f346429d",
#   "takerTokenAddress": "0xef7fff64389b814a946f3e92105513705ca6b990",
#   "feeRecipient": "0xb046140686d052fff581f63f8136cce132e857da",
#   "makerTokenAmount": "10000000000000000",
#   "takerTokenAmount": "20000000000000000",
#   "makerFee": "100000000000000",
#   "takerFee": "200000000000000",
#   "expirationUnixTimestampSec": "42",
#   "salt": "67006738228878699843088602623665307406148487219438534730168799356281242528500",
#   "ecSignature": "0x61a3ed31b43c8780e905a260a35faefcc527be7516aa11c0256729b5b351bc33"
# }]
