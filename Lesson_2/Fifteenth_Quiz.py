#==============================================================================
# THIS CODE IMPLEMENTS THE FIFTEENTH QUIZ FROM INDTRODUCTION TO DATA ANALYSIS COURSE
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: INDTRODUCTION TO DATA ANALYSIS COURSE...UDACITY COURSE
#============================================================================
##START
##LIBRARIES
import numpy as np
#==============================================================================
# HIS FUNCTION TO RETURN THE NAME OF THE COUNTRY WITH THE HIGHEST EMPLOYMENT IN THE GIVEN EMPLOYMENT DATA, AND THE EMPLOYMENT IN THAT COUNTRY
def max_employment(countries, employment):
    data = employment.argmax()
    return (countries[data], employment[data])
#=============================================================================
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
# PRINTING THE RESULT
print 'THE COUNTRIE WITH THE HIGHEST EMPLOYMENT IN THIS DATA IS{}'.format(max_employment(countries,employment))