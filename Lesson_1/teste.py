# Import libraries
import unicodecsv
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
    return time_delta.days < 7

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

