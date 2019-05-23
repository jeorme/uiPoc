from tkinter import *
from API import *
from ApiHelper import *
import json

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
    if instrumentType=="FXO VANILLA":
        url = url+"fx-option"
    elif instrumentType== "FX SPOT" :
        url = url + "fx-spot"
    elif instrumentType== "FX SWAP" :
        url = url + "fx-swap"
    elif instrumentType== "FX FORWARD" :
        url = url + "fx-forward"
    elif instrumentType== "SWAP" :
        url = url + "ir-swap"
    else:
        return tuple()
    trades = get(url)
    output = []
    for trade in trades:
        output.append(trade["id"])
    return tuple(output)

def pushTrade(tradePath, type, output):
    url_push  = "https://fr1pslcmf05:8770/api/pricing/store/trade/"
    if type == "SWAP":
        url_push = url_push+ "ir-swap"
    elif type == "FX SPOT":
        url_push = url_push + "fx-spot"
    elif type == "FX FORWARD":
        url_push = url_push + "fx-forward"
    elif type == "FX SWAP":
        url_push = url_push+"fx-swap"
    else:
        print("error instrument not defined")
    path = "C:/Users/jerom/PycharmProjects/uiPoc/"
    name = path+tradePath.get(1.0,END).replace("\n","")
    with open(name+".json", "r") as write_file:
        data = json.load(write_file)
        write_file.close()
    val = post(url_push,data)
    output.insert(END,val)

