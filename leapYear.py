#!c:\python\python.exe
import sys
import string

if len(sys.argv)<2:
    print "Usage:leap.py year,year,year..."
    sys.exit(0)

for i in sys.argv[1:]:
    try:
        y=string.atoi(i)

    except:
        print i,"Is not a year."
        continue

    leap="no"

    if y % 400 ==0:
        leap = "Yes"
    elif y %100 ==0:
        leap = "no"
    elif y % 4 == 0:
        leap = "yes"
    else:
        leap = "no"

    print y,"leap:", leap,"In the Gregorian calendar"

    if y % 4 ==0:
        leap = "yes"
    else :
        leap = "no"
    print y,"leap:",leap,"in the Julian calendar"

print "Calculated leapness for ",len (sys.argv)-1,"years"
