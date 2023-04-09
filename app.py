import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument('name', type=str, help='Name of the person')
    parser.add_argument('-r', '--repeat', type=int, help='Repeat message x times.', default=1, dest='repeat')
    args = parser.parse_args()

    for i in range(args.repeat):
        print(f"Hello, {args.name}!")

    #  docker run --rm -it --volume "$(pwd)":/data container-test data/mock.csv
