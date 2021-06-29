"""Application with eligibility"""
import sys
import datetime
import logging
import mysql.connector

logging.basicConfig(filename='appLog.log', level=logging.DEBUG, format='%(asctime)s:%(message)s')
content = open('mysql.config').read()
details = eval(content)  # pylint: disable=eval-used
mydb = mysql.connector.connect(
    host=details['host'],
    user=details['user'],
    password=details['password'],
    database=details['database']
)
mycursor = mydb.cursor()

# mycursor.execute('create table request_info (Req_id int auto_increment primary key,'
#                   'FirstName varchar(20),'
#                   'MiddleName varchar(20),LastName varchar(20),dob varchar(10),'
#                   'gender varchar(10),nationality varchar(15),'
#                   'city varchar(20),state varchar(20),pin int(6),qual varchar(20),'
#                   'salary int(15),pan varchar(10),Req_date varchar(10),age int(3))')
# mycursor.execute('create table `response_info` (Res_id int auto_increment primary key,'
#                   'Req_id int(100),'
#                   'Response varchar(10),reason varchar(100))')
class App:                 #pylint: disable=too-many-instance-attributes
    """Class to declare methods"""
    def __init__(self):
        self.first_name=None
        self.middle_name=None
        self.last_name=None
        self.dob=None
        self.gender=None
        self.nat=None
        self.city=None
        self.state=None
        self.pin=None
        self.qual=None
        self.salary=None
        self.pan=None
        self.age=None
        self.test_str='Eligible'

    def set_first_name(self,value):
        """Method to initiate first name"""
        self.first_name=value
        logging.debug("User's first name received")

    def set_middle_name(self,value):
        """Method to initiate middle name"""
        if value!='!':
            self.middle_name=value
            logging.debug("User's middle name received")
        else:
            self.middle_name=' '

    def set_last_name(self,value):
        """Method to initiate last name"""
        self.last_name=value
        logging.debug("User's first name received")

    def set_dob(self,value):
        """Method to initiate DOB"""
        self.dob=value
        logging.debug("User's DOB received")

    def set_gender(self,value):
        """Method to initiate gender"""
        self.gender=value
        logging.debug("User's gender received")

    def set_nationality(self,value):
        """Method to initiate nationality"""
        self.nat=value
        logging.debug("User's nationality received")
    def set_city(self,value):
        """Method to initiate city"""
        self.city=value
        logging.debug("User's city received")
    def set_state(self,value):
        """Method to initiate state"""
        self.state=value
        logging.debug("User's state received")

    def set_pin(self,value):
        """Method to initiate PIN code"""
        self.pin=value
        logging.debug("User's PIN code received")

    def set_qualification(self,value):
        """Method to initiate user's qualification"""
        self.qual=value
        logging.debug("User's qualification received")

    def set_salary(self,value):
        """Method to initiate salary"""
        self.salary=value
        logging.debug("User's salary received")

    def set_pan(self,value):
        """Method to initiate PAN number"""
        self.pan=value
        logging.debug("User's PAN number received")
        self.add_request()

    def add_request(self):
        """Method to add request to DB"""
        try:
            stmt="""insert into `request_info` (`FirstName`,`MiddleName`,`LastName`,
            `dob`,`gender`,`nationality`,`city`,
            `state`,`pin`,`qual`,`salary`,`pan`,
            `Req_date`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            val=(self.first_name,self.middle_name,self.last_name,self.dob,
                 self.gender,self.nat,self.city,self.state,
                 self.pin,self.qual,self.salary,self.pan,str(datetime.date.today()))

            mycursor.execute(stmt,val)
            mydb.commit()
            logging.debug("User's details are inserted to the DB")
            print('Request added successfully')
            self.validate_values()
        except SyntaxError:
            print('Error in mysql query')
            sys.exit()

    def validate_values(self):       #pylint: disable=too-many-statements
        """Method to validate input details"""
        stmt = """select `Req_id` from `request_info` where `pan`=%(pan_number)s"""
        mycursor.execute(stmt, {'pan_number': self.pan})
        rows = mycursor.fetchall()
        row = list(rows[len(rows) - 1])

        #row=[2]

        if len(self.first_name) < 3:
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',(row[0],
                            'Failed', 'Invalid first name'))
            mydb.commit()
            self.test_str='Invalid first name'
            logging.debug("Invalid firstname detected")
            return
        if self.middle_name!=' ' and len(self.middle_name)<3:
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',
                             (row[0], 'Failed', 'Invalid middle name'))
            mydb.commit()
            self.test_str = 'Invalid middle name'
            logging.debug("Invalid middlename detected")
            return
        if len(self.last_name) < 1 or self.last_name in ['@','#','*','!','%']:
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',
                             (row[0], 'Failed', 'Invalid last name'))
            mydb.commit()
            self.test_str = 'Invalid last name'
            logging.debug("Invalid lastname detected")
            return
        try:
            birth_date = datetime.datetime.strptime(self.dob, '%Y-%m-%d')
            logging.debug("Valid DOB detected")
            end_date = datetime.datetime.today()
            time_difference = end_date - birth_date
            self.age = int(int(time_difference.days) / 365)
            if self.age>-1 and self.age<101:
                mycursor.execute('update `request_info` set '
                                 '`age`=%(ageFound)s where `Req_id`=%(ri)s',
                                 {'ageFound':self.age,'ri':row[0]})
                logging.debug("User's age is calculated")
                mydb.commit()
            else:
                raise ValueError
        except ValueError:
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',
                             (row[0], 'Failed', 'Invalid input for DOB'))
            mydb.commit()
            self.test_str = 'Invalid DOB'
            logging.debug("Invalid DOB detected")
            return
        if not(self.gender.lower() == 'male' or
               self.gender.lower() == 'female' or
               self.gender.lower() == 'others'):
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',
                             (row[0], 'Failed', 'Given gender is invalid'))
            mydb.commit()
            self.test_str = 'Invalid gender'
            logging.debug("Invalid gender detected")
            return

        if not(len(str(self.pin)) == 6 and str(self.pin).isdigit()):
            mycursor.execute('insert into `response_info` (`Req_id`,'
                             '`Response`,`reason`) values (%s,%s,%s)',
                             (row[0], 'Failed', 'Given PIN number is invalid'))
            mydb.commit()
            self.test_str = 'Invalid pin code'
            logging.debug("Invalid PIN code detected")
            return

        if not(len(str(self.pan)) == 10 and self.pan.isalnum()):
            mycursor.execute('insert into `response_info` (`Req_id`,'
                             '`Response`,`reason`) values (%s,%s,%s)',
                             (row[0], 'Failed', 'Given PAN ID is invalid'))
            mydb.commit()
            self.test_str = 'Invalid PAN number'
            logging.debug("Invalid PAN ID detected")
            return
        self.validate()

    def validate(self):
        """Method to check eligibility"""
        stmt="""select `age`,`gender`,`Req_date`,`nationality`,`state`,
                `salary`,`Req_id` from 
                `request_info` where `pan`=%(pan_number)s"""
        mycursor.execute(stmt,{'pan_number': self.pan})
        rows=mycursor.fetchall()

        #rows=[[22,'male','2021-06-28','Indian','Tamil nadu',30000,1],[self.age,self.gender,str(datetime.date.today()),self.nat,self.state,self.salary,2]]

        logging.debug("Values fetched from DB")
        row=list(rows[len(rows)-1])
        if not(((str(row[1]).lower()=='male' or str(row[1]).lower()=='others') and row[0]>21) or
               (str(row[1]).lower()=='female' and row[0]>18)):
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',
                             (row[6],'Failed','Age is less than expected.'))
            mydb.commit()
            logging.debug("Given age is out of range for eligibility")
            self.test_str = 'Age is not eligible'
            return
        if row[3]!='Indian' and row[3]!='American':
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',
                             (row[6],'Failed', 'Entered nationality is not eligible'))
            mydb.commit()
            logging.debug("Given nationality is not eligible")
            self.test_str = 'Nationality is not eligible'
            return
        if row[4]  not in ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
                           'Bihar',  'Chattisgarh',  'Karnataka',
                           'Madhya Pradesh',  'Odisha',
                           'Tamil Nadu',  'Telangana', 'West Bengal']:
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',
                             (row[6],'Failed', 'Entered state is not eligible'))
            mydb.commit()
            logging.debug("Given state is not eligible")
            self.test_str = 'State is not eligible'
            return
        if row[5]<10000 or row[5]>90000:
            mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                             '`reason`) values (%s,%s,%s)',
                             (row[6], 'Failed', 'Salary is not equal to expected value.'))
            mydb.commit()
            logging.debug("Provided salary is out of range for eligibility")
            self.test_str = 'Salary is not eligible'
            return
        j=1
        for each in rows:
            each=list(each)
            if j!=len(rows):
                prev_date=datetime.datetime.strptime(each[2],'%Y-%m-%d')
                cur_date=datetime.datetime.strptime(row[2],'%Y-%m-%d')
                if (cur_date-prev_date).days<6:
                    mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                                     '`reason`) values (%s,%s,%s)',
                                     (row[6], 'Failed', 'Recently request received '
                                                        'in last 5 days'))
                    mydb.commit()
                    logging.debug("Not eligible-recently request received in last 5 days")
                    self.test_str = 'Not eligible to raise request today'
                    return
            j+=1
        mycursor.execute('insert into `response_info` (`Req_id`,`Response`,'
                         '`reason`) values (%s,%s,%s)',
                         (row[6], 'Success', 'Eligible'))
        mydb.commit()
    def close_db(self):
        mycursor.close()
        logging.debug('Mysql cursor closed')
        mydb.close()
        logging.debug('Mysql connection closed')

# OBJ=App()
# OBJ.set_first_name(input('Enter the first name : '))
# OBJ.set_middle_name(input('Enter the middle name or press "!" to skip: '))
# OBJ.set_last_name(input('Enter the last name : '))
# OBJ.set_dob(input('Enter the DOB (YYYY-MM-DD) : '))
# OBJ.set_gender(input('Enter the gender (Male/Female/Others) : '))
# OBJ.set_nationality(input('Enter the Nationality :'))
# OBJ.set_city(input('Enter the current city : '))
# OBJ.set_state(input('Enter the state : '))
# try:
#     OBJ.set_pin(int(input('Enter the pincode : ')))
# except TypeError:
#     print('Enter a valid pincode')
#     sys.exit()
# OBJ.set_qualification(input('Enter the qualification : '))
# try:
#     OBJ.set_salary(int(input('Enter the salary (Eg:20000): ')))
# except TypeError:
#     print('Enter a valid salary')
#     sys.exit()
# OBJ.set_pan(input('Enter the PAN number : '))
#
# logging.debug('Eligible user')
# OBJ.close_db()
