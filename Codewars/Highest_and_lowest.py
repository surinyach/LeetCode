def high_and_low(numbers):
    n = list(map(int, numbers.split()))
    return f"{max(n)} {min(n)}"