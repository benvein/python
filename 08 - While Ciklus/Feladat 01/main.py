from os import system

num: int = None

print("0 és 9 közötti szám: ",end="")
num = int(input())

while (num<0) or (num>10):
    print("nem jó")
    num = int(input())