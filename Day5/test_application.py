import application
import pytest
import unittest
class TestMethods(unittest.TestCase):
    def test_method1(self):
        key1 = application.App()
        key1.set_first_name('Vi')
        key1.set_middle_name('!')
        key1.set_last_name('C')
        key1.set_dob('1998-07-12')
        key1.set_gender('female')
        key1.set_nationality('Indian')
        key1.set_city('Dindigul')
        key1.set_state('Tamil Nadu')
        key1.set_pin(624802)
        key1.set_qualification('Bsc')
        key1.set_salary(22000)
        key1.set_pan('567GH123JK')
        assert key1.test_str=='Invalid first name'

    def test_method2(self):
        key1=application.App()
        key1.set_first_name('Aakash')
        key1.set_middle_name('!')
        key1.set_last_name('K')
        key1.set_dob('27-07-1995')
        key1.set_gender('male')
        key1.set_nationality('Indian')
        key1.set_city('Coimbatore')
        key1.set_state('Tamil Nadu')
        key1.set_pin(624892)
        key1.set_qualification('UG')
        key1.set_salary(29000)
        key1.set_pan('567GHU9OJK')
        assert key1.test_str=='Invalid DOB'

    def test_method3(self):
        key1=application.App()
        key1.set_first_name('Abinandhan')
        key1.set_middle_name('!')
        key1.set_last_name('B')
        key1.set_dob('2030-12-07')
        key1.set_gender('male')
        key1.set_nationality('Indian')
        key1.set_city('Coimbatore')
        key1.set_state('Tamil Nadu')
        key1.set_pin(623892)
        key1.set_qualification('UG')
        key1.set_salary(30000)
        key1.set_pan('907GHU9O8K')
        assert key1.test_str=='Invalid DOB'

    def test_method4(self):
        key1=application.App()
        key1.set_first_name('Aravindha')
        key1.set_middle_name('hariharan')
        key1.set_last_name('S')
        key1.set_dob('1995-12-07')
        key1.set_gender('male')
        key1.set_nationality('American')
        key1.set_city('Coimbatore')
        key1.set_state('Tamil Nadu')
        key1.set_pin(623802)
        key1.set_qualification('UG')
        key1.set_salary(42000)
        key1.set_pan('JD39IU8902')
        assert key1.test_str=='Not eligible to raise request today'

    def test_method5(self):
        key1=application.App()
        key1.set_first_name('Archana')
        key1.set_middle_name('!')
        key1.set_last_name('V')
        key1.set_dob('2000-06-29')
        key1.set_gender('femal')
        key1.set_nationality('American')
        key1.set_city('Salem')
        key1.set_state('Tamil Nadu')
        key1.set_pin(620092)
        key1.set_qualification('UG')
        key1.set_salary(38000)
        key1.set_pan('907GH67YH8')
        assert key1.test_str=='Invalid gender'

    def test_method6(self):
        key1=application.App()
        key1.set_first_name('Bala')
        key1.set_middle_name('ganesh')
        key1.set_last_name('R')
        key1.set_dob('1995-11-17')
        key1.set_gender('male')
        key1.set_nationality('Indian')
        key1.set_city('Coimbatore')
        key1.set_state('Tamil Nadu')
        key1.set_pin(62892)
        key1.set_qualification('UG')
        key1.set_salary(15000)
        key1.set_pan('8K0GHU668K')
        assert key1.test_str=='Invalid pin code'

    def test_method7(self):
        key1=application.App()
        key1.set_first_name('Chandru')
        key1.set_middle_name('!')
        key1.set_last_name('K')
        key1.set_dob('1999-10-19')
        key1.set_gender('Female')
        key1.set_nationality('Indian')
        key1.set_city('Coimbatore')
        key1.set_state('Tamil Nadu')
        key1.set_pin(612892)
        key1.set_qualification('UG')
        key1.set_salary(39000)
        key1.set_pan('AL04M93O8')
        assert key1.test_str=='Invalid PAN number'

    def test_method8(self):
        key1=application.App()
        key1.set_first_name('Guna')
        key1.set_middle_name('sethu')
        key1.set_last_name('G')
        key1.set_dob('1999-07-30')
        key1.set_gender('Male')
        key1.set_nationality('American')
        key1.set_city('Goida')
        key1.set_state('Assam')
        key1.set_pin(625892)
        key1.set_qualification('UG')
        key1.set_salary(25000)
        key1.set_pan('8K0G09KK8K')
        assert key1.test_str=='Age is not eligible'

    def test_method9(self):
        key1=application.App()
        key1.set_first_name('Manoj')
        key1.set_middle_name('kumar')
        key1.set_last_name('V')
        key1.set_dob('1997-09-10')
        key1.set_gender('Male')
        key1.set_nationality('Pakistan')
        key1.set_city('Simar')
        key1.set_state('Odisha')
        key1.set_pin(620194)
        key1.set_qualification('HSC')
        key1.set_salary(41000)
        key1.set_pan('8K0GHU90I8')
        assert key1.test_str=='Nationality is not eligible'

    def test_method10(self):
        key1=application.App()
        key1.set_first_name('Gopi')
        key1.set_middle_name('nath')
        key1.set_last_name('P')
        key1.set_dob('1995-08-19')
        key1.set_gender('Male')
        key1.set_nationality('Indian')
        key1.set_city('Sira')
        key1.set_state('Punjab')
        key1.set_pin(610914)
        key1.set_qualification('HSC')
        key1.set_salary(40000)
        key1.set_pan('B5U8P910I8')
        assert key1.test_str=='State is not eligible'

    def test_method11(self):
        key1=application.App()
        key1.set_first_name('Virat')
        key1.set_middle_name('kohli')
        key1.set_last_name('L')
        key1.set_dob('1992-11-21')
        key1.set_gender('Male')
        key1.set_nationality('Indian')
        key1.set_city('Kaba')
        key1.set_state('Madhya Pradesh')
        key1.set_pin(618904)
        key1.set_qualification('UG')
        key1.set_salary(9000)
        key1.set_pan('AS890134FV')
        assert key1.test_str=='Salary is not eligible'

    def test_method12(self):
        key1=application.App()
        key1.set_first_name('Aravindha')
        key1.set_middle_name('hariharan')
        key1.set_last_name('S')
        key1.set_dob('1995-12-07')
        key1.set_gender('male')
        key1.set_nationality('American')
        key1.set_city('Coimbatore')
        key1.set_state('Tamil Nadu')
        key1.set_pin(623802)
        key1.set_qualification('UG')
        key1.set_salary(42000)
        key1.set_pan('JD39IU8902')
        assert key1.test_str=='Eligible'

    def test_method13(self):
        key1=application.App()
        key1.set_first_name('Arun')
        key1.set_middle_name('ka')
        key1.set_last_name('S')
        key1.set_dob('1996-11-27')
        key1.set_gender('Male')
        key1.set_nationality('Indian')
        key1.set_city('Erode')
        key1.set_state('Tamil Nadu')
        key1.set_pin(609122)
        key1.set_qualification('UG')
        key1.set_salary(39050)
        key1.set_pan('JIO9034FG8')
        assert key1.test_str=='Invalid middle name'

    def test_method14(self):
        key1 = application.App()
        key1.set_first_name('Varun')
        key1.set_middle_name('!')
        key1.set_last_name('*')
        key1.set_dob('1998-08-12')
        key1.set_gender('Male')
        key1.set_nationality('Indian')
        key1.set_city('Kanyakumari')
        key1.set_state('Tamil Nadu')
        key1.set_pin(612781)
        key1.set_qualification('UG')
        key1.set_salary(41500)
        key1.set_pan('AS4K034FG8')
        assert key1.test_str == 'Invalid last name'


unittest.main