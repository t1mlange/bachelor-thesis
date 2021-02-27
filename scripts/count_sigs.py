import re
import glob

for fname in glob.glob("/home/tim/Projects/bachelor-thesis/scripts/susi/*.txt"):
  with open(fname, "r") as f:
    text = f.read()
    matches = re.findall(r"<(.*?): (.*?) (.*?)\((.*?)\)>", text)
    print(f"{fname.split('/')[-1]}: {len(matches)} signatures")