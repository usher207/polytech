import math

N = int(input("Введіть ціле число N (N > 1): "))

if N > 1:
    is_prime = True
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            is_prime = False 
            break
        
    if is_prime:
        print("TRUE")
    else:
        print("FALSE")
else:
    print("N < 1 or = 1")
