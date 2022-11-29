lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
countOfPrime = 0
countOfComposite = 0

for i in range(lower,upper + 1):
    if(i == 1):
        print(i, "is neither prime nor composite")
        continue
    f = 0
    for j in range(2, i):
        if (i % j == 0):
            f = 1
            break
    if (f == 0):
        countOfPrime += 1
        print(i, "is a prime number")
    else:
        countOfComposite += 1
        print(i, "is a composite number")

print("The number of the prime number in", lower, "-", upper, "are :", countOfPrime)
print("The number of the compositer number in", lower, "-", upper, "are :", countOfComposite)