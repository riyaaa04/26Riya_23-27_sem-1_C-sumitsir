#Define a class with a generator which can iterate the numbers, which are divisibleby 7, between a given range 0 and n.
class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Get user input for the range
n = int(input("Enter the value of n: "))

# Create an instance of the class
generator_instance = DivisibleBySevenGenerator(n)

# Iterate and print numbers divisible by 7
print(f"Numbers divisible by 7 in the range 0 to {n}:")
for num in generator_instance.generate_divisible_by_seven():
    print(num, end=' ')
