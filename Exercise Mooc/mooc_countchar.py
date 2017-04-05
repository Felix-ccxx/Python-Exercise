def countchar():
    astr=raw_input()
    rlist=[0 for x in range(26)]
    for x in astr:
        if x.isalpha():
            rlist[ord(x.lower())-97]=rlist[ord(x.lower())-97]+1
    else:
        print rlist
countchar()
