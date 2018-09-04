#Q1
import re
email=input('Enter Email Id :')
a=re.fullmatch('^[a-zA-Z][_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com)', email)
if a:
    print('\tVALID')
else:
    print('INVALID')




print('_______________________________')

#Q2
import re
x=input('Enter VALID Indian Phone number\t')
match=re.fullmatch('(\+91-)[6-9][0-9]{9}',x)
if match:
    print('VALID')
else:
    print('INVALID')
