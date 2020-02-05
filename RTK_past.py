from ApiHelper import *

trade = ["Kplus1/SpotDeals/5892"]
pricing_config = "%24id%2FDEFAULT-FXO"

def build_entity_request(trade, mdId = "$id/DEFAULT",asOf="2016-07-05",pricerResolver = "ccecc93d6a414527a463486644d56b7a",rfResolver = "87cdffb0f9994821a4efb3f28d33f3d4"):
    input_request = {"asOfDate": asOf, "marketDataSetId": mdId,
                     "perimeter": { "retrieveDate": asOf+"T00:00:00",
                                    "trade": {"ids": trade
                                              }
                                    },
                     "pricerResolverConfigId": pricerResolver,
                     "pricingMethod": "PRACTICAL",
                     "riskFactorResolverConfigId": rfResolver
                     }
    return input_request
##get pricing config
url_pricing_config = "http://fr1cslbmto0014:8198/api/pricing/configs"
pricing_config = get(url_pricing_config+"/"+pricing_config)
pricerResolver = pricing_config['pricerResolverConfigId']
rFresolver = pricing_config["riskFactorResolverConfigId"]
##get the entity
url_entity = "http://fr1cslbmto0014:8198/api/pricing/resolve-entity-risk-factors"
entity_input = build_entity_request(trade,pricerResolver = pricerResolver, rfResolver = rFresolver)
answer = post(url_entity,entity_input)
print(answer)

##price with entity
