def swapdata():
    f1=input("Enter the first file name:")
    f2=input("Enter file to be swapped:")
    with open(f1,"r")as file1:
        data1=file1.read()
    with open(f2,"r")as file2:
        data2=file2.read()
    with open(f1,"w")as F1:
        F1.write(data2)
    with open(f2,"w")as F2:
        F2.write(data1)
swapdata()