with open("/home/tim/Projects/bachelor-thesis/chapters/05validation.tex") as f:
    lines = f.read().splitlines()

    tp = [0, 0] # true positives
    fn = [0, 0] # false negatives
    fp = [0, 0] # false positives

    p = [0, 0]
    r = [0, 0]
    f1 = [0, 0]

    found = False
    for index in [0,1]:
        for line in lines:
            if "% begin droidbench" in line:
                found = True
                continue
            if "% end droidbench" in line:
                found = False
                break
            if "%" in line or (not "&" in line):
                continue
            if not found:
                continue
            
            splitted = line.split("&")
            for seq in splitted[index+1].split():
                if "\\tp" in seq:
                    tp[index] += 1
                elif "\\fn" in seq:
                    fn[index] += 1
                elif "\\fp" in seq:
                    fp[index] += 1

        p[index] = tp[index] / (tp[index] + fp[index])
        r[index] = tp[index] / (tp[index] + fn[index])
        f1[index] = 2*p[index]*r[index] / (p[index] + r[index])


    print("\\tp &$", tp[0], "$&$", tp[1], "$\\\\")
    print("\\fp &$", fp[0], "$&$", fp[1], "$\\\\")
    print("\\fn &$", fn[0], "$&$", fn[1], "$\\\\")
    print("Precision & $", round(p[0]*100, 2), "\\%$ & $", round(p[1]*100, 2), "\\%$\\\\")
    print("Recall & $", round(r[0]*100, 2), "\\% $ & $", round(r[1]*100, 2), "\\%$\\\\")
    print("F1 measure & $", round(f1[0], 2), "$ & $", round(f1[1], 2), "$\\\\")