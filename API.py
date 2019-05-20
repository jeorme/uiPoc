from ApiHelper import  unitary

scenarioContexts =[

    {
      "id": "base",
      "measureGroupIds": [
        "NPV"
      ]
    }

]
perimeter = {"trade" : {"ids": ["FXOptionVanilla_1"]}}

result = unitary(aod="2016-07-04",referenceCurrency="$id/USD",perimeter=perimeter, scenarioContexts = scenarioContexts)
print(result)