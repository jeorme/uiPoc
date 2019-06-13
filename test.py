import json
import os
if __name__=="__main__":
    path = "C:\\Users\\jerom\\PycharmProjects\\uiPoc\\fxspot\\"
    data_list=[]
    for filename in os.listdir(path):
        with open(path+filename,"r") as write_file:
            data = json.load(write_file)
            write_file.close()
        data_list.append(data)

    with open("FxSpotView.json","w") as file:
        json.dump(data_list,file)