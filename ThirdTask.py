from Crypto.Cipher import AES
import base64
import hashlib

msg_text = 'chiVBb5bMmiqhsm3Gpp6IFd/CalXMXKMrEMQJCl1u+0='
txt = 'This is a really hidden message.'


with open('words.txt','r') as f:
    for fline in f:
        secret_key = hashlib.sha256(fline.rstrip()).digest()
        enc = base64.b64decode(msg_text)
        IV="\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"
        cipher = AES.new(secret_key,AES.MODE_CBC,IV)
        decoded = cipher.decrypt(enc)
        #print decoded
        if decoded == txt:
            print ("The key is "+fline.rstrip())
            break


