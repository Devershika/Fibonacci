class Fibonacci:
    def __init__(self, n):
        self.n = n  # number of terms

    def generate_series(self):
        a, b = 0, 1
        series = []

        for _ in range(self.n):
            series.append(a)
            a, b = b, a + b

        return series


# Main program
n = int(input("Enter number of terms: "))

obj = Fibonacci(n)          # Object creation
result = obj.generate_series()  # Method call

print("Fibonacci Series:", result)
