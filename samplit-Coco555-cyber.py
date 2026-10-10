import sys
import random


def main():
    file = sys.argv[1]

    with open(file) as f:
        for line in f:
            if random.random() < 0.01:
                print(line)

if __name__ == "__main__":
    main()