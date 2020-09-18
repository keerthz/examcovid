f=open("covid.csv","r")
dict={}


for lines in f:
    data=lines.rstrip("/n").split(",")
    state=data[1]
    confirm=data[4]
    recovered=data[6]
    death=data[5]
    if(state not in dict):
        dict[state]={"confirmed":confirm,"recovered":recovered,"death":death}
    else:
        dict[state]={"confirmed": confirm, "recovered": recovered, "death": death}

def Fetchdata(**kwargs):
    if(kwargs["state"] not in dict):
        print("no result found")
    else:
        for k,v in dict.items():
            if(k==kwargs["state"]):
                print("total confirmed cases:", v["confirmed"])
                if("high" in kwargs):
                    val=kwargs["high"]
                if(val=="recovered"):
                    print("recovered:",v["recovered"])
                elif(val=="death"):
                    print("death:",v["death"])
Fetchdata(state="Kerala",high="recovered")