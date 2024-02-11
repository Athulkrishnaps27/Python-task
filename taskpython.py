row=int(input("Enter the row"))
col=int(input("Enter the colomn"))
n=1
for y in range(col):
    if n<=4:
        if n==1:
            print(r' ___     ___     ___     ___     ')
        for x in range(row):
            print(r'/   \___',end="")
        print()
        for x in range(row):
            print(r'\___/   ',end="")
        print()
        n+=1


