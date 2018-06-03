#==============================================================================
# THIS CODE IMPLEMENTS THE SEVENTEENTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#============================================================================
##START
##LIBRARIES
import numpy as np 
#==============================================================================
# CREATING THE NUMPY ARRAYS
# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])
'''THIS FUNCTION TO RETURN A STANDARDIZED VERSION OF THE GIVEN VALUES,
    WHICH WILL BE IN A NUMPY ARRAY. EACH VALUE SHOULD BE TRANSLATED INTO THE
    NUMBER OF STANDARD DEVIATIONS THAT VALUE IS AWAY FROM THE MEAN OF THE DATA.
    (A POSITIVE NUMBER INDICATES A VALUE HIGHER THAN THE MEAN, AND A NEGATIVE
    NUMBER INDICATES A VALUE LOWER THAN THE MEAN.)
    '''
standardize_data = lambda values: (values - values.mean())/values.std()
result = standardize_data(employment)
# PRINTING THE RESULT
for i in range(len(result)):
    print 'THE STANDARDIZED VERSION OF EMPLOYMENT IN THIS DATA FOR {} IS {}'.format(countries[i], result[i])