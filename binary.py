l=[1,2,3,4,5]
with open("myfile.bin","wb") as f:
    for item in l:
        s=str(item)+"\n"
        bt=s.encode()
        f.write(bt)
    f.close()