from os import system
system("cls")

print("életkor: ",end="")
eletkor=int(input())

while (eletkor<0) or (eletkor>100):
    print("érvényes életkort adjon meg")
    eletkor=int(input())

if eletkor>0 and eletkor<7:
    print("gyerek")
elif eletkor>7 and eletkor<19:
    print("iskolás")
elif eletkor>19 and eletkor<66:
    print("dolgozó")
else:
    print("nyugdíjas")
    