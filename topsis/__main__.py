def main():
    import pandas as pd
    import numpy as np
    import argparse

    parser = argparse.ArgumentParser(description='TOPSIS')

    parser.add_argument("-f", "--filepath", type=str, help="Enter input File", dest="filepath")
    parser.add_argument("-w", "--weights", type=str, default="1,1,1,1,1", help="Enter Weights", dest="weights")
    parser.add_argument("-i", "--impacts", default="-,+,+,+,+", help="Enter impacts", dest="impacts")
    parser.add_argument("-o", "--Output", type=str, help="Enter Output File", dest="output")

    args = parser.parse_args()
    print(args.filepath, args.weights, args.output, args.impacts)


if __name__ == '__main__':
    main()