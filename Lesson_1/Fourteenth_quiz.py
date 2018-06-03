#==============================================================================
# THIS CODE IMPLEMENTS THE FOURTEENTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA...NOT WORKING
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#==============================================================================
##START
##LIBRARIES
import unicodecsv
import numpy as np
from collections import defaultdict
from datetime import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
#==============================================================================
# CREATE FUNCTIONS
# FUNCTION TO READ THE FILES USING THE UNICODECSV + WITH STATEMENT
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
    
# THIS FUNCTION CONVERTS STRINGS TO A DATETIME OBJECT
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')  
    
# THIS FUNCTION CONVERTS STRING TO INTEGER
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)    
    
# THIS FUNCTION CHECK IF THE DAYS ARE IN THE SAME WEEK
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days >=0 and time_delta.days < 7

# THIS FUNCTION REMOVE FREE TRIAL STUDENTS
def remove_free_trial_cancels(data, list_paid_students):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in list_paid_students:
            new_data.append(data_point)
    return new_data

#THIS FUNCTION GROUP THE DATA BY A KEY NAME
def group_date(data, key_name):
    grouped_date = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_date[key].append(data_point)
    return grouped_date

#THIS FUNCTION SUM A GROUPED DATA by a field name
def sum_gruped_items(grouped_data, field_name):
    summed_data = {} 
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
            summed_data [key] = total   
    return summed_data
            
#=============================================================================
# READING THE FILES
enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

# FIXING THE NAME OF DATASET DAILY_ENGAGEMENT.CSV
for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]
    
#THIS ARE UDACITY ACCOUNTS...WE GONNA REMOVE THEM...BUT FIRST WE GONNA SE HOW MANY
list_students_udacity = set()
non_udacity_enrollments = []
non_udacity_engagement = []
non_udacity_submissions = []

# CLEAN UP THE DATA TYPES IN THE ENROLLMENTS TABLE
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

# CLEAN UP THE DATA TYPES IN THE ENGAGEMENT TABLE
for engagement_record in daily_engagement:
    if engagement_record['account_key'] not in list_students_udacity:
        engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
        engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
        engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
        engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
        engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
        non_udacity_engagement.append(engagement_record)

# CLEAN UP THE DATA TYPES IN THE SUBMISSIONS TABLE
for submission in project_submissions:
    if submission['account_key'] not in list_students_udacity:
        submission['completion_date'] = parse_date(submission['completion_date'])
        submission['creation_date'] = parse_date(submission['creation_date'])
        non_udacity_submissions.append(submission)

# EXPLORING THE DATE TO FIND HOW MANY STUDENTS ARE REALY TAKING THE COURSE
paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or
            enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or
                enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date
            
# PRINTING THE TOTAL NUMBER OF STUNDETS THE ARE TAKING THE COURSE       
print("Total of paid students: " + str(len(paid_students)))

# PRINTING THE NUMBERS WITH FREE TRIAL STUDENTS
print ("Paid students and trial students: " + str(len(non_udacity_enrollments)))
print ("Paid students and trial students: " + str(len(non_udacity_engagement)))
print ("Paid students and trial students: " + str(len(non_udacity_submissions)))

# REMOVING THE FREE TRIAL STUDENTS
paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments, paid_students)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement, paid_students)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions, paid_students)

# PRINTING THE NUMBERS WITHOUT THE FRE TRIAL STUDENTS
print ("Only paid students: " + str(len(paid_enrollments)))
print ("Only paid students: " + str(len(paid_engagement)))
print ("Only paid students: " + str(len(paid_submissions)))

# SELECTING THE PAID STUDENTS IN THE FIRST WEEK
paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)
# THE NUMBER OF PAID STUDENTS IN THE FIRST WEEK
print("Engagement of paid students in first week: " + str(len(paid_engagement_in_first_week)))

# KEYS FOR THE SUBWAY PROJECT
subway_project_lesson_keys = ['746169184', '3176718735']

# GETING THE LESSONS KEY AND THE ASSIGNED TATING TO CHECK HOW PASSED IN THE SUBWAY PROJECT
pass_subway_project = set()
for submission in paid_submissions:
    project = submission['lesson_key']
    rating = submission['assigned_rating']
    if ((project in subway_project_lesson_keys) and (rating == 'PASSED' or rating == 'DISTINCTION')):
        pass_subway_project.add(submission['account_key'])
        
# MARKING THE ACCOUNTS THAT HAVE VISITED THE CLASS 
for engagement_record in paid_engagement:
    if engagement_record['num_courses_visited']>0:
        engagement_record['has_visited'] = 1
    else:
        engagement_record['has_visited'] = 0

# PRINTING THE NUMBER OF PERSONS HOW PASSED
print 'THE TOTAL NUMBER OF PERSON HOW PASSED IN THE SUBWAY PROJECT IS {}'.format(len(pass_subway_project))

# HOW MANY PERSONS PASS AT THE SUBWAY PROJECT IN THE FIRST WEEK
passing_engagement = []
non_passing_engagement = []
for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

# PRINTING THE NUMBER OF PERSONS HOW PASSED IN THE FIRST WEEK
print 'THE TOTAL NUMBER OF PERSON HOW  PASSED IN THE SUBWAY PROJECT IN THE FIRST WEEK IS {}'.format(len(passing_engagement))
print 'THE TOTAL NUMBER OF PERSON HOW DID NOT PASSED IN THE SUBWAY PROJECT IN THE FIRST WEEK IS {}'.format(len(non_passing_engagement))

# GROUPING THE DATA FOR PASSING AND NON PASSING STUDENTS BY ACCOUNT KEY
passing_engagement_by_account = group_date(passing_engagement,'account_key')
non_passing_engagement_by_account = group_date(non_passing_engagement, 'account_key')

# SUM ALL MINUTES SPEND FOR PASSING AND NON PASSING STUDENTS
passing_minutes = sum_gruped_items(passing_engagement_by_account, 'total_minutes_visited')
non_passing_minutes = sum_gruped_items(non_passing_engagement_by_account, 'total_minutes_visited')

# PLOT CONTROL
# DEFINE THE NUMBER OF BINS ON THE HIST
n = 100

# PRINTING THE RESULTS FOR PASSING STUDENTS
print 'DATA FOR THE PASSING STUDENTS...MINUTES SPEND'
print 'TOTAL OF MINUTES SPEND IN AVERAGE IS {}'.format(np.mean(passing_minutes.values()))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(passing_minutes.values()))
print 'THE MAX OF MINUTES SPEND IS {}'.format(np.max(passing_minutes.values()))
print 'THE MIN OF MINUTES SPEND IS {}'.format(np.min(passing_minutes.values()))
plt.hist(passing_minutes.values(), bins = n)
plt.title('MINUTES SPEND FOR THE PASSING STUDENTS IN THE FIRST WEEK')
plt.xlabel('MINUTES SPEND')
plt.show()

# PRINTING THE RESULTS FOR NON PASSING STUDENTS
print 'DATA FOR THE NON PASSING STUDENTS...MINUTES SPEND'
print 'TOTAL OF MINUTES SPEND IN AVERAGE IS {}'.format(np.mean(non_passing_minutes.values()))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(non_passing_minutes.values()))
print 'THE MAX OF MINUTES SPEND IS {}'.format(np.max(non_passing_minutes.values()))
print 'THE MIN OF MINUTES SPEND IS {}'.format(np.min(non_passing_minutes.values()))
plt.hist(non_passing_minutes.values(), bins = n)
plt.title('MINUTES SPEND FOR THE NON PASSING STUDENTS IN THE FIRST WEEK')
plt.xlabel('MINUTES SPEND')
plt.show()

# SUM ALL LESSONS COMPLETED FOR PASSING AND NON PASSING STUDENTS
passing_lessons = sum_gruped_items(passing_engagement_by_account, 'lessons_completed')
non_assing_lessons = sum_gruped_items(non_passing_engagement_by_account, 'lessons_completed')

# PRINTING THE RESULTS FOR PASSING STUDENTS
print 'DATA FOR THE PASSING STUDENTS...LESSONS COMPLETED'
print 'TOTAL OF LESSONS COMPLETED IN AVERAGE IS {}'.format(np.mean(passing_lessons.values()))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(passing_lessons.values()))
print 'THE MAX OF LESSONS COMPLETED IS {}'.format(np.max(passing_lessons.values()))
print 'THE MIN OF LESSONS COMPLETED IS {}'.format(np.min(passing_lessons.values()))
plt.hist(passing_lessons.values(), bins = n)
plt.title('LESSONS COMPLETED FOR THE PASSING STUDENTS IN THE FIRST WEEK')
plt.xlabel('LESSONS COMPLETED')
plt.show()

# PRINTING THE RESULTS FOR NON PASSING STUDENTS
print 'DATA FOR THE NON PASSING STUDENTS...LESSONS COMPLETED'
print 'TOTAL OF LESSONS COMPLETED IN AVERAGE IS {}'.format(np.mean(non_assing_lessons.values()))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(non_assing_lessons.values()))
print 'THE MAX OF LESSONS COMPLETED IS {}'.format(np.max(non_assing_lessons.values()))
print 'THE MIN OF LESSONS COMPLETED IS {}'.format(np.min(non_assing_lessons.values()))
plt.hist(non_assing_lessons.values(), bins = n)
plt.title('LESSONS COMPLETED FOR THE NON PASSING STUDENTS IN THE FIRST WEEK')
plt.xlabel('LESSONS COMPLETED')
plt.show()

# SUM ALL DAYS VISITED FOR PASSING AND NON PASSING STUDENTS
passing_visit = sum_gruped_items(passing_engagement_by_account, 'has_visited')
non_passing_visit = sum_gruped_items(non_passing_engagement_by_account, 'has_visited')

# PRINTING THE RESULTS FOR PASSING STUDENTS
print 'DATA FOR THE PASSING STUDENTS...DAYS VISITED'
print 'TOTAL OF DAYS VISITED IN AVERAGE IS {}'.format(np.mean(passing_visit.values()))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(passing_visit.values()))
print 'THE MAX OF DAYS VISITED IS {}'.format(np.max(passing_visit.values()))
print 'THE MIN OF DAYS VISITED IS {}'.format(np.min(passing_visit.values()))
plt.hist(passing_visit.values(), bins = n)
plt.title('DAYS VISITED FOR THE PASSING STUDENTS IN THE FIRST WEEK')
plt.xlabel('DAYS VISITED')
plt.show()

# PRINTING THE RESULTS FOR NON PASSING STUDENTS
print 'DATA FOR THE NON PASSING STUDENTS...DAYS VISITED'
print 'TOTAL OF DAYS VISITED IN AVERAGE IS {}'.format(np.mean(non_passing_visit.values()))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(non_passing_visit.values()))
print 'THE MAX OF DAYS VISITED IS {}'.format(np.max(non_passing_visit.values()))
print 'THE MIN OF DAYS VISITED IS {}'.format(np.min(non_passing_visit.values()))
plt.hist(non_passing_visit.values(), bins = n)
plt.title('DAYS VISITED FOR THE NON PASSING STUDENTS IN THE FIRST WEEK')
plt.xlabel('DAYS VISITED')
plt.show()