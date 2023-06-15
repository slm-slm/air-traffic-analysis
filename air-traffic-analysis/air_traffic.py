#In order for the program to work
#a file called 'input.txt' should be created
#which contains air traffic data

import os

#Exercise 1:
#How many flights are there to "Frankfurt"?
#-------------------------------------------
i=0
file = open('input.txt')
for line in file:
    if "Frankfurt" in line:
        i+=1
print(i)


#Exercise 2:
#Which flight has the most passengers?
#--------------------------------------
if os.path.getsize('input.txt') == 0:
    print("File is empty!")
else:
    file = open('input.txt')
    passengers=[]
    for line in file:
        [passengers.append(int(p)) for p in line.split() if p.isdigit()]
    file = open('input.txt')
    for line in file:
        if int(line.split()[2]) == max(passengers):
                print(line, end='')


#Exercise 3:
#Find the first flight with passengers less than 100.
#-----------------------------------------------------
flight=[]
if os.path.getsize('input.txt') == 0:
    print("There is no flight with passengers less than 100.")
else:
    file = open('input.txt')
    for line in file:
        if int(line.split()[2]) < 100:
                flight.append(line)
                break
    if flight:
        print(' '.join(map(str, flight)), end='')
    else:
        print("There is no flight with passengers less than 100")


#Exercise 4:
#Name the airline with the most total number of passengers.
#Print out the total number of passengers carried by the airline as well.
#-------------------------------------------------------------------------
if os.path.getsize('input.txt') == 0:
    print("File is empty!")
else:
    file = open('input.txt')
    totals={}
    for line in file:
        if line.split()[0] not in totals:
            totals[line.split()[0]] = 0
        totals[line.split()[0]] += int(line.split()[2])
    for key, value in totals.items():
        if value == max(totals.values()):
            print(key,value)

file.close()