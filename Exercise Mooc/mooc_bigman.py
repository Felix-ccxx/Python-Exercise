leaders={'xiaoyun':88888,'xiaohong':5555555,'xiaoteng':11111,'xiaoyi':1234321,'xiaoyang':1212121}
namerept = True
while namerept:
    name = raw_input("Please input the name:")
    if leaders.has_key(name)==True:
        print  "%s \'s QQ number is: %d" %(name,leaders[name])
        namerept=False
    else:
        print "You input name \'%s\' is not exit." %name
        namerept=True

print  ""
print  "Who has the nice QQ number?"
for lname in leaders.keys():
    if leaders[lname] <= 99999:
        print "%s has a nice QQ number: %d" %(lname,leaders[lname])
