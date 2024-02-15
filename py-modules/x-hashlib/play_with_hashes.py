import string
import random
import  hashlib
# initializing size of string
N = 32
 
# using random.choices()
# generating random strings
random_hash_like = ''.join(random.choices(string.hexdigits.lower(),k=N))

index = 0
while random_hash_like != hashlib.md5(random_hash_like.encode('utf-8')).hexdigest():
    the_hash_of_random_hash_like = hashlib.md5(random_hash_like.encode('utf-8')).hexdigest()
    print(index,random_hash_like, the_hash_of_random_hash_like,sep=" -> ")
    random_hash_like = ''.join(random.choices(string.hexdigits.lower(),k=N))
    index += 1

