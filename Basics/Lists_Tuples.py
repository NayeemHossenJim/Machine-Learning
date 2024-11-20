#List are changable , can have duplicte value also ordered []
FirstList = ["Lambo","Tesla","Ferrari"]
print(len(FirstList))
print(type(FirstList))
print(FirstList)

if "Lambo" in FirstList:
    FirstList.pop(2)
    FirstList.append("Ferrari is Beast")
    print(FirstList)

List = list(("Rune","Dune","Some")) # Use constructor same for tuples
if "Dune" in List:
    print("Kaise Ho App Lok")

SortedList = [2,4,58,5]
SortedList.sort()
print(SortedList)

#For Tuples we use () first perenthesis
#Tuples are unchangable ,can have duplicte value also ordered

Tuples = ("Jim","Topu","Rimon","Sojeb","Joy")
for i in range(len(Tuples)):
    print(Tuples[i])
if "Sojeb" in Tuples:
    print("Sojeb is Gay")