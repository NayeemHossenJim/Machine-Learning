import numpy as nb
a = nb.array([1,2,3])
print(a)

#to use 2D array be careful to third bracket
b = nb.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]]) 
print(b)

#ndim = Number of Dimension
print("Number of Dimension in A : " +str(b.ndim))

#Number of row & col
print("Shape of B: " + str(b.shape))

#dtype = Data Type
print("Type of A: " + str(a.dtype))

#You can also define Data type in any array out of third bracket by using dtype = int16
print("Size of A : " + str(a.itemsize))

#nbytes = Number of Bytes
print("Size of A : " + str(a.nbytes))

#Get speicific element
print("Specific Element: "+str(b[0,4]))

#Get speicific Row
print("Specific Row: "+str(b[0,:]))

#Get speicific Coloumn
print("Specific Coloumn: "+str(b[:,4]))

#Stepping
print("Stepping : " + str(b[0, 1:6:2]))

#Change any Element
b[1,3] = 20
print(b)
#Change A whole Row/Coloumn
b[:,3] = [1,2]
print(b)


#3D Array
print("3D Array")
c = nb.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(c)

#Get speicific element
print("Specific Element: "+str(c[1,0,2]))

#Change in 3D Array
c[1,1,1] = 0
print(c)