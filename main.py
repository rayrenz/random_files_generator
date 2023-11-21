import string
import random


def generate(n: int):
    """Generate n number of files with random data in them with size 1 to 10KB each"""
    for i in range(n):
        with open(f"./files/file_{i}.txt", "w+") as f:
            f.write("".join(random.choices(string.ascii_letters, k=random.randint(1000, 10000))))

if __name__ == '__main__':
    generate(100000)