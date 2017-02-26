from Crypto.Cipher import AES
import base64

#given encrypted message
msg_text = 'y4TrHG1xZgvdRcnn2lU+el785PPKBRVgS7IvIa onruraSDs9rhsGQrgmbI9TM5pxhTWEaBrqxJMN vmwIHuP9WfR7O1QsokIZcyqVO/GSYyDIqM1Nil U5kBSsI7Tfg21ayxOo04h60fgAm5B+GxdgYiGj hw/LK04o9Hch6PvVowQ='
secret_key = 'VIRTUAL INSANITY' # given key

cipher = AES.new(secret_key,AES.MODE_ECB) # converting to cipher text with key
# cipher text is decoded and printed
decoded = cipher.decrypt(base64.b64decode(msg_text))
print decoded.strip()
