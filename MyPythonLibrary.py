def bubbleSort(ArrayToSort): #Sort an array and return the sorted version
    for passnum in range(len(a)-1,0,-1):
        for i in range(passnum):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    return a

def Array_Sum(a,b): #Sum two arrays, and return the final array
    #take the sizer
    sizea = len(a)
    sizeb = len(b)
    #define size of the bigger and what is the bigger and the sort array
    if sizea > sizeb:
        size = sizea
        bigger = a
        short = b
    else:
        size = sizeb
        bigger = b
        short = a
    #creates the final array
    c = [None]* size
    #sum the values, if the short index is over, copy the value from the bigger
    for i in range (size):
        try:
            c[i] = short[i] + bigger[i]
        except IndexError:
            c[i] = bigger[i]
    return c

def TriangleType(a,b,c): #Receives three sides of triangle and display it's type  
    if (a==0 or b==0 or c==0):
        print ("it is not a triangle")
    elif (a==b and b==c):
        print("the triangle is equilateral")
    elif (a==b or b==c or a ==c):
        print ("the triangle is isosceles")
    elif (a!=c and b!=c and a!=c):
        print ("the triangle is scalene")

def isprimenumber (n): #receive a number and check if is prime
    cont=0
    cont2=0
    while (cont<=n):
        cont=cont+1
        resto=n%cont
        
        if (resto == 0):
            cont2=cont2+1
        if (cont2>=3):
            #print("Is not a prime number")
            return False
            break
    else:
        #print("Is a prime number")
        return True

def Identity(matrix,rows,columns): #Receive a matrix and define if it is Identity or not
    if rows != columns:
        return (False)
    for i in range (rows):
        if matrix[i][i]!=1:
            return (False )
            break
        else:
            return (True)

def MatrixMinimum (matrix,rows,columns):
    smaller = matrix[rows-1][columns-1]
    for i in range(rows):
            for j in range(columns):
                    if smaller>matrix[i][j]:
                        smaller = matrix[i][j]
    return (smaller)

def Factorial (n): #returns the factorial of a number
    fator=1
    acm=1
    while fator<=n:
        acm=acm*fator
        fator=fator+1
    return acm

def MatrixSum (Matrixa, Matrixb, rows, columns): #Sum two matices of same size and returns the sum matrix
    c=[[5 for i in range (1,columns+1)] for i in range (1,rows+1)]
    for i in range(rows):
            for j in range(columns):
                    c[i][j]=Matrixa[i][j]+Matrixb[i][j]
    return (c)

