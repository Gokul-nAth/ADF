import sys
import re
from collections import Counter

try:
    iFile=sys.argv[1]
    #iFile='day 2.txt'
    inputFileList=open(iFile,'r').read().split(' ')
    if(len(inputFileList)!=0):
        to=0
        ing=0
        palindrome=[]
        uniqueList=[]
        for word in inputFileList:
            if(word[:2]=='To' or word[:2]=='to'):
                to+=1
            if(word[-3:]=='ing'):
                ing+=1
            if(word.lower()==word[::-1].lower()):
                palindrome.append(word)

        print("Number of words whose prefix is To/to : ",to,'\n')
        print('Number of words whose suffix is "ing" : ',ing,'\n')
        dict=Counter(inputFileList)
        max=0
        for key in dict:
            if(dict[key]>max):
                max=dict[key]
        print('Word(s) with maximum number of occurance is : ',end=" ")
        fisrtWord=True
        for key in dict:
            uniqueList.append(key)
            if(fisrtWord and dict[key]==max):
                print(key,end="")
                fisrtWord=False
                continue
            if(dict[key]==max):
                print(','+key,end="")
        print('\n\nPalindrome word(s) : '+str(palindrome)[1:-1])
        print('\nUnique list : ',uniqueList)
        Word={}
        i=1
        for word in inputFileList:
            Word[i]=word
            i+=1
        print('\nDictionary : ',Word)
        file='file'
        for i in range(5):
            openFile=open(file+str(i+1)+'.txt','a')
            j=-1
            for word in inputFileList:
                j+=1
                if(i==0):
                    value=re.split('a|e|i|o|u',word)
                    for letter in value:
                        openFile.write(letter+' ')
                elif(i==1):
                    try:
                        openFile.write(word[:2]+word[2].upper()+word[3:])
                    except IndexError:
                        openFile.write(word)
                elif(i==2):
                    if(j==4):
                        openFile.write(word.upper()+' ')
                        continue
                    openFile.write(word)
                elif(i==3):
                    if(j==0):
                        openFile.write(word)
                        continue
                    else:
                        openFile.write('-'+word)
                        continue
                openFile.write(' ')
            openFile.close()
    else:
        print('The given file is empty')
except ValueError:
    print('Unable to open given file')