print("\n---IF THE FILE EXIST THEN SHOWS--AS--BELOW:\n")
#Opening file named as File.txt
with open('File.txt','r') as f:
   t= f.read()
   print(t)
print("\n---IF THE FILE DOSEN'T EXIST THEN SHOWS---ERROR--AS--BELOW:\n")
#Opening file named as Exist.txt which is not exists at all.
with open('Exist.txt','r') as myFile:
    k= myFile.read()
    print(k)
   
