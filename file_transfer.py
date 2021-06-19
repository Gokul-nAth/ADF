a=[]
b=[]
try:
    outputFile=open("to.txt","w")
    try:
        inputFile=open("from.txt","r").read().split(' ')
        for word in inputFile:
            ans=''
            for c in word:
                if(c!='\n'):
                    count=0
                    for v in word:
                        if(c==v):
                            count+=1
                    if(count==1):
                        ans=ans+c
            a.append(len(ans))
            ans=ans+str(len(ans))
            b.append(ans)
        a.sort()
        for w in a:
            for x in b:
                if(w==int(x[len(x)-1])):
                    outputFile.write(x+' ')
                    b.remove(x)
                    break
        print('File transfer executed successfully')
        outputFile.close()
    except IOError:
        print('Unable to open source file')
except IOError:
    print('Unable to open destination file')
