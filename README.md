      1.Program to read a file and store the unique words in a list sorted based on the length of word in a new file along with each word length appended to it.
   Open the input file in read mode and output file in append mode.Extract and append words from file to list.Iterate through the list,then find the count of each word using list.count(string) method.When the count is 1,append the length of the word in list (a).Concatenate the length to the word and append to the list (b).Sort the list (a).Append the words to output file based on the values in list (a).
   
      2.Program to read a CSV (CSV with n number of columns) and store it in DICT of list.
   Open the given csv file in read mode.Extract each row using csv.DictReader() method and append the extracted dictionary to the resultant list.
   
      3.Program to Print all Prime Numbers in an Interval of 5 seconds.
   Get an integer(n) to set limit for prime numbers.Declare a boolean list with True values of size n.True represents the position as prime number,which means initially all numbers are considered as prime number.Interate(i) the list,starting from 2.If boolean[i] and i^2 is less than n,initiate the inner for loop to set value False for all the multiples of i,starting from i^2 to n.Print the position of boolean array whose value is True in the interval for 5 seconds using time.sleep() method.

      
