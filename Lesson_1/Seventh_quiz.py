#==============================================================================
# THIS CODE IMPLEMENTS THE SEVENTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#==============================================================================
##START
##LIBRARIES
import unicodecsv
from datetime import datetime as dt
#==============================================================================
# THIS FUCTIONS RETURNS THE UNIQUE DATA...CLEANING THE DATASET
def unique (data):
   unique_data = set()  ##SETS IN PYTHON ARE LIKE TUPLES, BUT EACH ELEMENT IS UNIQUE
   for data in data:
      unique_data.add(data['account_key'])##ONLY THE UNIQUE ELEMENTS WILL BE ADD
   return unique_data
# THIS FUCTION CONVERTS STRINGS TO A DATETIME OBJECT
def get_date(date):
   if date == '':
      return None
   else:
      return dt.strptime(date,'%Y-%m-%d')
# THIS FUCTON CONVERTS STRING TO INTEGERS
def get_int(integer):
   if integer == '':
      return None
   else:
      return int(integer)
# FUNCTION TO READ THE FILES USING THE UNICODECSV + WITH STATEMENT
def read (file_name):
   with open(file_name, 'rb') as fl:##WITH ALLOWS TO OPEN AND CLOSE THE FILE AUTOMATICLY...MORE IN DOCS
      read = unicodecsv.DictReader(fl)
      return list(read)
# FUNCTION REMOVE THE UDACITY ACCOUNTS FROM THE DATASET
def remove_test_student(data):
   not_test_student = []
   for data_point in data:
      if data_point ['account_key'] not in test_student:
         not_test_student.append(data_point)
   return not_test_student
#==============================================================================
# READING THE FILES
erol = read('enrollments.csv')
# CORRECTING THE TYPES OF THE VALUES
for enrollment in erol:
    enrollment['cancel_date'] = get_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = get_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = get_date(enrollment['join_date'])
#THIS ARE UDACITY ACCOUNTS...WE GONNA REMOVE THEM...BUT FIRST WE GONNA SE HOW MANY
test_student = set()
for erollament in erol:
   if erollament['is_udacity']:
      test_student.add(erollament['account_key'])
#WE GONNA REMOVE THEM      
not_test_erol = remove_test_student(erol)
# EXPLORING THE DATE TO FIND HOW MANY STUDENTS ARE REALY TAKING THE COURSE
paid_student = {}
for erollament in not_test_erol:
   if (not erollament['is_canceled'] or erollament['days_to_cancel'] > 7):## ELIMINETING THE FREE TRIAL STUDENTS..7 DAYS OF FREE TRIAL
      key = erollament['account_key']
      value = enrollment['join_date']
      if (key not in paid_student or value > paid_student[key]):
         paid_student[key] = value
print len(paid_student)
   
