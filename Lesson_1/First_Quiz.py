#==============================================================================
# THIS CODE IMPLEMENTS THE FIRST QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#==============================================================================
##START
##LIBRARIES
import unicodecsv
#==============================================================================
# FUNCTION TO READ THE FILES USING THE UNICODECSV + WITH STATEMENT
def read (file_name):
   with open(file_name, 'rb') as fl:##WITH ALLOWS TO OPEN AND CLOSE THE FILE AUTOMATICLY...MORE IN DOCS
      read = unicodecsv.DictReader(fl)
      return list(read)
#==============================================================================
# READING THE FILES      
errol = read('enrollments.csv')
daily_enga = read('daily_engagement.csv')
proj_sub = read('project_submissions.csv')
# PRINTING THE RESULTS
print errol[0], daily_enga[0], proj_sub[0]