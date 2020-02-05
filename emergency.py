from ApiHelper import *

## add FXO option
url_fxo = "http://fxoqa2-tower.misys.global.ad:8198/api/pricing/store/trade/fx-option"
fxo = openJson("FXO1103.json")
post(url_fxo,fxo)


