
print("Hello Everyone!")


# print with parameters
import sys

print("My","Name","is","mostafa",sep=" ",end="\n",file=sys.stdout,flush=True)

outputfile = open('/tmp/outputfile.txt', "w")
print("My","Name","is","mostafa",sep=" ",end="\n",file=outputfile,flush=True)

print(1,2,3,4,"test",type("my string"),["lists","are","simpe"],{"dicts":"are","amazing":"for you"})
