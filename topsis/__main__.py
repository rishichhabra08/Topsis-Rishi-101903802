def main():
    import pandas as pd
    import numpy as np
    import argparse

    parser = argparse.ArgumentParser(description='TOPSIS')

    parser.add_argument("-f", "--filepath", type=str, help="Enter input File", dest="filepath")
    parser.add_argument("-w", "--weights", type=str, default="1,1,1,1,1", help="Enter Weights", dest="weights")
    parser.add_argument("-i", "--impacts", default="-,+,+,+,+", help="Enter impacts", dest="impacts")
    parser.add_argument("-o", "--output", type=str, help="Enter Output File", dest="output")


    args = parser.parse_args()
    print(args.filepath, args.weights, args.output, args.impacts,args.output)

    filename = args.filepath
    weights = args.weights
    impacts = args.impacts
    output = args.output


    weights = weights.split(",")
    weights = [float(i) for i in weights]
    impacts = impacts.split(",")


    excel_file = pd.read_excel(filename)
    csv_file = excel_file.to_csv("data.csv", index=None, header=True)


    df = pd.read_csv("data.csv")
    # print(df)

    newdf = df
    # print(newdf)

    rows, cols = newdf.shape
    # print(rows, cols)

    # for i in range(cols):
    #     sum=0
    #     for j in range(rows):
    #         sum = sum+newdf.iloc[j,i]**2
    #         print(newdf.iloc[j,i])
    #     print(sum)
    #     print("\n")
    #     sum = sum**0.5
    #     print(sum)
    #     print("\n")

    # print(newdf.columns[1:])

    totalSum = []
    for i in newdf.columns[1:]:
        square = newdf[i] * newdf[i]
        s = sum(square)
        totalSum.append(s)

    totalSum = np.array(totalSum)
    sqrtarr = np.sqrt(totalSum)

    # print(totalSum,sqrtarr)

    for i, ele in enumerate(newdf.columns[1:]):
        # print(newdf[ele] / sqrtarr[i])
        newdf[ele] = newdf[ele] / sqrtarr[i]

    # print(newdf)
    # print(weights)

    for i, ele in enumerate(newdf.columns[1:]):
        newdf[ele] = newdf[ele] * weights[i]
        # print(newdf[ele]*weights[i])

    # print(newdf)

    best = [0] * cols
    worst = [0] * cols
    for i, ele in enumerate(newdf.columns[1:]):
        # print(newdf[ele])
        best[i] = newdf[ele].max()
        worst[i] = newdf[ele].min()
        if impacts[i] == "-":
            best[i], worst[i] = worst[i], best[i]
        # print(best[i], worst[i])

    totalEucl = []

    euclbest = []
    euclworst = []
    topsis_score = []

    for i in range(rows):
        eb = 0
        ew = 0
        for j, ele in enumerate(newdf.columns[1:]):
            # print(newdf.iloc[i][j+1])
            eb = eb + ((newdf.iloc[i][j + 1] - best[j]) ** 2)
            ew = ew + ((newdf.iloc[i][j + 1] - worst[j]) ** 2)

        ew = ew ** 0.5
        eb = eb ** 0.5
        euclbest.append(eb)
        euclworst.append(ew)
        # print(euclbest[i],euclworst[i])

        topsis_score.append(euclworst[i] / (euclbest[i] + euclworst[i]))
        # print(topsis_score[i])
        # print("\n")

    newdf["Topsis Score"] = topsis_score

    newdf["Rank"] = (newdf["Topsis Score"].rank(method="max", ascending=False))
    newdf = newdf.astype({"Rank": "int"})

    # print(newdf)

    newdf.to_csv(output, index=None)


if __name__ == '__main__':
    main()