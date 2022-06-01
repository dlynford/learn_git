# 6/1/2022
# I am learning how to commit, push, and pull files on Github.
def main():
    digits = []
    for i in range(25):
        digits.append(i)
    return digits


def add_up(a, b):
    total = a + b
    return total


def calculate(f, a, b):
    return f(a, b)


if __name__ == '__main__':
    print(calculate(add_up, 7, 8))
    print(main(), 'hello')
