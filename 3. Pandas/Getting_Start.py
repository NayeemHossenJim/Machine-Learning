import pandas as pd
print(pd.__version__)

a = {"Jim" :1,"Im" :2,"Lim" :3}
b = pd.Series(a)
print(b)

c = {
    "Name" : ["Topu","Jim","Sojeb"],
    "DickSize" : [0.7,10,0.8]
}
d = pd.DataFrame(c, index=("Choto_Nunu","OMaiGod","3_Bichi"))
print(d )
print("\n")
print(d.loc["Choto_Nunu"])
