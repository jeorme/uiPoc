from tkinter import *
from API import *
from ApiHelper import *
import json
import pandas as pd
import numpy as np
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import xlsxwriter

configName="DEFAULT"
pricingMethod="THEORETICAL"
marketDataSetId="$id/DEFAULT"
marketDataProviderId="PE_STORE_MDP"
resultHandlerConfigId=None
resultHandlerId="Collector"


notPresent = ['Kplus/SwapDeals/6219', 'Kplus/SwapDeals/6228',
              'Kplus/SwapDeals/6232',
              'Kplus/SwapDeals/6237',
              'Kplus/SwapDeals/6275','Kplus/SwapDeals/6276','Kplus/SwapDeals/6277',
              'Kplus/SwapDeals/6204','Kplus/SwapDeals/6206','Kplus/SwapDeals/6354']

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

def pushTrade(tradePath, typePath, output):
    url_push  = "https://fr1pslcmf05:8770/api/pricing/store/trade/"
    type = typePath.get()
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
    path = "C:/Users/jerpetit/PycharmProjects/uiPoc/"
    name = path+tradePath.get(1.0,END).replace("\n","")
    with open(name+".json", "r") as write_file:
        data = json.load(write_file)
        write_file.close()
    val = post(url_push,data)
    output.insert(END,val)

def priceBatch():
    df = pd.read_excel("dictionnaryIRS.xlsx")
    fcp_Trade = df["FCP"].values
    SB_trade =df["Kenibo427"].apply(lambda x : np.nan  if x is np.nan else "Kplus/SwapDeals/"+str(x).replace(".0","")).values
    df["FCP_VAL"] = priceArray(fcp_Trade,"FCP trade ")
    push_batch()
    df["SB_trade"] = priceArray(SB_trade,"SB trade ")
    df["diff"] = df["SB_trade"] - df["FCP_VAL"]
    df.to_excel("output.xlsx",engine="xlsxwriter")
    print("np written in the files")
    return None

def priceArray(vector,label):
    val = []
    for id in vector:
        if id is np.nan or id == "Kplus/SwapDeals/nan" or id in notPresent:
            val.append(np.nan)
        else:
            perimeter = {"trade": {"ids": [id]}}
            result = unitary(aod="2016-07-04", referenceCurrency="$id/USD", perimeter=perimeter,
                         scenarioContexts=scenarioContexts)
            if len(result) != 0:
                val.append(result[id]["scenarios"][0]["entries"][0]["measures"]["NPV"])
                print(label + id + " has been priced")
            else:
                 val.append(np.nan)
    return val

def push_batch():
    url = "https://fr1pslcmf05:8770/api/pricing/store/trade/ir-swap/batch"
    with open("IFcpIRSView.json", "r") as write_file:
        data = json.load(write_file)
        write_file.close()
    val = post(url, data)
    return None