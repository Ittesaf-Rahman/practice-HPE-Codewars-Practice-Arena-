def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq

n_terms = int(input("Enter the number of terms: "))

if n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Sequence:")
    for num in fibonacci(n_terms):
        print(num, end=" ")