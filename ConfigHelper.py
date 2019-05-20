import ApiHelper

def getPricingId(configName):
    urlConfig = "https://fr1pslcmf05:8770/api/pricing/configs"
    config = ApiHelper.get(urlConfig)
    for item in config:
        if (item['name']==configName):
            return item["id"]
    return "error"


if __name__=="__main__":
    getPricingId("DEFAULT")
