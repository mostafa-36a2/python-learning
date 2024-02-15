import re

txt = "The ralseiohgfilsdhfgilhsd ;ogihw 34;o8rhy 24;9y r;o45et in Spain"
x = re.search("^The.*Spain$", txt)
if x is not None:
    print("Found")
else:
    print("Bad format")

article = "Hello World!"
article = re.sub(r"[aeoui]", "", article)
print(article)

nrt_filename_pattern = re.compile("NR([A-Z0-9]{5})([A-Z0-9]{5})([0-9]{7})")
filename = "NRSYR01SYRSP0000102"
if nrt_filename_pattern.match(filename):
    print(f"{filename} match")

filename = "NRSYR01SYR.P0000102"
if not nrt_filename_pattern.match(filename):
    print(f"{filename} not match")
