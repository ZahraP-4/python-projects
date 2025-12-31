#This program reads tea sales from tea.txt,stores and prints a sales report.

#Processing/Output
def main():
    teaDict = {}
    infile = open("tea.txt", "r")
    lineStr = infile.readline()
    lineStr = lineStr.rstrip("\n")
    while lineStr != "":
        fields = lineStr.split(":")
        teaName = fields[0]
        store1 = float(fields[1])
        store2 = float(fields[2])
        store3 = float(fields[3])
        teaDict[teaName] = [store1, store2, store3]
        lineStr = infile.readline()
        lineStr = lineStr.rstrip("\n")
    infile.close()
    store1Total = 0.0
    store2Total = 0.0
    store3Total = 0.0
    for teaName in sorted(teaDict):
        store1 = teaDict[teaName][0]
        store2 = teaDict[teaName][1]
        store3 = teaDict[teaName][2]
        teaTotal = store1 + store2 + store3
        print(format(teaName, "12"),
              format(store1, "10.2f"),
              format(store2, "10.2f"),
              format(store3, "10.2f"),
              format(teaTotal, "10.2f"))
        store1Total = store1Total + store1
        store2Total = store2Total + store2
        store3Total = store3Total + store3
    print(" " * 12,
          format(store1Total, "10.2f"),
          format(store2Total, "10.2f"),
          format(store3Total, "10.2f"))
if __name__ == "__main__":
    main()
