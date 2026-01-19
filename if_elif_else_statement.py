#Grade Calculator
score1 = input("What score did you get? ")
score = int(score1)

#Grade System

if 100 >= score >= 90:
    print("You have achieved an A grade")

elif 89 >= score >= 80:
    print("You have achieved a B grade")

elif 79 >= score >= 70:
    print("You have achieved a C grade")

elif 69 >= score >= 60:
    print("You have achieved a D grade")

elif 60 >= score >= 0:
    print("You have achieved an F grade")

else:
    print("Invalid score entered")