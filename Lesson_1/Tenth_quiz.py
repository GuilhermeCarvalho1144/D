#==============================================================================
# THIS CODE IMPLEMENTS THE TENTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA...NOT WORKING
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#==============================================================================
##START
##LIBRARIES
import unicodecsv
import numpy as np
from collections import defaultdict
from datetime import datetime as dt
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

print("Engagement of paid students in first week: " + str(len(paid_engagement_in_first_week)))
##=============================================================================
#ORGANAZING THE ENGAGEMENT RECORDS 
engagement_by_account = group_date(paid_engagement_in_first_week, 'account_key')
#CALCULATING THE TOTAL OS MINUTES OF EACH ACCOUNT
total_minutes_by_account = sum_gruped_items(engagement_by_account, 'total_minutes_visited')
#SUM ALL THE MINUTES SPEND   
total_minutes = total_minutes_by_account.values()
#PRINTING THE RESULTS
print 'TOTAL MINUTES SPEND IN AVERAGE IS {}'.format(np.mean(total_minutes))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(total_minutes))
print 'THE MAX OF MINUTES SPEND IS {}'.format(np.max(total_minutes))
print 'THE MIN OF MINUTES SPEND IS {}'.format(np.min(total_minutes))

lessons_complete_by_account = sum_gruped_items(engagement_by_account, 'lessons_completed')

total_lessons = lessons_complete_by_account.values()
                                               
print 'TOTAL LESSONS MADE IN AVERAGE IS {}'.format(np.mean(total_lessons))
print 'THE STANDAR DEVIATION IS {}'.format(np.std(total_lessons))
print 'THE MAX OF LESSONS IS {}'.format(np.max(total_lessons))
print 'THE MIN OF LESSONS IS {}'.format(np.min(total_lessons))
