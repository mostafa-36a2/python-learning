from collections import defaultdict

d = defaultdict(list)
d["m"].append("Hello World")
d["m"].append("Byebye")
d["n"].append("Hello World")
d["n"].append("Byebye")

write_file = open("/tmp/test_write_file.txt","w")
for key, value in d.items():
    print(key,value,sep=":",end="\n",file=write_file,flush=True)
