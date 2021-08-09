from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
import time
import os


# get the PID
print "PID = " + str(os.getpid())
raw_input("continue...")
#-----------------------#

f_time = "%.20f" % time.time()

bs = Blowfish.block_size
key = b'mcsc2'
iv = Random.new().read(bs)
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

with open("encrypt_16MB.txt", "r") as f:
    plaintext = f.readlines()

plaintext = ''.join(plaintext)

plen = bs - divmod(len(plaintext),bs)[1]
padding = [plen]*plen
padding = pack('b'*plen, *padding)
#----------------------------

msg = iv + cipher.decrypt(plaintext + padding)

#----------------------------

l_time = "%.20f" % time.time()

done_time = float(l_time) - float(f_time)

f= open("DECRYPT.txt","w+")
f.write(msg)
f.close()

print "DEcrypt time : " + str(done_time)
raw_input("continue...")
