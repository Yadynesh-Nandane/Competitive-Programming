"""
Author: Yadynesh Nandane [Fresher]

Question asked in flair_labs technical interview.
Program for printing following pattern

********
*Hello,*
*there.*
*How   *
*do    *
*you   *
*do?   *
********

"""


strng = input()                                        # Accepting a string as input from user.
strng = strng.split(" ")
column = 0
row = (len(strng)+2)

for i in strng:                                        # Calculating Number of columns.
    if(column < len(i)):
        column = (len(i)+2)

for i in range(row):                                   # Loop for rows.
    if(i==0):
        for j in range(column):                        # Loop for printing initial line of "*".
            print("*",end="")
        print(end="\n")
    elif(i == (row-1)):
        for j in range(column):                        # Loop for printing last line of "*".
            print("*",end="")
    else:
        print("*",end="")
        count = 0                                      # Counter to maintain count of number of characters printed.
        for k in strng[(i-1)]:                         # Loop for printing characters of each word in the string.
            print(k,end="")
            count+=1
        if(count != (column-1)):
            for i in range(((column-2)-(count))):      # Loop for printing number of spaces after the words printed
                print(" ",end="")
        print("*",end="\n")
