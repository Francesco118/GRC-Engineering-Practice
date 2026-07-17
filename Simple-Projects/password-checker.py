#Plan
#1. Get password input from user

#2. store the password in a variable

#3. Check the requirements of the password
## 3.1 Check if the password length is at least 8 characters
## 3.2 Check if the password contains at least one uppercase letter
## 3.3 Check if the password contains at least one lowercase letter
## 3.4 Check if the password contains at least one digit
## 3.5 Check if the password contains at least one special character

#4. If the password meets all the requirements, print "Password is valid"
##4.1 Grade each requirement as good, better, best, and an overall note - and print the grade for each requirement and the overall note

#5. If the password does not meet the requirements, print "Password is invalid" and
#5.1 specify which requirements were not met

#start loop and stop when all requirements are checked and satisfied

#Variables
Password = input("Enter your password: ")
upperCase_count = 0

#Requirements
##3.1 lenght
if len(Password) >= 16:
    print("Lenght is quality: Best") 
elif len(Password) >= 12:
    print("Lenght is quality: Better")
elif len(Password) >= 8:
    print("Lenght is quality: Good")
else:
    print("Lenght is quality: Failed")

#3.2 Uppercase letter
if any(char.isupper() for char in Password):
    upperCase_count += 1

if upperCase_count == 0:
    print("Uppercase Quality: Failed")
elif upperCase_count == 1:
    print("Uppercase Quality: Good")
elif upperCase_count >= 2 and upperCase_count <= 4:
    print("Uppercase Quality: Better")
elif upperCase_count >= 5:
    print("Uppercase Quality: Best")
else:
    print("Password does not contain uppercase letters: Failed")

#Print result (testing)
#print("this is your password:", Password)