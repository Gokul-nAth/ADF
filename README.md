      1.Program to read a file and store the unique words in a list sorted based on the length of word in a new file along with each word length appended to it.
   Open the input file in read mode and output file in append mode.Extract and append words from file to list.Iterate through the list,then find the count of each word using list.count(string) method.When the count is 1,append the length of the word in list (a).Concatenate the length to the word and append to the list (b).Sort the list (a).Append the words to output file based on the values in list (a).
   
      2.Program to read a CSV (CSV with n number of columns) and store it in DICT of list.
   Open the given csv file in read mode.Extract each row using csv.DictReader() method and append the extracted dictionary to the resultant list.
   
      3.Program to Print all Prime Numbers in an Interval of 5 seconds.
   Get an integer(n) to set limit for prime numbers.Declare a boolean list with True values of size n.True represents the position as prime number,which means initially all numbers are considered as prime number.Interate(i) the list,starting from 2.If boolean[i] and i^2 is less than n,initiate the inner for loop to set value False for all the multiples of i,starting from i^2 to n.Print the position of boolean array whose value is True in the interval for 5 seconds using time.sleep() method.
      
      4.Program to Find HCF or GCD
   Collect both numbers as user input.Find out the minimum number among them.Starting from the smallest(i),iterate the value and check the divisibility status of both inputs until (i) reaches 0.When a number divides both input numbers,consider that as a GCD of given two numbers. 
      
      5.Program to Convert Decimal to Binary, Octal and Hexadecimal
   Get an integer(n) as input.Create three separate methods for calculating binary,octal and hexa decimal values for the number.
   
   Binary:  
            Declare a resultant string with no value(bin).Append the resultant string(bin) to the string value of n%2 and divide n by 2,until n=0.Return the resultant string as binary value of that decimal number.
    
   Octal:  
            Declare a resultant string with no value(oct).Append the resultant string(oct) to the string value of n%8 and divide n by 8,until n=0.Return the resultant string as octal value of that decimal number.
            
   Hexa decimal:  
            Declare a resultant string with no value(hex).Append the resultant string(hex) to the string value of n%16 when (n%16) is lesser than 10,otherwise append the resultant string(hex) to the string value of (n%16)+55 and divide n by 16,until n=0.Return the resultant string as hexa decimal value of that decimal number.
            
       6.Program to Find ASCII Value of Character.
   Print the ASCII value of given character using ord() method,which return the equivalent integer value for a character.
   
      7.Program to get an application (name , age , gender, salary, state, city)
   Get the number of employees whose details are need to be added as input.Collect all the mentioned details as input.Create a class with constructor to add details and printDetails() method to show the given details as output.Create one object for each employee and store the values as instance variable.Call the printDetails() method with required object to get the details of a particular employee.
      
