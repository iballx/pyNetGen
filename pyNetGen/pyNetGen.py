def main():
    in_file = open("C:\\Users\\Andrew\\Documents\\netlist.csv",'r')
    ColList = []
    Netlist = {}
    StoreNets = False
    for LineNo, LineText in enumerate(in_file):
        cells = [x.strip() for x in LineText.split(',')]
        if LineNo == 1:
            for ColNo,CellText in enumerate(cells):
                if (CellText.strip().lower() == "connector") & (ColNo > 0):
                    ColList.append(ColNo)
            StoreNets = True # Now that we have the connector columns we can start storing the nets
        elif StoreNets:
            for x in ColList:
                if len(cells[x]):
                    if cells[0] not in Netlist:
                        Netlist[cells[0]] = []
                    Netlist[cells[0]].append(cells[x]+':'+cells[x+1])
    in_file.close()
    MaxNetNameLength = max(len(x) for x in Netlist.keys())
    MaxLineLength = 20
    out_file = open("netlist.txt",'w')
    for x in sorted(Netlist.keys(),key=str.lower):
        s = str.format("{0:.<{1}}".format(x,MaxNetNameLength))+' '
        for i,v in enumerate(Netlist[x]):
            if len(s) + len(v) + 1 > MaxLineLength:
                out_file.write(s+'\n')
                s = (MaxNetNameLength+1)*" "
            s += v;
            test = len(Netlist[x])
            if i != len(Netlist[x])-1:
                s += ','
        out_file.write(s+'\n')
    out_file.close()

if __name__ == "__main__":
    main()