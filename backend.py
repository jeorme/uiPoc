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


notPresent = ['KSwapDeals/6224','KSwapDeals/6228',
              'KSwapDeals/6232','KSwapDeals/6167','KSwapDeals/6185','KSwapDeals/6268',

              'KSwapDeals/6275','KSwapDeals/6276','KSwapDeals/6277',
              'KSwapDeals/6204','KSwapDeals/6206'
                ,"FxForward_10",	"Kplus1/ForwardDeals/1364","FxForward_06",	"Kplus1/ForwardDeals/1363","FxForward_07",	"Kplus1/ForwardDeals/1358","FxForward_11",	"Kplus1/ForwardDeals/1369"



              ]

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
    path = "C:/Users/jerom/PycharmProjects/uiPoc/"
    name = path+tradePath.get(1.0,END).replace("\n","")
    with open(name+".json", "r") as write_file:
        data = json.load(write_file)
        write_file.close()
    val = post(url_push,data)
    output.insert(END,val)

def priceBatch(tradePath,typePath,output):
    type = typePath.get()
    dict = "dictionnary"
    if type == "SWAP":
        dict = dict+"IRS.xlsx"
    elif type == "FX SPOT":
        dict = dict + "fx-spot.xlsx"
    elif type == "FX FORWARD":
        dict = dict + "fx-forward.xlsx"
    elif type == "FX SWAP":
        dict = dict + "fx-swap.xlsx"
    elif type == "FXO VANILLA":
        dict = dict + "fx-option.xlsx"
    else:
        print("error instrument not defined")
    df = pd.read_excel(dict)
    fcp_Trade = df["FCP"].values
    SB_trade =df["kenobi427"].values
    df["FCP_VAL"] = priceArray(fcp_Trade,"FCP trade ")
    push_batch(tradePath,typePath,output)
    df["SB_trade"] = priceArray(SB_trade,"SB trade ")
    df["DIF"] = df["SB_trade"] - df["FCP_VAL"]
    df.to_excel("output"+type.replace(" ","_")+".xlsx",engine="xlsxwriter")
    print("written in the files")
    return None

def priceArray(vector,label):
    val = []
    for id in vector:
        if id is np.nan or id == "KSwapDeals/nan" or id in notPresent:
            val.append(np.nan)
        else:
            perimeter = {"trade": {"ids": [id]}}
            result = unitary(aod="2016-07-04", referenceCurrency="$id/USD", perimeter=perimeter,
                         scenarioContexts=scenarioContexts)
            val.append(result[id]["scenarios"][0]["entries"][0]["measures"]["NPV"])
            print(label + id + " has been priced")
    return val

def push_batch(tradePath,typePath,output):
    url_push = "https://fr1pslcmf05:8770/api/pricing/store/trade/"
    type = typePath.get()
    if type == "SWAP":
        url_push = url_push + "ir-swap/batch"
    elif type == "FX SPOT":
        url_push = url_push + "fx-spot/batch"
    elif type == "FX FORWARD":
        url_push = url_push + "fx-forward/batch"
    elif type == "FX SWAP":
        url_push = url_push + "fx-swap/batch"
    elif type == "FXO VANILLA":
        url_push = url_push + "fx-option/batch"
    else:
        print("error instrument not defined")
    path = "C:/Users/jerom/PycharmProjects/uiPoc/"
    name = path + tradePath.get(1.0, END).replace("\n", "")
    with open(name + ".json", "r") as write_file:
        data = json.load(write_file)
        write_file.close()
    val = post(url_push, data)
    output.delete(1.0, END)
    output.insert(END, val)
