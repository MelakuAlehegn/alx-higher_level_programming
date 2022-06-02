#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_sum = 0
    for i in range(1, len(argv)):
        num_sum += int(argv[i])
    print(f"{num_sum}")
