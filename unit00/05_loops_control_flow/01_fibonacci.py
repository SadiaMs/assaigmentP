MAX_TERM_VALUE = 10000  # Maximum limit
def main():
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Terms ko ek hi line mein print karna
        
        # Next Fibonacci term calculate karna
        curr_term, next_term = next_term, curr_term + next_term

if __name__ == '__main__':
    main()
