from ApiHelper import get,post
import json

if __name__=="__main__":
    url_yc_def = "https://fr1pslcmf05:8770/api/pricing/store/market-data/yield-curve-definitions"
    url_yc_values = "https://fr1pslcmf05:8770/api/pricing/store/market-data/yield-curve-values"
    reponses_def = get(url_yc_def)
    reponses_values = get(url_yc_values+"/?date=2016-07-05")
    dict_yc = ["EUROIS","GBPOIS","USDOIS","MXNOIS","CLPGOV","UDISBMT","JPYXUSD","JPYOIS","HKDDISC","CHFOIS","CAD-LIBOR","CNYCNNDS","EURABSE","USDSBQL","USDSBML","USDSBSL","EURAMME","EURABQE","GBPSBQL","JPYSBQL","GBPSBSL","JPYSBSL","CHFAMQL","CHFABSL"]
    id_def = {}
    id_values = {}
    #for uc in reponses_def:
    #    if(uc["name"] in dict_yc):
    #        id_def[uc["name"]] = uc["id"]
    #for uc in reponses_values:
    #    if(uc["name"] in dict_yc):
    #        id_values[uc["name"]] = uc["id"]

    #for key in id_def.keys():
    #    yc_def = get(url_yc_def+"/"+id_def[key])
    #    with open(key+"_def.json","w") as file:
    #        json.dump(yc_def,file)

    #for key in id_values.keys():
    #    yc_val = get(url_yc_values+"/"+id_values[key])
    #    with open(key+"_val.json","w") as file:
    #        json.dump(yc_val,file)

    ## post service
    ##crete yield curve : batch

    url_yc_name = "http://fr1cslbmto0013:8198/api/pricing/store/market-data/yield-curves"
    url_yc_def = "http://fr1cslbmto0013:8198/api/pricing/store/market-data/yield-curve-definitions"
    url_yc_values = "http://fr1cslbmto0013:8198/api/pricing/store/market-data/yield-curve-values"
    for yc in dict_yc:
        id = {"name" : yc+"V","id":"Kplus1/YC/"+yc+"V"}
        post(url_yc_name,id)
        with open(yc+"_def.json","r") as write_file:
            data = json.load(write_file)
            data["name"] = yc+"V"
            if yc=="USDSBSL":
                print("toto")
            post(url_yc_def,data)
            write_file.close()
        with open(yc+"_val.json","r") as write_file:
            data = json.load(write_file)
            data["name"] = yc+"V"
            post(url_yc_values,data)
            write_file.close()

    ## post service
    ##crete yield curve values :batch

    ## post service
    ##crete yield curve def : batch
