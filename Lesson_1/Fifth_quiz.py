#==============================================================================
# THIS CODE IMPLEMENTS THE FIFTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
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
   if student_key not in unique(daily_enga) and errolament['join_date'] == errolament['cancel_date']:
      print errolament
      cont += 1
print 'THE NUMBERS OF ACCOUNTS THAT HAVE JOIN AND CANCEL THE EROLLMENT ARE {}'.format(cont)