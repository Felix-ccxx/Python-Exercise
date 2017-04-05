
song="Blowin\' in the wind\n"
singer="Bob Dylan\n"
inc="     1962 by Warner Bros.Inc\n"

sfile=open('Blowing in the wind.txt',mode='r+')
cont=sfile.readlines()
cont.insert(0,song)
cont.insert(1,singer)
cont.insert(len(cont)+1,inc)
sfile.seek(0,0)
sfile.writelines(cont)
print cont
print sfile
sfile.close()
