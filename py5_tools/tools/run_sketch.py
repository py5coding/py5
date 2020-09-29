import argparse

from py5_tools import run


parser = argparse.ArgumentParser(description="Execute py5 sketch",
                                 epilog="this is the epilog")
parser.add_argument(
    action='store',
    dest='sketch_path',
    help='path to py5 sketch')
parser.add_argument('-c', '--classpath', action='store', dest='classpath',
                    help='extra directories to add to classpath')


def main():
    args = parser.parse_args()
    run.run_sketch(args.sketch_path, classpath=args.classpath)


if __name__ == '__main__':
    main()
