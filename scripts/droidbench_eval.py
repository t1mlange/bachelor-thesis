import itertools

filenames = [
    "/home/tim/Projects/bachelor-thesis/scripts/droidbench_data/easyfw.txt",
    "/home/tim/Projects/bachelor-thesis/scripts/droidbench_data/easybw.txt",
    ]
dic = {}

class TestResult:
    def __init__(self, name, infoflow, alias):
        self.name = name
        self.infoflowFw = int(infoflow)
        self.aliasFw = int(alias)
        self.infoflowBw = -1
        self.aliasBw = -1
        self.infoflowDiff = "-"
        self.aliasDiff = "-"
        self.totalDiff = "-"
        self.relativeDiff = "-"

    def setEdges(self, infoflow, alias):
        self.infoflowBw = int(infoflow)
        self.aliasBw = int(alias)

        if self.infoflowFw != -1 and self.infoflowBw != -1:
            self.infoflowDiff = self.infoflowBw - self.infoflowFw
            self.aliasDiff = self.aliasBw - self.aliasFw
            self.totalDiff = self.infoflowDiff + self.aliasDiff 

    def toString(self):
        return f"{self.name} & ${self.infoflowFw}$ & ${self.aliasFw}$ & ${self.infoflowBw}$ & ${self.aliasBw}$ & ".replace("-1", "-") + f"${self.infoflowDiff}$ & ${self.aliasDiff}$ & ${self.totalDiff}$\\\\\n"

    def __lt__(self, other):
         return self.name < other.name

for i, fname in enumerate(filenames):
    with open(fname) as f:
        for line in f.read().splitlines():
            split = line.split(",")
            category = split[0]
            name = split[1]
            infoflow = split[2]
            alias = split[3]
            
            if not category in dic:
                dic[category] = {}
            if i == 0 and not name in dic[category]:
                dic[category][name] = TestResult(name, infoflow, alias)
            elif i == 1:
                if not name in dic[category]:
                    dic[category][name] = TestResult(name, -1, -1)
                dic[category][name].setEdges(infoflow, alias)

string = ""
summary = [0,0,0,0,0,0,0,0]
count = 0
for k, v in dic.items():
    string += "\\hline\n\\tsubEight{%s}\n" % k
    for k2, v2 in sorted(v.items()):
        string += v2.toString()
        if v2.totalDiff != "-":
            summary[0] += v2.infoflowFw
            summary[1] += v2.aliasFw
            summary[2] += v2.infoflowBw
            summary[3] += v2.aliasBw
            summary[4] += v2.infoflowDiff
            summary[5] += v2.aliasDiff
            summary[6] += v2.totalDiff
            count += 1
string += "\\hline\\hline"
print(string)
for i in range(0, len(summary)):
    summary[i] = round(summary[i] / count, 2)
print(f"$\\varnothing$ Propagations & ${summary[0]}$ & ${summary[1]}$ & ${summary[2]}$ & ${summary[3]}$ & ${summary[4]}$ & ${summary[5]}$ & ${summary[6]}$")