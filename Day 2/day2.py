"""Example of pylint"""
import sys
import re
from collections import Counter


try:
    IFILE=sys.argv[1]
    #IFILE='day2.txt'
    iFileList=open(IFILE,'r').read().split(' ')
    inputFileList=[]
    for word in iFileList:
        if '.' in word:
            inputFileList.append(word[:word.index('.')])
            if word.index('.')+1<len(word):
                inputFileList.append(word[word.index('.')+1:])
        elif ',' in word:
            inputFileList.append(word[:word.index(',')])
            inputFileList.append(word[word.index(',') + 1:])
        elif '\n' in word:
            inputFileList.append(word[:word.index('\n')])
            inputFileList.append(word[word.index('\n')+1:])
        else:
            inputFileList.append(word)
    if len(inputFileList)!=0:
        TO=0
        ING=0
        palindrome=[]
        uniqueList=[]
        for word in inputFileList:
            if word[:2]=='To' or word[:2]=='to':
                TO+=1
            if word[-3:]=='ing':
                ING+=1
            if word.lower()==word[::-1].lower():
                palindrome.append(word)

        print('Number of words whose prefix is To/to : ',TO,'\n')
        print('Number of words whose suffix is "ing" : ',ING,'\n')

        dictC=Counter(inputFileList)
        MAXI=0
        maxList=[]
        for key in dictC:
            if dictC[key]>MAXI:
                MAXI=dictC[key]
        print('Word(s) with maximum number of occurance is : ',end=" ")
        for key in dictC:
            uniqueList.append(key)
            if dictC[key]==MAXI:
                maxList.append(key)
        print(maxList)
        print('\nPalindrome word(s) : ',palindrome)
        print('\nUnique list : ',uniqueList)
        Word={}
        i=1
        for word in inputFileList:
            Word[i]=word
            i+=1
        print('\nDictionary : ',Word)




        FILE='file'
        for i in range(5):
            with open(FILE+str(i+1)+'.txt','w') as openFile:
                j=-1
                if i == 4:
                    iFileList = open(IFILE, 'r').read().split(' ')
                    for w in iFileList:
                        if '\n' in w:
                            openFile.write(w[:w.index('\n')] + ';\n' + w[w.index('\n') + 1:] + ' ')
                            continue
                        openFile.write(w + ' ')
                for word in inputFileList:
                    j+=1
                    if i==0:
                        value=re.split('a|e|i|o|u',word)
                        for letter in value:
                            openFile.write(letter+' ')
                    elif i==1:
                        try:
                            openFile.write(word[:2]+word[2].upper()+word[3:])
                        except IndexError:
                            openFile.write(word)
                    elif i==2:
                        if j==4:
                            openFile.write(word.upper()+' ')
                            continue
                        openFile.write(word)
                    if i!=3:
                        openFile.write(' ')
                    if i==3:
                        if j==0:
                            openFile.write(word)
                        else:
                            openFile.write('-'+word)

    else:
        print('The given file is empty')
except ValueError:
    print('Unable to open given file')
except IndexError:
    print('No input')