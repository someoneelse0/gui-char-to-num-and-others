#!/usr/bin/python3

import base64,codecs,hashlib,tkinter

t=tkinter.Tk()

st=tkinter.StringVar()
fn=tkinter.StringVar()

def ff(f,s):
    b=codecs.encode(s)
    o=open(f,"w")
    o.write("\n")
    o.write("Character, phrase or sentence: "+s+"\n\n")
    for i in s:
        o.write("Character to number: "+str(ord(i))+"\n")
    o.write("\n")
    for ii in s:    
        o.write("Number to hexadecimal: "+hex(ord(ii))[2:]+"\n")
    o.write("\n")
    for iii in s:
        o.write("Number to binary: "+bin(ord(iii))[2:]+"\n")
    o.write("\n")
    for iiii in s:
        o.write("Number to octal: "+oct(ord(iiii))[2:]+"\n")
    o.write("\n")
    b85=base64.b85encode(b)
    o.write("Character, phrase or sentence to b85: "+codecs.decode(b85)+"\n")
    b64=base64.b64encode(b)
    o.write("Character, phrase or sentence to b64: "+codecs.decode(b64)+"\n")
    b32=base64.b32encode(b)
    o.write("Character, phrase or sentence to b32: "+codecs.decode(b32)+"\n")
    b16=base64.b16encode(b)
    o.write("Character, phrase or sentence to b16: "+codecs.decode(b16)+"\n")
    a85=base64.b16encode(b)
    o.write("Character, phrase or sentence to a85: "+codecs.decode(a85)+"\n\n")
    md5=hashlib.md5(b).hexdigest()
    o.write("Character, phrase or sentence to md5: "+md5+"\n")
    sha1=hashlib.sha1(b).hexdigest()
    o.write("Character, phrase or sentence to sha1: "+sha1+"\n")
    sha224=hashlib.sha224(b).hexdigest()
    o.write("Character, phrase or sentence to sha224: "+sha224+"\n")
    sha256=hashlib.sha256(b).hexdigest()
    o.write("Character, phrase or sentence to sha256: "+sha256+"\n")
    sha512=hashlib.sha512().hexdigest()
    o.write("Character, phrase or sentence to sha512: "+sha512+"\n")
    sha3_224=hashlib.sha3_224().hexdigest()
    o.write("Character, phrase or sentence to sha3_224: "+sha3_224+"\n")
    sha3_256=hashlib.sha3_256().hexdigest()
    o.write("Character, phrase or sentence to sha3_256: "+sha3_256+"\n")
    sha3_512=hashlib.sha3_512(b).hexdigest()
    o.write("Character, phrase or sentence to sha3_512: "+sha3_512+"\n")
    blake2b=hashlib.blake2b(b).hexdigest()
    o.write("Character, phrase or sentence to blake2b: "+blake2b+"\n")
    blake2s=hashlib.blake2s(b).hexdigest()
    o.write("Character, phrase or sentence to blake2s: "+blake2s+"\n\n")
    o.close()

tl0=tkinter.Label(t,text="Introduce any character, phrase or sentence")
tl0.grid(row=0,column=0)

te0=tkinter.Entry(t,textvariable=st)
te0.grid(row=0,column=1)

tl1=tkinter.Label(t,text="Filename to write")
tl1.grid(row=1,column=0)

te1=tkinter.Entry(t,textvariable=fn)
te1.grid(row=1,column=1)

tb=tkinter.Button(t,text="Write file",command=lambda:ff(fn.get(),st.get()))
tb.grid(row=2,column=1,columnspan=2)

t.mainloop()
