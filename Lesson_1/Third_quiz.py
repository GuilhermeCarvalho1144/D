#==============================================================================
# THIS CODE IMPLEMENTS THE THIRD QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#==============================================================================
##START
##LIBRARIES
import unicodecsv
#==============================================================================
#THIS FUCTIONS RETURNS THE UNIQUE DATA...CLEANING THE DATASET
def unique (data,row_name):
   unique_data = set()  ##SETS IN PYTHON ARE LIKE TUPLES, BUT EACH ELEMENT IS UNIQUE
   for data in data:
      unique_data.add(data[row_name])##ONLY THE UNIQUE ELEMENTS WILL BE ADD
   return len(unique_data)
# FUNCTION TO READ THE FILES USING THE UNICODECSV + WITH STATEMENT
def read (file_name):
   with open(file_name, 'rb') as fl:##WITH ALLOWS TO OPEN AND CLOSE THE FILE AUTOMATICLY...MORE IN DOCS
      read = unicodecsv.DictReader(fl)
      return list(read)
#==============================================================================
# READING THE FILES
proj_sub = read('project_submissions.csv')
errol = read('enrollments.csv')
daily_enga = read('daily_engagement.csv')
# PRINTING THE RESULTS
print 'The file project_submissions.csv had {} lines before cleaning. After cleaning the file have {} lines'.format(len(proj_sub), unique(proj_sub,'account_key'))
print 'The file enrollments.csv had {} lines before cleaning. After cleaning the file have {} lines'.format(len(errol), unique(errol,'account_key'))
print 'The file daily_engagement.csv had {} lines before cleaning. After cleaning the file have {} lines'.format(len(daily_enga), unique(daily_enga,'acct'))