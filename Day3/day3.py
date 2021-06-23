import logging
import sys
import re
from collections import Counter
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(message)s')

class ReadWriteFile:

    def __init__(self,fName):
        self.fileName=fName

    def openFileRM(self):
        try:
            inputList=open(self.fileName,'r').read().split(' ')
            logging.debug(f'{self.fileName} file opened')
            return inputList
        except FileNotFoundError:
            logging.debug('Unable to open {} file'.format(self.fileName))

    def openFileAM(self):
        try:
            outputList=open(self.fileName,'a')
            logging.debug(f'{self.fileName} file opened')
            return  outputList
        except FileNotFoundError:
            logging.debug('Unable to open {} file'.format(self.fileName))

    def closeFile(self,file):
        file.close()

    def printDetails(self):
        pass

class Test(ReadWriteFile):

    def __init__(self,file):
        super(Test, self).__init__(file)

    def printDetails(self,temp):
        print(temp)

    def to(self,l):
        count=0
        for word in l:
            if(word[:2]=='To' or word[:2]=='to'):
                count+=1
        self.printDetails(count)

    def ing(self,l):
        count = 0
        for word in l:
            if (word[-3:]=='ing'):
                count+=1
        self.printDetails(count)

    def findMax(self,l):
        dict = Counter(l)
        ansList=[]
        max = 0
        for key in dict:
            if (dict[key] > max):
                max = dict[key]
        for key in dict:
            if(dict[key]==max):
                ansList.append(key)
        self.printDetails(ansList)

    def palindrome(self,l):
        palindrome=[]
        for word in l:
            if (word.lower() == word[::-1].lower()):
                palindrome.append(word)
        self.printDetails(palindrome)

    def uniq(self,l):
        dict=Counter(l)
        uList=[]
        for key in dict:
            uList.append(key)
        self.printDetails(uList)

    def dict(self,l):
        Word = {}
        i = 1
        for word in l:
            Word[i] = word
            i += 1
        self.printDetails(Word)

    def vowelSplit(self,f,w):
        value = re.split('a|e|i|o|u', w)
        for letter in value:
            f.write(letter + ' ')

    def thirdLetter(self,f,w):
        try:
            f.write(w[:2] + w[2].upper() + w[3:])
        except IndexError:
            f.write(w)

file=sys.argv[1]
obj=Test(file)
inputList=obj.openFileRM()
if(len(inputList)!=0):
    print(f'Number of words whose prefix is To/to : ',end="")
    obj.to(inputList)
    logging.debug('Count of words whose preffix "To/to" is determined')
    print('Number of words whose suffix is "ing" : ',end="")
    obj.ing(inputList)
    logging.debug('Count of words whose suffix "ing" is determined')
    print('Word(s) with maximum occurance is/are : ',end="")
    obj.findMax(inputList)
    logging.debug('Word(s) with maximum occurance is/are determined')
    print('Palindrome word(s) : ',end="")
    obj.palindrome(inputList)
    logging.debug('Palindrome word(s) is/are determined')
    print('Unique list : ',end="")
    obj.uniq(inputList)
    logging.debug('Unique list is identified')
    print('Counter index : ', end="")
    obj.dict(inputList)
    logging.debug('Counter index dictionary is identified')

    file = 'file'
    for i in range(4):
        openFileObj=Test(file + str(i + 1) + '.txt')
        #openFile = open(file + str(i + 1) + '.txt', 'a')
        o=openFileObj.openFileAM()
        j = -1
        for word in inputList:
            j += 1
            if (i == 0):
                openFileObj.vowelSplit(o,word)
            elif (i == 1):
                openFileObj.thirdLetter(o,word)
            elif (i == 2):
                if (j == 4):
                    o.write(word.upper() + ' ')
                    continue
                o.write(word)
            elif (i == 3):
                if (j == 0):
                    o.write(word)
                    continue
                else:
                    o.write('-' + word)
                    continue
            o.write(' ')
        if(i==0):
            logging.debug('Writing splited words based on vowels in a new file is completed')
        elif(i==1):
            logging.debug('Converting the third letter of each word and write it in a new file is completed')
        elif(i==2):
            logging.debug('Converting the fourth word of file and write it in a new file is completed')
        elif(i==3):
            logging.debug('Converting the " " to "-" is done and write it in a new file is completed')
        openFileObj.closeFile(o)
        logging.debug('{} file closed'.format(file + str(i + 1) + '.txt'))
    logging.debug('All operations are done successfully\n')
else:
    print('The given file is empty')
    logging.debug(f'The file {file} is empty')