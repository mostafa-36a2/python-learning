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
