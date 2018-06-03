#==============================================================================
# THIS CODE IMPLEMENTS THE EIGHTEENTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#============================================================================
##START
##LIBRARIES
import numpy as np 
#==============================================================================
# CREATING THE NUMPY ARRAYS
# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])
'''
    FILL IN THIS FUNCTION TO CALCULATE THE MEAN TIME SPENT IN THE CLASSROOM
    FOR STUDENTS WHO STAYED ENROLLED AT LEAST (GREATER THAN OR EQUAL TO) 7 DAYS.
    UNLIKE IN LESSON 1, YOU CAN ASSUME THAT DAYS_TO_CANCEL WILL CONTAIN ONLY
    INTEGERS (THERE ARE NO STUDENTS WHO HAVE NOT CANCELED YET).
    
    THE ARGUMENTS ARE NUMPY ARRAYS. TIME_SPENT CONTAINS THE AMOUNT OF TIME SPENT
    IN THE CLASSROOM FOR EACH STUDENT, AND DAYS_TO_CANCEL CONTAINS THE NUMBER
    OF DAYS UNTIL EACH STUDENT CANCEL. THE DATA IS GIVEN IN THE SAME ORDER
    IN BOTH ARRAYS.
    '''
mean_time_for_paid_students = lambda time_spent, days_to_cancel: time_spent[days_to_cancel >= 7].mean()
# PRINTING THE RESULT
print 'THE MEAN TIME SPENT IN THE CLASSROOM FOR STUDENTS WHO STAYED ENROLLED AT LEAST 7 DAYS IS {}'.format(mean_time_for_paid_students(time_spent, days_to_cancel))