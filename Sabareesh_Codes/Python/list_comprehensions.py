# Python program: List Comprehensions and Filtering
# Date: 2026-08-29

def demonstrate_comprehensions():
    numbers = list(range(1, 21))
    
    # Even squares
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print("Even squares:", even_squares)
    
    # Filter prime candidates
    primes = [x for x in numbers if x > 1 and all(x % d != 0 for d in range(2, int(x**0.5) + 1))]
    print("Primes up to 20:", primes)

if __name__ == "__main__":
    demonstrate_comprehensions()
