import numpy
def mat_multiply(a,b):
	c={}
	print("Matrix C is")
	for i in range(r1):
		for j in range(c2):
			c[i,j]=0	
			for k in range(c1):
				c[i,j]+=(A[i,k]*B[k,j])
			print(c[i,j]), '\t',
		print('\n')


r1=input("No. of rows in matrix1 : ")
c1=input("No. of columns in matrix1 : ")
print("Enter matrix A ")
A=numpy.empty((r1,c1))
for i in range(r1):
	for j in range(c1):
		A[i,j]=input("")
print("Matrix A is ")
for i in range(r1):
	for j in range(c1):
		print(A[i,j]), '\t',
	print
print('\n')
r2=input("No. of rows in matrix2 : ")
c2=input("No. of columns in matrix2 : ")
B=numpy.empty((r2,c2))
print("Enter matrix B ")
for i in range(r2):
	for j in range(c2):
		B[i,j]=input("")
print("Matrix B is ")
for i in range(r2):
	for j in range(c2):
		print(B[i,j]), '\t',
	print
print('\n')

mat_multiply(A,B)