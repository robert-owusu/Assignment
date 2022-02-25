#Importing Numpy Function
from numpy import *

#Question 1.A
#Creating a 2x3 Matrix
Mat=matrix('1,2,3 ; 4,5,6')
#Multiplying by Scalar=2
Mat1=Mat*2
#print(Mat1)

#Question 1.B
#Creating a 3x3 Identity Matrix
MatId=identity(3)
#print(MatId)

#Question1.C
#Creating 1D array
arry1=array([range(1,28)])
#print(arry1)

#Converting 1D to 3D
arry2=arry1.reshape(3,3,3)
#print(arry2)

#Question1.D
#Creating 2 1D Arrays
Array1=array([range(1,7)])
Array2=array([range(7,13)])
#print(Array1)
#print(Array2)

#Converting into 2D Arrays
ArrayA=Array1.reshape(2,3)
ArrayB=Array2.reshape(2,3)
#print(ArrayA)
#print(ArrayB)

#Horizontal Stack of 2D Arrays
Stack1=hstack((ArrayA,ArrayB))
#print(Stack1)

#Vertical Stack of 2D Arrays
Stack2=vstack((ArrayA,ArrayB))
#print(Stack2)

#Question1.E
#Creating an equally spaced sequence from 0-100
Seq=linspace(0,100,5)
#print(Seq)
















