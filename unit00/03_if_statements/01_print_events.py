def print_even_numbers(count: int = 20):
    """
    Pehle 'count' even numbers print karega.
    """
    even_numbers = [num * 2 for num in range(count)]  # List comprehension ka use
    print(" ".join(map(str, even_numbers)))  # Numbers ko space-separated format me print karna

def main():
    print_even_numbers()

if __name__ == "__main__":
    main()
