import csv
file=input('Enter the file name : ')
try:
    inputCSV=open(file,'r')
    dict_list=[]
    for line in csv.DictReader(inputCSV):
        dict_list.append(line)
    print(dict_list)
except IOError:
    print('Unable to find or open '+file+' file')