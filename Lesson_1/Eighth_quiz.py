##==============================================================================
## THIS CODE IMPLEMENTS THE EIGHTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
## AUTHOR : GUILHERME CARVALHO PEREIRA...NOT WORKING
## SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
##==============================================================================
###START
###LIBRARIES
#import unicodecsv
#from datetime import datetime as dt
##==============================================================================
## THIS FUCTIONS RETURNS THE UNIQUE DATA...CLEANING THE DATASET
#def unique (data):
#   unique_data = set()  ##SETS IN PYTHON ARE LIKE TUPLES, BUT EACH ELEMENT IS UNIQUE
#   for data in data:
#      unique_data.add(data['account_key'])##ONLY THE UNIQUE ELEMENTS WILL BE ADD
#   return unique_data
## THIS FUCTION CONVERTS STRINGS TO A DATETIME OBJECT
#def get_date(date):
#   if date == '':
#      return None
#   else:
#      return dt.strptime(date,'%Y-%m-%d')
## THIS FUCTON CONVERTS STRING TO INTEGERS
#def get_int(integer):
#   if integer == '':
#      return None
#   else:
#      return int(integer)
## FUNCTION TO READ THE FILES USING THE UNICODECSV + WITH STATEMENT
#def read (file_name):
#   with open(file_name, 'rb') as fl:##WITH ALLOWS TO OPEN AND CLOSE THE FILE AUTOMATICLY...MORE IN DOCS
#      read = unicodecsv.DictReader(fl)
#      return list(read)
## FUNCTION REMOVE THE UDACITY ACCOUNTS FROM THE DATASET
#def remove_test_student(data):
#   not_test_student = []
#   for data_point in data:
#      if data_point ['account_key'] not in test_student:
#         not_test_student.append(data_point)
#   return not_test_student
## FUCTIONS REMOVE FREE TRIAL STUDENTS
#def remove_free_trial_cancels(data, list_paid_students):
#    new_data = []
#    for data_point in data:
#        if data_point['account_key'] in list_paid_students:
#            new_data.append(data_point)
#    return new_data
## FUCTIONS CHECK IF THE DAYS ARE IN THE SAME WEEK
#def within_one_week(join_date, engagement_date):
#    time_delta = engagement_date - join_date
#    return time_delta.days >=0 and time_delta.days < 7
##=============================================================================
## READING THE FILES
#erol = read('enrollments.csv')
#daily_enga = read('daily_engagement.csv')
#proj_sub = read('project_submissions.csv')
## FIXING THE NAME OF DATASET DAILY_ENGAGEMENT.CSV
#for element in daily_enga:
#   element['account_key'] = element['acct']
#   del[element['acct']]
##THIS ARE UDACITY ACCOUNTS...WE GONNA REMOVE THEM...BUT FIRST WE GONNA SE HOW MANY
#test_student = set()
#not_test_erol = []
#not_test_daily_eng = []
#not_test_proj_sub = []
## CORRECTING THE TYPES OF THE VALUES
#for enrollment in erol:
#    if enrollment['is_udacity'] == 'False':
#        enrollment['cancel_date'] = get_date(enrollment['cancel_date'])
#        enrollment['days_to_cancel'] = get_int(enrollment['days_to_cancel'])
#        enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
#        enrollment['join_date'] = get_date(enrollment['join_date'])
#        not_test_erol.append(enrollment)
#    else:
#        test_student.add(enrollment['account_key'])
#        
#for engagement_record in daily_enga:
#    if engagement_record['account_key'] not in test_student:
#        engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
#        engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
#        engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
#        engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
#        engagement_record['utc_date'] = get_date(engagement_record['utc_date'])
#        not_test_daily_eng.append(engagement_record)
#
#for submission in proj_sub:
#    if submission['account_key'] not in test_student:
#        submission['completion_date'] = get_date(submission['completion_date'])
#        submission['creation_date'] = get_date(submission['creation_date'])
#        not_test_proj_sub.append(submission)
#
## EXPLORING THE DATE TO FIND HOW MANY STUDENTS ARE REALY TAKING THE COURSE
#paid_students = {}
#for erollament in not_test_erol:
#   if (not erollament['is_canceled'] or erollament['days_to_cancel'] > 7):## ELIMINETING THE FREE TRIAL STUDENTS..7 DAYS OF FREE TRIAL
#      account_key = erollament['account_key']
#      enrollment_date = enrollment['join_date']
#      if (account_key not in paid_students or enrollment_date > paid_students[account_key]):
#         paid_students[account_key] = enrollment_date
#print 'THE TOTAL NUMBER OF PAID STUNDES: {}'.format(len(paid_students))
#
#print 'THE NUMBER OF ENROLLMENTS WITH FREE TRIAL {}'.format(len(not_test_erol))
#print 'THE NUMBER OF ENGAGEMENTES WITH FREE TRIAL {}'.format(len(not_test_daily_eng))
#print 'THE NUMBER OF PROJECTS SUBMITIONS WITH FREE TRIAL {}'.format(len(not_test_proj_sub))
##REMOVING THE FREE TRIAL STUDENTS
#not_free_erol = remove_free_trial_cancels(not_test_erol, paid_students)
#paid_engagement = remove_free_trial_cancels(not_test_daily_eng, paid_students)
#not_free_proj_sub = remove_free_trial_cancels(not_test_proj_sub, paid_students)
##DATA FROM THE FIRST WEEK
#print 'THE NUMBER OF ENROLLMENTS WITHOUT FREE TRIAL {}'.format(len(not_free_erol))
#print 'THE NUMBER OF ENGAGEMENTES WITHOUT FREE TRIAL {}'.format(len(paid_engagement))
#print 'THE NUMBER OF PROJECTS SUBMITIONS WITHOUT FREE TRIAL {}'.format(len(not_free_proj_sub))
#
#paid_engagement_in_first_week = []
#for engagement_record in paid_engagement:
#    account_key = engagement_record['account_key']
#    join_date = paid_students[account_key]
#    engagement_record_date = engagement_record['utc_date']
#
#    if within_one_week(join_date, engagement_record_date):
#        paid_engagement_in_first_week.append(engagement_record)
#
#
#print("Engagement of paid students in first week: " + str(len(paid_engagement_in_first_week)))
##=============================================================================
#working code not mine
# Import libraries
import unicodecsv
import numpy as np
from collections import defaultdict
from datetime import datetime as dt


# Create functions

# Open csv files and convert to list
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

# Takes a date as a string, and returns a Python datetime object. 
# If there is no date given, returns None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
    
# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)
    
# Return a bool type that represent if the student's engagement is 
# in first week of program
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days >=0 and time_delta.days < 7

# Return new list without the trial students
def remove_free_trial_cancels(data, list_paid_students):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in list_paid_students:
            new_data.append(data_point)
    return new_data


# Set data in variables
enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')


# Rename column acct to account_key in enrollments list
for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]


list_students_udacity = set()
non_udacity_enrollments = []

# Clean up the data types in the enrollments table
for enrollment in enrollments:
    if enrollment['is_udacity'] == 'False':
        enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
        enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
        enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
        enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
        enrollment['join_date'] = parse_date(enrollment['join_date'])
        non_udacity_enrollments.append(enrollment)
    else:
        list_students_udacity.add(enrollment['account_key'])



non_udacity_engagement = []

# Clean up the data types in the engagement table
for engagement_record in daily_engagement:
    if engagement_record['account_key'] not in list_students_udacity:
        engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
        engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
        engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
        engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
        engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
        non_udacity_engagement.append(engagement_record)


non_udacity_submissions = []

# Clean up the data types in the submissions table
for submission in project_submissions:
    if submission['account_key'] not in list_students_udacity:
        submission['completion_date'] = parse_date(submission['completion_date'])
        submission['creation_date'] = parse_date(submission['creation_date'])
        non_udacity_submissions.append(submission)


paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or
            enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or
                enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date

print("Total of paid students: " + str(len(paid_students)))





print ("Paid students and trial students: " + str(len(non_udacity_enrollments)))
print ("Paid students and trial students: " + str(len(non_udacity_engagement)))
print ("Paid students and trial students: " + str(len(non_udacity_submissions)))

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments, paid_students)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement, paid_students)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions, paid_students)

print ("Only paid students: " + str(len(paid_enrollments)))
print ("Only paid students: " + str(len(paid_engagement)))
print ("Only paid students: " + str(len(paid_submissions)))




paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print("Engagement of paid students in first week: " + str(len(paid_engagement_in_first_week)))
# END OF THE CODE THAT IS NOT MINE
##=============================================================================
#ORGANAZING THE ENGAGEMENT RECORDS 
engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)
#CALCULATING THE TOTAL OS MINUTES OF EACH ACCOUNT
total_minutes_by_account = {}

for account_key, engagement_for_student in engagement_by_account.items():
   total_minutes = 0
   for engagement_record in engagement_for_student:
       total_minutes += engagement_record['total_minutes_visited']
   total_minutes_by_account [account_key] = total_minutes
#SUM ALL THE MINUTES SPEND   
total_minutes = total_minutes_by_account.values()
#PRINTING THE RESULTS
print 'TOTAL MINUTES SPEND IN AVERAGE IS {}'.format(np.mean(total_minutes))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(total_minutes))
print 'THE MAX OS MINUTES SPEND IS {}'.format(np.max(total_minutes))
print 'THE MIN OF MINUTES SPEND IS {}'.format(np.min(total_minutes))
    