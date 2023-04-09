import argparse
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument('-n', '--number', type=int, help='Number of tests', default=1, dest='number')
    args = parser.parse_args()

    if args.number <= 1:
        print(f"All Unit Tests successful!")
    else:
        print(f"{random.randint(0, args.number)}/{args.number} Unit Tests successful!")
