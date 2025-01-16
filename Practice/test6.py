#number of x's in a row
numbers = [5, 2, 5, 2, 2]

#for x in numbers:
#    print("x" * x)

for x in numbers:
    for y in range(x):
        print("x", end= "")
    print()
    