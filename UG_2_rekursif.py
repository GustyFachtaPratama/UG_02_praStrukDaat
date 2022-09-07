import time

def DeretAjaib(y):
    if y < 6:
        return y
    else:
        return DeretAjaib(y-2) + DeretAjaib(y//2)

for i in range(1,100):
    b = DeretAjaib(i)
    print(b,end=" ")


start = time.time()

end = time.time()
print()
print("waktu yang di tempuh",end-start)

