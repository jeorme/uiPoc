import json
import requests
import pandas as pd

# calibrate with FCC
##step 1 creation of locationDate
url_fcc_marketSet = ""

##step 2 creation of users
url_fcc_users = ""

##step 3 creation of marketSet
url_fcc_marketSet = ""

#price with FCP
EURUSD = "Kplus1/Pairs/76584"


FXVolDef = pd.DataFrame(columns=["name","pairId","smileType","basis","smileInterpolationVar","smileInterpolationMethod","smileExtrapolationMethod","tenorInterpolationVar","tenorInterpolationMethod","tenorExtrapolationMethod","comesticCurve","foreignCurve","premiumAdjusted","marketSet"])

##hardcoded value db modif:
premiumAdjusted = False
smileExtrapolationMethod = "flat"
tenorInterpolationVar = "totalVariance"

#binding
#smileType = VolatCurves.smileType
#basis= VolatCurves.basis
#smileInterpolationMethod = VolatCurves.smileInterpolationMethod

#hardcoded defect FCP : PANDA-4096
smileInterpolationVar = "volatility"


FXVolDef[0] = ["Kplus1/VolatCurves/256380",EUR/USD,"strike","ACT/365.FIXED",smileInterpolationVar,"linear",smileExtrapolationMethod]
#step 1 create the Fx vol
url_fcp_name = ""

#step 2 create fx vol def into store
url_fcp_def = ""

#step 3 call FCP entity risk factor
url_fcp_rf =""

#step 4 call FCP pricing Kondor FX vol
url_fcp_price = ""
