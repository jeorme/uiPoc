from tkinter import *
from API import *
from ApiHelper import *

configName="DEFAULT"
pricingMethod="THEORETICAL"
marketDataSetId="$id/DEFAULT"
marketDataProviderId="PE_STORE_MDP"
resultHandlerConfigId=None
resultHandlerId="Collector"

scenarioContexts =[

    {
      "id": "base",
      "measureGroupIds": [
        "NPV"
      ]
    }

]


def price(tradeEntry,output):
    id = tradeEntry.get()
    perimeter = {"trade": {"ids": [id]}}
    result = unitary(aod="2016-07-04",referenceCurrency="$id/USD",perimeter=perimeter, scenarioContexts = scenarioContexts)
    output.delete(1.0,END)
    if id is "":
        output.insert(END,"Please enter an ID")
    else:
        output.insert(END,result[id]["scenarios"][0]["entries"][0]["measures"])

def getTrade(instrumentType):
    url = "https://fr1pslcmf05:8770/api/pricing/store/trade/"
    if instrumentType=="fxo":
        url = url+"fx-option"
    else:
        url = url + "fx-swap"
    trades = get(url)
    output = []
    for trade in trades:
        output.append(trade["id"])
    return tuple(output)