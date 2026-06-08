# Control Flow in Python refers to the order in which statements are executed in a program. 
# It is managed using conditional statements (if, elif, else), loops (for, while), 
# and loop control statements (break, continue, pass) to make decisions and repeat actions.

age =17
has_licence = True
if age >= 18:
    print("he/she is major")
else:
    print("minor!")

if age >=18:
    if has_licence:
        print("you have the eligiblity to drive!")
    else:
        print("wait for 18 yrs and get the licence for drive")

for i in range(1,10):
    print(i)

fruits = ["banan",'mango','apple','mango']
for i in fruits:
    print(i)

count =1
while count<=15:
    count +=1
    print(count)
    if count == 12:
        continue