N = int(input("Введіть ціле число N (N > 0): "))

if N > 0:
    reversed_N = 0 
    
    while N > 0:
        last_digit = N % 10  
        reversed_N = reversed_N * 10 + last_digit  
        N = N // 10  
        
    print(f"reversed N: {reversed_N}")
else:
    print("error: N < or = 0")
