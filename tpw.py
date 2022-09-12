import hashlib
t1 = input("Bitte was eingeben: ")
#t1 = "2021"
s1 = "#T"
# encode it to bytes using UTF-8 encoding
message = t1.encode()
# hash with MD5 (not recommended)
print("WLAN-PW: ", hashlib.sha256(message).hexdigest()[0:18],s1,sep='')
