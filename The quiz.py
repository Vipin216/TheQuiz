# The quiz

print("Welcome to The Quiz")
print("The Quiz will be of 5 points")
#Defining functions and answer key
anskey=("TIGER","1945","MERCURY","URANUS","JUPITER")
def anscheck(a):
    a=a.upper()
    if a in anskey:
        print("Correct Answer!")
    else:
        print("Wrong Answer")

strt=input("Press any number to continue")

#Quiz

print("Q1:\nWhat is the National Animal of India?")
print("A.Lion         B.Tiger\nC.Elephant     D.Cow")
q1=input("Enter your answer")
anscheck(q1)

print("Q2:\nWhich year did WW2 end? ")
print("A.1945         B.1947\nC.1941          D.1939")
q2=input("Enter your answer")
anscheck(q2)

print("Q3:\nWhat is the closest planet to the Sun? ")
print("A.Earth      B.Venus\nC.Pluto          D.Mercury")
q3=input("Enter your answer")
anscheck(q3)

print("Q4:\nWhich is the coldest planet in the solar system? ")
print("A.Neptune      B.Uranus\nC.Saturn      D.Mars")
q4=input("Enter your answer")
anscheck(q4)

print("Q5:\nWhich is the Largest Planet in the Solar System ")
print("A.Earth      B.Jupiter\nC.Saturn       D.Venus")
q5=input("Enter your answer")
anscheck(q5)

#point counter
pt=0
q1=q1.upper()
q2=q2.upper()
q3=q3.upper()
q4=q4.upper()
q5=q5.upper()

if q1 in anskey:
    pt=pt+1
else:
    pt=pt

if q2 in anskey:
    pt=pt+1
else:
    pt=pt

if q3 in anskey:
    pt=pt+1
else:
    pt=pt

if q4 in anskey:
    pt=pt+1
else:
    pt=pt

if q5 in anskey:
    pt=pt+1
else:
    pt=pt

print("YOU GOT",pt,"/5")
if(pt==5):
    print("Congratulations!!!!")
elif(pt>3):
    print("Good Job!")
elif(pt>2):
    print("Good Try!")
else:
    print("Work Harder!")

