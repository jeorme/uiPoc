from tkinter import *
from API import *

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