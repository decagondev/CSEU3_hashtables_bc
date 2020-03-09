import time
import hashlib
import bcrypt

n = 1
key = b"STR"

# hash
print("Hash")
start = time.time()
hash(key)
end = time.time()
print(end - start,"Seconds")

# hashlib
print("Hash Lib SHA256")
start = time.time()
hashlib.sha256(key)
end = time.time()
print(end - start,"Seconds")


# TODO: implement djb2

def djb2(key):
    # start from an arbitrary large prime such as (5381)
    # set the ahs value to 5381
    # iterate over each char in the key
        # set the hash value to the bit shift left by 5 of the hash value and sum of the hash value  then add the value for the char 
    # return the hash value



