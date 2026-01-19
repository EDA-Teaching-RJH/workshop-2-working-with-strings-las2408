import math  

def main():
    A = input("What is side A's length? ")
    B = input("What is side B's length? ")
    A1 = int(A)
    B1 = int(B)
    pythag(A1,B1)

def pythag(A1,B1):
    C = ((A1 ** 2) + (B1 ** 2))
    print(C)

main()