#!/usr/bin/python3
def main():
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    result = 0

    if op not in operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    for operator in operators.keys():
        if operator == op:
            result = operators[operator](a, b)
            break
    print(f"{a} {op} {b} = {result}")


if __name__ == "__main__":
    main()