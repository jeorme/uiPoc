import json
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import ast

auth = HTTPBasicAuth('kplus','Kondor_123')

##installation
##step 1 creation of locationDate
url_fcc_marketSet = "http://fr1cslbmto0014:8200/api/v1/static-data/locations/bulk"
locationDateJson = [{ "locationDate": "2020-02-11",    "name": "AOD",    "transient": False  }]
response = requests.post(url_fcc_marketSet,json = locationDateJson, auth=auth)
if response.status_code == 409:
    print("locationDate already exists")
else:
    idLocation = ast.literal_eval(response.text)["ids"][0]

##step 2 creation of users
url_fcc_users = "http://fr1cslbmto0014:8200/api/v1/static-data/user-profiles/bulk"
userJson = [{"location": "AOD",    "name": "kplus",    "transient": False  }]
response = requests.post(url_fcc_users,json = userJson, auth=auth)
if response.status_code == 409:
    print("user already exists")
else:
    idUser =  ast.literal_eval(response.text)["ids"][0]

##step 3 creation of marketSet for Yield curves
url_fcc_marketSet = "http://fr1cslbmto0014:8200/api/fcc/marketset"
idMaster = "FCC-master"
masterJSON = {"description" : "YC master marketData", "name" : "master"}
response = requests.post(url_fcc_marketSet,json = masterJSON, auth=auth)
if response.status_code == 409:
    print("master already exists")


#step 4 : push of the YC :
###workaround while there is no transient
url_currency = "http://fr1cslbmto0014:8200/api/v1/static-data/currencies"
#EURid = requests.get(url_currency,auth=auth)
CCY = ast.literal_eval(requests.get(url_currency,auth=auth).content.decode('ascii'))
count = 0
for val in CCY:
    for val1 in val.values():
        if val1 == "EUR":
            EURid = val["id"]
            count = count +1
        if val1 == "USD":
            USDid = val["id"]
            count = count + 1
    if count == 2:
        break

##push the yield curve
url_yc_calibrated = "http://fr1cslbmto0014:8200/api/fcc/curve/calibrated/import"
EUROIS = {
  "asOfDate": "2016-07-05",
  "calibrationParameters": {
    "artificialPillarMethod": "None",
    "extrapolationMethodAfterLastPlot": "Flat",
    "extrapolationMethodBeforeFirstPlot": "Flat",
    "extrapolationVariableAfterLastPlot": "Zero Coupon Rate",
    "extrapolationVariableBeforeFirstPlot": "Zero Coupon Rate",
    "forwardRatesBasis": "ACT/360",
    "interpolationMethod": "Cubic Spline",
    "interpolationVariable": "Discount Factor",
    "quoteConvention": "Mid",
    "quoteType": "Discount Factor",
    "zeroCouponBasis": "ACT/360",
    "zeroCouponFormula": "Compound"
  },
  "currencyId": EURid,
  "marketSet": idMaster,
  "maturities": {
  "2016-07-06":{
  "quote":{
  "mid" : 0.999
  }
  },
   "2016-07-07":{
  "quote":{
  "mid" : 0.999
  }
  },
   "2016-07-09":{
  "quote":{
  "mid" : 0.998
  }
  },
   "2016-07-13":{
  "quote":{
  "mid" : 0.996
  }
  },
   "2016-08-06":{
  "quote":{
  "mid" : 0.99
  }
  },
   "2016-10-06":{
  "quote":{
  "mid" : 0.984
  }
  },
   "2017-07-06":{
  "quote":{
  "mid" : 0.975
  }
  },
   "2018-07-06":{
  "quote":{
  "mid" : 0.94
  }
  },
   "2022-07-06":{
  "quote":{
  "mid" : 0.895
  }
  }

  },
  "name": "EUROIS"
}
USDOIS = {
  "asOfDate": "2016-07-05",
  "calibrationParameters": {
    "artificialPillarMethod": "None",
    "extrapolationMethodAfterLastPlot": "Flat",
    "extrapolationMethodBeforeFirstPlot": "Flat",
    "extrapolationVariableAfterLastPlot": "Zero Coupon Rate",
    "extrapolationVariableBeforeFirstPlot": "Zero Coupon Rate",
    "forwardRatesBasis": "ACT/360",
    "interpolationMethod": "Cubic Spline",
    "interpolationVariable": "Discount Factor",
    "quoteConvention": "Mid",
    "quoteType": "Discount Factor",
    "zeroCouponBasis": "ACT/360",
    "zeroCouponFormula": "Compound"
  },
  "currencyId": USDid,
  "marketSet": idMaster,
  "maturities": {
  "2016-07-06":{
  "quote":{
  "mid" : 1.021
  }
  },
   "2016-07-07":{
  "quote":{
  "mid" : 1.001
  }
  },
   "2016-07-08":{
  "quote":{
  "mid" : 0.999
  }
  },
   "2016-07-15":{
  "quote":{
  "mid" : 0.998
  }
  },
   "2016-08-05":{
  "quote":{
  "mid" : 0.991
  }
  },
   "2016-12-06":{
  "quote":{
  "mid" : 0.983
  }
  },
   "2017-07-06":{
  "quote":{
  "mid" : 0.97
  }
  },
   "2018-07-06":{
  "quote":{
  "mid" : 0.95
  }
  },
   "2022-07-06":{
  "quote":{
  "mid" : 0.89
  }
  }

  },
  "name": "USDOIS"
}
response = requests.post(url_yc_calibrated,json = EUROIS, auth=auth)
if response.status_code == 409:
    print("EUROIS already exists")

response = requests.post(url_yc_calibrated,json = USDOIS, auth=auth)
if response.status_code == 409:
    print("USDOIS already exists")

##create FX vol : MDS

##link MDS to master





FXVolDef = pd.DataFrame(columns=["name","pairId","smileType","basis","smileInterpolationVar","smileInterpolationMethod","smileExtrapolationMethod","tenorInterpolationVar","tenorInterpolationMethod",
                                 "tenorExtrapolationMethod","domesticCurve","foreignCurve","premiumAdjusted","marketSet"])

##hardcoded value db modif:
premiumAdjusted = False
smileExtrapolationMethod = "flat"
tenorInterpolationVar = "totalVariance"
tenorExtrapolationMethod = "flat"
domesticCurve = "USDOIS"
foreignCurve = "EUROIS"
marketSet = "$id/DEFAULT"
#binding
#smileType = VolatCurves.smileType
#basis= VolatCurves.basis
#smileInterpolationMethod = VolatCurves.smileInterpolationMethod
#tenorInterpolationVar = VolatCurves.TenorInteprolation


#hardcoded defect FCP : PANDA-4096
smileInterpolationVar = "volatility"


FXVolDef[0] = ["Kplus1/VolatCurves/256380",EUR/USD,"strike","ACT/365.FIXED",smileInterpolationVar,"linear",smileExtrapolationMethod,tenorInterpolationVar,"linear",tenorExtrapolationMethod,domesticCurve,foreignCurve,premiumAdjusted,marketSet]
#step 1 create the Fx vol
url_fcp_name = ""

#step 2 create fx vol def into store
url_fcp_def = ""

#step 3 call FCP entity risk factor
url_fcp_rf =""

#step 4 call FCP pricing Kondor FX vol
url_fcp_price = ""

response = requests.get(url, verify=False)