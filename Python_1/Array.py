import numpy as np

arr=(1, 2, 3, 4, 5,"prj")
for i in arr:
        print(i,end=" ")

print("\n")
b = np.empty(3, dtype = int)
print("Matrix b : \n", b)
print(b[0])    

'''
arr = array.array('i', [1, 2, 3]) 
print ("The new created array is : ",end="")
for i in range (0,3):
    print (arr[i], end=" ")

print ("\r")
print("B\n", np.linspace(2.0, 3.0, 10), "\n")    
print("\n")

a = np.empty_like([2, 2], dtype = int) 
print("\nMatrix a : \n", a) 
  
c = a = ([1,2,3], [4,5,6]) 
print("\nMatrix c : \n", np.empty_like(c)) '''

print(type(arr))
'''import os 
  
logout = input("Do you wish to log out your computer ? (yes / no): ") 
  
if logout == 'no': 
    exit() 
else: 
    os.system("shutdown -l") '''
if (30 and 0):
    print("Its true")
else:
    print("Its false")
