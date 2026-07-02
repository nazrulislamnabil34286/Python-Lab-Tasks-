
sum=0

for a in range(2,1000):
    prime=True

    for b in range(2,a):
        if a%b==0:
            prime=False
            break
    if prime:
        sum=sum+a

print("Total sum : ",sum)

