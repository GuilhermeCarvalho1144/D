#==============================================================================
# THIS CODE IMPLEMENTS THE SIXTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#==============================================================================
##START
##LIBRARIES
import unicodecsv
#==============================================================================
#THIS FUCTIONS RETURNS THE UNIQUE DATA...CLEANING THE DATASET
def unique (data):
   unique_data = set()  ##SETS IN PYTHON ARE LIKE TUPLES, BUT EACH ELEMENT IS UNIQUE
   for data in data:
      unique_data.add(data['account_key'])##ONLY THE UNIQUE ELEMENTS WILL BE ADD
   return unique_data
# FUNCTION TO READ THE FILES USING THE UNICODECSV + WITH STATEMENT
def read (file_name):
   with open(file_name, 'rb') as fl:##WITH ALLOWS TO OPEN AND CLOSE THE FILE AUTOMATICLY...MORE IN DOCS
      read = unicodecsv.DictReader(fl)
      return list(read)
## FUNCTION REMOVE THE UDACITY ACCOUNTS FROM THE DATASET
def remove_test_student(data):
   not_test_student = []
   for data_point in data:
      if data_point ['account_key'] not in test_student:
         not_test_student.append(data_point)
   return not_test_student
#==============================================================================
# READING THE FILES
proj_sub = read('project_submissions.csv')
erol = read('enrollments.csv')
daily_enga = read('daily_engagement.csv')
# FIXING THE NAME OF DATASET DAILY_ENGAGEMENT.CSV
for element in daily_enga:
   element['account_key'] = element['acct']
   del[element['acct']]
#INVESTIGATING WHY THE NUMBER OF UNIQUE VALUES IN THE DAILY_ENGAGEMENT.CSV AND THE ENROLLMENTS.CSV ARE NOT THE SAME
cont = 0
for errolament in erol:
   student_key = errolament['account_key']
   if student_key not in unique(daily_enga) and errolament['join_date'] != errolament['cancel_date']:
      #print errolament...#DEBUG 
      cont+=1
print 'THERE ARE MORE {} SURPRISING DATA POINTS'.format(cont)
#THIS ARE UDACITY ACCOUNTS...WE GONNA REMOVE THEM...BUT FIRST WE GONNA SE HOW MANY 
test_student = set()
for errolament in erol:
   if errolament['is_udacity'] == 'True':
      test_student.add(errolament['account_key'])  
print 'THERE ARE MORE {} TEST STUDENTS (UDACITY ACCOUNTS)'.format(len(test_student))
#REMOVING THE TEST STUDENTS
not_test_erol = remove_test_student(erol)
not_test_proj_sub = remove_test_student(proj_sub)
not_test_daily_eng = remove_test_student(daily_enga)
print 'THERE ARE MORE {} REAL STUDENTS ON THE daily_engagement.csv FILE'.format(len(not_test_daily_eng))
print'THERE ARE MORE {} REAL STUDENTS ON THE enrollments.csv FILE'.format(len(not_test_erol)) 
print 'THERE ARE MORE {} REAL STUDENTS ON THE project_submissions.csv FILE'.format(len(not_test_proj_sub))
print 'DATA IS CLEAN...YEAH!!!'
