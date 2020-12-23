import hashlib
import sys

def sub_hash(msg):
    h = ""
    m = hashlib.md5()
    m.update(msg)
    msg_md5 = m.digest()
    for i in range(8):
        n = (ord(msg_md5[2*i]) + ord(msg_md5[2*i+1])) % 0x3e
        if n > 9:
            if n > 35:
                n += 61
            else:
                n += 55
        else:
            n += 0x30
        h += chr(n)
    return h


if len(sys.argv) < 2:
 print 'Error: You did not enter a parameter !!!'
 print 'Use: python Encrypt_sub_3DD5E4.py Password'
 exit()

print '------------------------------------------'
print '| DevelopAKR       Encrypt_sub_3DD5E4    |'
print '------------------------------------------'
print 'Use: python Encrypt_sub_3DD5E4.py Password'
print '------------------------------------------'
print 'Hash(sub_3DD5E4): ', 
print sub_hash(sys.argv[1])
print '------------------------------------------'
