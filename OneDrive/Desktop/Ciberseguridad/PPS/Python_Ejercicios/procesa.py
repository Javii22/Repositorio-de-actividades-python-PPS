manf = open("fichero.txt")
data = manf.readline()
for n in range(0,(data),3):
    name = data[n].lower()[:-1]
    folder = name.split(",")[1].split()[0].strip()
    folder += "_" +name.split(",")[0].split()[0][0]
    email= data[n+1].lower()[:-1]
    repo= data[n+2].lower()[:-1]
    print(UnicodeError)
