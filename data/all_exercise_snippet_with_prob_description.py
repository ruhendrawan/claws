#CODE_SNIPPET
#exercise type: py
#exercise name: py_fail_course
# problem description: Construct a program to determine whether a student fails the course based on the inputs that it receives from the instructor. The student fails the course if the exam score is less than 55 or student has more than 2 missing homework.
#Step 1: Read the instructor inputs
text = input("Enter the exam score:")
exam_score = int(text)
text = input("Enter number of missing homework:")
number_of_missing_hw = int(text)
#Step 2: Write the boolean expression to determine whether the student fails the course
is_failing = exam_score < 55 or number_of_missing_hw > 2
#Step 3: Print the result
if is_failing == True :
    print("Yes! The student fails the course.")
else:
    print("No! The student does not fail the course.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_fail_course2
#Step 1: Read the instructor inputs
#problem description : Construct a program that determines whether a student fails the course based on the inputs that it receives from the instructor. The student fails the course if the exam score is less than 55 or when the student has cheated. Drag a tile to each missing field to construct this program.
text = input("Enter the exam score:")
exam_score = int(text)
text = input("Enter 1 if the student has cheated, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the student has cheated
if input_num == 1 :
    has_cheated = True
else:
    has_cheated = False
#Step 3: Write the boolean expression to determine whether the student fails the course
is_failing = exam_score < 55 or has_cheated
#Step 4: Print the result
if is_failing == True :
    print("Yes! The student fails the course.")
else:
    print("No! The student does not fail the course.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_fail_course3
#problem description: Construct a program that determines whether a student fails the course based on the inputs that it receives from the instructor. The student fails the course if his/her score is not above the class average. Drag a tile to each missing field to construct this program.
#Step 1: Read the instructor inputs
text = input("Enter the student's score:")
student_score = int(text)
text = input("Enter the class average:")
class_average = int(text)
#Step 2: Write the boolean expression to determine whether the student fails the course
is_failing = not ( student_score > class_average )
#Step 3: Print the result
if is_failing == True :
    print("Yes! The student fails the course.")
else:
    print("No! The student does not fail the course.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_phone_age
#Step 1: Read the user inputs
#problem description : Construct a program that determines whether it is time to buy a new phone based on the inputs that it receives from the user. A new phone should be bought if the phone breaks or the phone is at least 3 years old.
text = input("Enter the phone age in years:")
phone_age = int(text)
text = input("Enter 1 if the phone is broken, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the phone is broken
if input_num == 1 :
    is_broken = True
else:
    is_broken = False
#Step 3: Write the boolean expression to determine whether it is time to buy a new phone
need_phone = is_broken or phone_age >= 3
#Step 4: Print the result
if need_phone == True :
    print("Yes! It is time to buy a new phone.")
else:
    print("No! It is not yet the time to buy a new phone.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_phone_age2
#problem description : Construct a program that determines whether it is time to buy a new phone based on the inputs that it receives from the user. A new phone should be bought in either of the following cases: the phone break, the screen has a problem, the phone has the random shutdown problem
#Step 1: Read the user input for determining whether the phone is broken
text = input("Enter 1 if the phone is broken, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the phone is broken
if input_num == 1 :
    is_broken = True
else:
    is_broken = False
#Step 3: Read the user input for determining whether the phone screen is good
text = input("Enter 1 if the phone screen is good, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether the phone screen is good
if input_num == 1 :
    screen_is_good = True
else:
    screen_is_good = False
#Step 5: Read the user input for determining whether the phone has random shutdown problem
text = input("Enter 1 if the phone has the random shutdown problem, otherwise enter 0:")
input_num = int(text)
#Step 6: Determine whether the phone has random shutdown problem
if input_num == 1 :
    random_shutdown = True
else:
    random_shutdown = False
#Step 7: Write the boolean expression to determine whether it is time to buy a new phone
need_phone = is_broken or not screen_is_good or random_shutdown
#Step 8: Print the result
if need_phone == True :
    print("Yes! It is time to buy a new phone.")
else:
    print("No! It is not yet the time to buy a new phone.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_rent_car
# problem description : Construct a program that determines whether a customer could rent a car based on the inputs that it receives from the car rental agent. Rental cars are available to licensed drivers of 21 years of age or over.
#Step 1: Read the inputs from the car rental agent
text = input("Enter the customer's age:")
age = int(text)
text = input("Enter 1 if the customer has driver's license, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the customer has driver's license
if input_num == 1 :
    has_license = True
else:
    has_license = False
#Step 3: Write the boolean expression to determine whether a customer could rent a car
can_rent_car = age >= 21 and has_license
#Step 4: Print the result
if can_rent_car == True :
    print("Yes! The customer could rent a car.")
else:
    print("No! The customer could not rent a car.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_rent_car2
#problem description Construct a program that determines whether a customer could rent a car based on the inputs that it receives from the car rental agent. Rental cars are available to licensed drivers of 21 years of age or over who have not had a car accident.Construct a program that determines whether a customer could rent a car based on the inputs that it receives from the car rental agent. Rental cars are available to licensed drivers of 21 years of age or over who have not had a car accident.
#Step 1: Read the input for the customer's age
text = input("Enter the customer's age:")
age = int(text)
#Step 2: Read the input for determining whether the customer has driver's license
text = input("Enter 1 if the customer has driver's license, otherwise enter 0:")
input_num = int(text)
#Step 3: Determine whether the customer has driver's license
if input_num == 1 :
    has_license = True
else:
    has_license = False
#Step 4: Read the input for determining whether the customer has had an accident
text = input("Enter 1 if the customer has had an accident, otherwise enter 0:")
input_num = int(text)
#Step 5: Determine whether the customer has had an accident
if input_num == 1 :
    had_accidents = True
else:
    had_accidents = False
#Step 6: Write the boolean expression to determine whether a customer could rent a car
can_rent_car = age >= 21 and has_license and not had_accidents
#Step 7: Print the result
if can_rent_car == True :
    print("Yes! The customer could rent a car.")
else:
    print("No! The customer could not rent a car.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_rent_car3
# problem description: Construct a program that determines whether a customer could rent a car based on the inputs that it receives from the car rental agent. Rental cars are available to licensed drivers who are either at least 21 years old or have a credit card with $10,000 or more of credit.
#Step 1: Read the input for the customer's age
text = input("Enter the customer's age:")
age = int(text)
#Step 2: Read the input for determining whether the customer has driver's license
text = input("Enter 1 if the customer has driver's license, otherwise enter 0:")
input_num = int(text)
#Step 3: Determine whether the customer has driver's license
if input_num == 1 :
    has_license = True
else:
    has_license = False
#Step 4: Read the input for the customer's credit amount
text = input("Enter the customer's credit amount:")
credit = int(text)
#Step 5: Write the boolean expression to determine whether a customer could rent a car
can_rent_car = has_license and (age >= 21 or credit >= 10000)
#Step 6: Print the result
if can_rent_car == True :
    print("Yes! The customer could rent a car.")
else:
    print("No! The customer could not rent a car.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_check_age
#problem description : Construct a program that receives a string that has the user name and age separated by a colon, and prints whether the user is a teenager. Make sure that the program handles all possible exceptions.
#Step 1: Define the function
def check_age(s):
    #Step 1.1: Split the given string into the name and age
    lst = s.split(":")
    #Step 1.2: Enclose the code that might throw an exception within the try block
    try:
        name = lst[0]
        age = int(lst[1])
        if age >= 13 and age <= 19 :
            print(name + " is a teenager.")
        else:
            print(name + " is not a teenager.")
    #Step 1.3: Handle all possible exceptions that may be thrown in the try block
    except IndexError :
        print("Error! Separate the name and age by a colon.")
    except ValueError :
        print("Error! Age must be an integer.")
#Step 2: Call the function
check_age(input("Enter the name and age, separated by a colon:"))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_check_age2
#problem description : Construct a program that asks the user to enter a string that has the user name and age separated by a colon, and prints whether the user is a teenager. Make sure that the program handles all possible exceptions. The program must ask the user for an input until the user enters a string that could be processed without any exception.
#Step 1: Define the function
def check_age():
    #Step 1.1: Ask for a valid input as long as the input could not be processed; otherwise stop
    processed = False
    while not processed :
        s = input("Enter the name and age, separated by a colon:")
        #Step 1.1.1: Split the given string into the name and age
        lst = s.split(":")
        #Step 1.1.2: Enclose the code that might throw an exception within the try block
        try:
            name = lst[0]
            age = int(lst[1])
            if age >= 13 and age <= 19 :
                print(name + " is a teenager.")
            else:
                print(name + " is not a teenager.")
            processed = True
        #Step 1.1.3: Handle all possible exceptions that may be thrown in the try block
        except IndexError :
            print("Error! Separate the name and age by a colon.")
        except ValueError :
            print("Error! Age must be an integer.")
#Step 2: Call the function
check_age()


#CODE_SNIPPET
#exercise type: py
#exercise name: py_three_boolean
#problem description: Construct a program that determines whether at least one of the three boolean variables is True based on the inputs that it receives from the user.
#Step 1: Read the user input for the value of the first boolean variable (variable a)
text = input("Enter 1 if the value of the first boolean variable (variable a) is True, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the value of the first boolean variable (variable a) is True
if input_num == 1 :
    a = True
else:
    a = False
#Step 3: Read the user input for the value of the second boolean variable (variable b)
text = input("Enter 1 if the value of the second boolean variable (variable b) is True, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether the value of the second boolean variable (variable b) is True
if input_num == 1 :
    b = True
else:
    b = False
#Step 5: Read the user input for the value of the third boolean variable (variable c)
text = input("Enter 1 if the value of the third boolean variable (variable c) is True, otherwise enter 0:")
input_num = int(text)
#Step 6: Determine whether the value of the third boolean variable (variable c) is True
if input_num == 1 :
    c = True
else:
    c = False
#Step 7: Write the boolean expression to determine whether at least one of the three boolean variables is True
result = a or b or c
#Step 8: Print the result
if result == True :
    print("Yes! At least one of the three boolean variables is True.")
else:
    print("No! None of the boolean variables are True.")

#CODE_SNIPPET
#exercise type: py
#exercise name: py_three_boolean2
#problem description:  Construct a program that determines whether at least one of the three boolean variables is False based on the inputs that it receives from the user.
#Step 1: Read the user input for the value of the first boolean variable (variable a)
text = input("Enter 1 if the value of the first boolean variable (variable a) is True, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the value of the first boolean variable (variable a) is True
if input_num == 1 :
    a = True
else:
    a = False
#Step 3: Read the user input for the value of the second boolean variable (variable b)
text = input("Enter 1 if the value of the second boolean variable (variable b) is True, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether the value of the second boolean variable (variable b) is True
if input_num == 1 :
    b = True
else:
    b = False
#Step 5: Read the user input for the value of the third boolean variable (variable c)
text = input("Enter 1 if the value of the third boolean variable (variable c) is True, otherwise enter 0:")
input_num = int(text)
#Step 6: Determine whether the value of the third boolean variable (variable c) is True
if input_num == 1 :
    c = True
else:
    c = False
#Step 7: Write the boolean expression to determine whether at least one of the three boolean variables is False
result = not (a and b and c)
#Step 8: Print the result
if result == True :
    print("Yes! At least one of the three boolean variables is False.")
else:
    print("No! None of the boolean variables are False.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_three_boolean3
#problem description : Construct a program that receives the value of three boolean variables from the user and determines whether all variables have the same value, either all three True or all three False.
#Step 1: Read the user input for the value of the first boolean variable (variable a)
text = input("Enter 1 if the value of the first boolean variable (variable a) is True, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the value of the first boolean variable (variable a) is True
if input_num == 1 :
    a = True
else:
    a = False
#Step 3: Read the user input for the value of the second boolean variable (variable b)
text = input("Enter 1 if the value of the second boolean variable (variable b) is True, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether the value of the second boolean variable (variable b) is True
if input_num == 1 :
    b = True
else:
    b = False
#Step 5: Read the user input for the value of the third boolean variable (variable c)
text = input("Enter 1 if the value of the third boolean variable (variable c) is True, otherwise enter 0:")
input_num = int(text)
#Step 6: Determine whether the value of the third boolean variable (variable c) is True
if input_num == 1 :
    c = True
else:
    c = False
#Step 7: Write the boolean expression to determine whether all the three boolean variables have the same value
result = (a == b and b == c)
#Step 8: Print the result
if result == True :
    print("Yes! All the three boolean variables have the same value.")
else:
    print("No! Not all the variables have the same value.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_boolean_dry_hot
#problem description : Construct a program that determines whether it is both too hot and too dry based on the inputs that it receives from the user.
#Step 1: Read the user input for determining whether it is too hot
text = input("Enter 1 if it is too hot, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether it is too hot
if input_num == 1 :
    too_hot = True
else:
    too_hot = False
#Step 3: Read the user input for determining whether it is too dry
text = input("Enter 1 if it is too dry, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether it is too dry
if input_num == 1 :
    too_dry = True
else:
    too_dry = False
#Step 5: Write the boolean expression to determine whether it is both too hot and too dry
result = too_hot and too_dry
#Step 6: Print the result
if result == True :
    print("Yes! It is too hot and too dry.")
else:
    print("No! the weather condition 'too hot and too dry' is not met.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_boolean_dry_hot2
#problem description : Construct a program that determines whether it is either too hot or too dry (or both) based on the inputs that it receives from the user.
#Step 1: Read the user input for determining whether it is too hot
text = input("Enter 1 if it is too hot, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether it is too hot
if input_num == 1 :
    too_hot = True
else:
    too_hot = False
#Step 3: Read the user input for determining whether it is too dry
text = input("Enter 1 if it is too dry, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether it is too dry
if input_num == 1 :
    too_dry = True
else:
    too_dry = False
#Step 5: Write the boolean expression to determine whether it is either too hot or too dry (or both)
result = too_hot or too_dry
#Step 6: Print the result
if result == True :
    print("Yes! It is either too hot or too dry (or both).")
else:
    print("No! the weather condition 'too hot or too dry (or both)' is not met.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_boolean_dry_hot3
#problem description: Construct a program that determines whether it is too hot but not too dry based on the inputs that it receives from the user.
#Step 1: Read the user input for determining whether it is too hot
text = input("Enter 1 if it is too hot, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether it is too hot
if input_num == 1 :
    too_hot = True
else:
    too_hot = False
#Step 3: Read the user input for determining whether it is too dry
text = input("Enter 1 if it is too dry, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether it is too dry
if input_num == 1 :
    too_dry = True
else:
    too_dry = False
#Step 5: Write the boolean expression to determine whether it is too hot but not too dry
result = too_hot and not too_dry
#Step 6: Print the result
if result == True :
    print("Yes! It is too hot but not too dry.")
else:
    print("No! the weather condition 'too hot but not too dry' is not met.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_boolean_dry_hot4
#problem description: Construct a program that determines whether it is either too hot or too dry but not both based on the inputs that it receives from the user.
#Step 1: Read the user input for determining whether it is too hot
text = input("Enter 1 if it is too hot, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether it is too hot
if input_num == 1 :
    too_hot = True
else:
    too_hot = False
#Step 3: Read the user input for determining whether it is too dry
text = input("Enter 1 if it is too dry, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether it is too dry
if input_num == 1 :
    too_dry = True
else:
    too_dry = False
#Step 5: Write the boolean expression to determine whether it is either too hot or too dry but not both.
result1 = ( too_hot or too_dry ) and not ( too_hot and too_dry )
result2 = too_hot ^ too_dry
#Step 6: Print the result
if result1 == True :
    print("Yes! it is either too hot or too dry but not both.")
else:
    print("No! the weather condition 'too hot or too dry but not both' is not met.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_str_repeat_chars
#problem description: Construct a program that has a function that receives a string and creates a new string that has each character of the given string repeated two times. For example, the new string that will be formed from the string 'abc' is 'aabbcc'.
#Step 1: Define the function
def double_char(s):
    #Step 1.1: Assign initial value to the variable that we need for the new string
    new_s = ""
    #Step 1.2: Iterate through the characters in the given string
    for char in s:
        #Step 1.2.1: Add the repeated character to the the new string
        new_s += char * 2
    #String 1.3: Print the new string
    print(new_s)
#Step 2: Call the function
double_char("Hi There")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_str_repeat2
#problem description : Construct a program that has a function that receives a string and creates a new string that has every other character of the given string, starting with the first character, repeated two times. For example, the new string that will be formed from the string 'abcde' is 'aaccee'.
#Step 1: Define the function
def double_char(s):
    #Step 1.1: Assign initial value to the variable that we need for the new string
    new_s = ""
    #Step 1.2: Iterate through every other characters in the given string
    for i in range(0, len(s), 2) :
        #Step 1.2.1: Add the repeated character to the the new string
        new_s += s[i] * 2
    #String 1.3: Print the new string
    print(new_s)
#Step 2: Call the function
double_char("Hi There")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_file_input_stat
#problem description:  Construct a program that receives the full path to an input file from the user, reads that file and reports the number of lines, the longest line, the number of words on each line, and the length of the longest word on each line. Make sure that the program handles each specific exception that could occur.
#Step 1: Define the function
def get_stat(file_name):
    #Step 1.1: Assign initial value to variable that we need for reporting the file information
    num_lines = 0
    longest_line = ""
    #Step 1.2: Enclose the code that might throw an exception within the try block
    try :
        #Step 1.2.1: Open the file and process each line in the file
        myfile = open( file_name, "r")
        for line in myfile:
            num_lines += 1
            num_words = len(line.split())
            #Determine if the line is the longest line so far
            if (len(line) > len(longest_line)) :
                longest_line = line
            #Find the length of the longest word in the line
            longest_word = 0
            for w in line.split() :
                if len(w) > longest_word :
                    longest_word = len(w)
            #Print the line information
            print("Line " + str(num_lines) + " has " + str(num_words) + " tokens (longest = " + str(longest_word) + ")")
        print("Longest line:" + longest_line)
        #Step 1.2.2: Close the file
        myfile.close()
    #Step 1.3: Handle all possible exceptions that may be thrown in the try block
    except FileNotFoundError:
        print("File not found.")
    except IOError:


#CODE_SNIPPET
#exercise type: py
#exercise name: py_input_stat2
#problem description:  Construct a program that receives the full path to an input file from the user, reads that file and reports the number of lines, the longest line, the number of words on each line, and the length of the longest word on each line. Make sure that the program handles each specific exception that could occur. Also, the program must ask the user for a valid file path until the user enters a file path that could be accessed without any exception.
#Step 1: Define the function that gets the valid file path
def get_file():
    valid = False
    while not valid :
        try:
            file_name = input("Enter the full path of a file: ")
            myfile = open( file_name, "r")
            myfile.close()
            valid = True
        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Problem with the file!")
    return file_name
#Step 2: Define the function that processes the file
def get_stat(file_name):
    #Step 2.1: Assign initial value to variable that we need for reporting the file information
    num_lines = 0
    longest_line = ""
    #Step 2.2: Enclose the code that might throw an exception within the try block
    try :
        #Step 2.2.1: Open the file and process each line in the file
        myfile = open( file_name, "r")
        for line in myfile:
            num_lines += 1
            num_words = len(line.split())
            #Determine if the line is the longest line so far
            if (len(line) > len(longest_line)) :
                longest_line = line
            #Find the length of the longest word in the line
            longest_word = 0
            for w in line.split() :
                if len(w) > longest_word :
                    longest_word = len(w)
            #Print the line information
            print("Line " + str(num_lines) + " has " + str(num_words) + " tokens (longest = " + str(longest_word) + ")")
        print("Longest line:" + longest_line)
        #Step 2.2.2: Close the file
        myfile.close()
    #Step 2.3: Handle all possible exceptions that may be thrown in the try block
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Problem with the file!")
#Step 3: Call the functions
get_stat( get_file() )


#CODE_SNIPPET
#exercise type: py
#exercise name: py_student_score
#problem description : Assume we have a list of students and a list of their corresponding test scores. Construct a program that has a function which receives these two lists and returns a dictionary that maps each student to the scores of that student.For example, if the student list is ['Sam', 'Kim', 'Sam'] and the scores list is [15, 10, 14], the program creates the following dictionary:{'Sam': [15, 14], 'Kim': [10]}
#Step 1: Define the function
def create_dictionary(std_lst, test_lst):
    #Step 1.1: Create an empty dictionary
    res_dict={}
    #Step 1.2: Update the dictionary entries as we iterate through the indexes in the given lists
    for i in range(len(std_lst)):
        if std_lst[i]  in res_dict:
            res_dict[ std_lst[i] ].append( test_lst[i] )
        else:
            res_dict[ std_lst[i] ] = [ test_lst[i] ]
    return res_dict
#Step 2: Call the function
names = ['Joe', 'Tom', 'Barbara', 'Sue', 'Sally', 'Joe', 'Sue']
scores=[10, 23, 13, 18, 12, 9, 15]
print(create_dictionary(names, scores))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_score_dict2
#problem description : Assume we have a list of students and a list of their corresponding test scores. Construct a program that has two functions: - a function that receives these two lists and returns a dictionary that maps each student to the scores of that student, and  - a function that receives the dictionary created by the above function and calculates the average score of each student
#Step 1: Define the function that creates the dictionary
def create_dictionary(std_lst, test_lst):
    #Step 1.1: Create an empty dictionary
    res_dict={}
    #Step 1.2: Update the dictionary entries as we iterate through the indexes in the given lists
    for i in range(len(std_lst)):
        if std_lst[i]  in res_dict:
            res_dict[ std_lst[i] ].append( test_lst[i] )
        else:
            res_dict[ std_lst[i] ] = [ test_lst[i] ]
    return res_dict
#Step 2: Define the function that calculates the average of each student's scores
def average(new_dict):
    #Step 2.1: Iterate through the students in the dictionary
    for std_name in new_dict :
        #Step 2.1.1: Iterate through the list of student's scores, add each score to the running total
        total = 0;
        for score in new_dict[std_name]:
            total+= score
        #Step 2.1.2: Calculate and print the average of student's scores
        average = total/len(new_dict[std_name])
        print(std_name, average)
#Step 3: Call the functions
names = ['Joe', 'Tom', 'Barbara', 'Sue', 'Sally', 'Joe', 'Sue']
scores=[10, 23, 13, 18, 12, 9, 15]
average( create_dictionary(names, scores) )



#CODE_SNIPPET
#exercise type: py
#exercise name: bjects_classes_loan
#problem description: Construct a class that represents a loan. This class should contain data representing the interest rate, loan amount, and the length of loan period (in years); all of which could be accessed or changed only through the getter and setter methods. An instance of the class should be created by specifying annual interest rate, length of loan period, and loan amount. The other method of the this class should calculate the amount of monthly payments on the loan.
#Step 1: Define the class
class Loan1 :
    #Step 1.1: Initialize the loan with the specified values
    def __init__(self, annual_interest_rate, number_of_years, loan_amount) :
        self.__annual_interest_rate = annual_interest_rate
        self.__number_of_years = number_of_years
        self.__loan_amount = loan_amount
    #Step 1.2: Define the method that calculates the amount of monthly payments on the loan
    def get_monthly_payment(self) :
        monthly_interest_rate = self.__annual_interest_rate / 12
        monthly_payment = self.__loan_amount * monthly_interest_rate / (1 -
                (1 / (1 + monthly_interest_rate) ** (self.__number_of_years * 12) ))
        return monthly_payment
    #Step 1.3: Define the methods to get/set the properties of the loan
    def get_annual_interest_rate(self) :
        return self.__annual_interest_rate
    def set_annual_interest_rate(self, annual_interest_rate) :
        self.__annual_interest_rate = annual_interest_rate
    def get_number_of_years(self) :
        return self.__number_of_years
    def set_number_of_years(self, number_of_years) :
        self.__number_of_years = number_of_years
    def get_loan_amount(self) :
        return self.__loan_amount
    def set_loan_amount(self, loan_amount) :
        self.__loan_amount = loan_amount
#Step 2: Test the class
annual_interest_rate = float(input("Enter the annual interest rate: "))
number_of_years = int(input("Enter the number of years for the loan period: "))
loan_amount = (float(input("Enter the loan amount: ")))
loan1 = Loan1(annual_interest_rate, number_of_years, loan_amount)
print("The monthly payment for the loan is: {:.2f} ".format(loan1.get_monthly_payment()))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_loan2
# problem description: Construct a class that represents a loan. This class should contain data representing the interest rate, loan amount, and the length of loan period (in years); all of which could be accessed or changed only through the getter and setter methods. An instance of the class should be created by specifying annual interest rate, length of loan period, and loan amount.The other methods of the this class should calculate the amount of monthly payments on the loan as well as the total payment.
#Step 1: Define the class
class Loan2 :
    #Step 1.1: Initialize the loan with the specified values
    def __init__(self, annual_interest_rate, number_of_years, loan_amount) :
        self.__annual_interest_rate = annual_interest_rate
        self.__number_of_years = number_of_years
        self.__loan_amount = loan_amount
    #Step 1.2: Define the method that calculates the amount of monthly payments on the loan
    def get_monthly_payment(self) :
        monthly_interest_rate = self.__annual_interest_rate / 12
        monthly_payment = self.__loan_amount * monthly_interest_rate / (1 -
                (1 / (1 + monthly_interest_rate) ** (self.__number_of_years * 12) ))
        return monthly_payment
    #Step 1.3: Define the method that calculates the amount of total payments on the loan
    def get_total_payment(self) :
        total_payment = self.get_monthly_payment() * self.__number_of_years * 12
        return total_payment
    #Step 1.4: Define the methods to get/set the properties of the loan
    def get_annual_interest_rate(self) :
        return self.__annual_interest_rate
    def set_annual_interest_rate(self, annual_interest_rate) :
        self.__annual_interest_rate = annual_interest_rate
    def get_number_of_years(self) :
        return self.__number_of_years
    def set_number_of_years(self, number_of_years) :
        self.__number_of_years = number_of_years
    def get_loan_amount(self) :
        return self.__loan_amount
    def set_loan_amount(self, loan_amount) :
        self.__loan_amount = loan_amount
#Step 2: Test the class
annual_interest_rate = float(input("Enter the annual interest rate: "))
number_of_years = int(input("Enter the number of years for the loan period: "))
loan_amount = (float(input("Enter the loan amount: ")))
loan2 = Loan2(annual_interest_rate, number_of_years, loan_amount)
print("The monthly payment for the loan is: {:.2f} ".format(loan2.get_monthly_payment()))
print("The total payment for the loan is: {:.2f} ".format(loan2.get_total_payment()))



#CODE_SNIPPET
#exercise type: py
#exercise name: 
# problem description: Construct a class that represents a TV. The class should contain data that represents the TV's state (power on or off, current channel). The state of the TV could be accessed or changed only through the getter and setter methods. The class should also include methods to change the state of the TV (turn on/off, change channels). Assume that the valid channel range is from 1 to 120 (both inclusive).
#Step 1: Define the class
class TV1 :
    #Step 1.1: Initialize the state of the TV
    def __init__(self):
        self.__on = False
        self.__channel = 1
    #Step 1.2: Define the methods to change the on/off state of the TV
    def turn_on(self) :
        self.__on = True
    def turn_off(self) :
        self.__on = False
    #Step 1.3: Define the methods to change the channel of the TV
    def set_channel(self, new_channel) :
        if self.__on and new_channel >= 1 and new_channel <= 120 :
            self.__channel = new_channel
    def channel_up(self) :
        if self.__on and self.__channel < 120 :
            self.__channel += 1
    def channel_down(self) :
        if self.__on and self.__channel > 1 :
            self.__channel -= 1
    #Step 1.4: Define the methods to get the current state of the TV
    def get_channel(self) :
        return self.__channel
    def is_on(self) :
        return self.__on
#Step 2: Test the class
tv1 = TV1()
tv1.turn_on()
tv1.set_channel(30)
tv2 = TV1()
tv2.turn_on()
tv2.channel_up()
tv2.channel_up()
tv2.channel_down()
print("tv1's channel is " + str(tv1.get_channel()))
print("tv2's channel is " + str(tv2.get_channel()))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_tv2
#problem description: Construct a class that represents a TV. The class should contain data that represents the TV's state (power on or off, current volume level). The state of the TV could be accessed or changed only through the getter and setter methods. The class should also include methods to change the state of the TV (turn on/off, change volume level). Assume that the volume level is an integer and ranges from 1 to 7 (both inclusive).
#Step 1: Define the class
class TV2 :
    #Step 1.1: Initialize the state of the TV
    def __init__(self):
        self.__on = False
        self.__volume_level = 1
    #Step 1.2: Define the methods to change the on/off state of the TV
    def turn_on(self) :
        self.__on = True
    def turn_off(self) :
        self.__on = False
    #Step 1.3: Define the methods to change the volume level of the TV
    def set_volume(self, new_volume_level) :
        if self.__on and new_volume_level >= 1 and new_volume_level <= 7 :
            self.__volume_level = new_volume_level
    def volume_up(self) :
        if self.__on and self.__volume_level < 7 :
            self.__volume_level += 1
    def volume_down(self) :
        if self.__on and self.__volume_level > 1 :
            self.__volume_level -= 1
    #Step 4: Define the methods to get the current state of the TV
    def get_volume_level(self) :
        return self.__volume_level
    def is_on(self) :
        return self.__on
#Step 2: Test the class
tv1 = TV2()
tv1.turn_on()
tv1.set_volume(4)
tv1.set_volume(-1)
tv1.volume_down()
tv2 = TV2()
tv2.turn_on()
tv2.volume_up()
print("tv1's volume level is " + str(tv1.get_volume_level()))
print("tv2's volume level is " + str(tv2.get_volume_level()))



#CODE_SNIPPET
#exercise type: py
#exercise name: objects_classes_point
#problem description : Construct a class that represents a point in the Euclidean plane. The class should contain data that represents the point’s integer coordinates (x,y). The point's coordinates could be accessed or changed only through the getter and setter methods. The class should also include a method to translate the point, i.e., shift the point's location by the specified amount.
#Step 1: Define the class
class Point1 :
    #Step 1.1: Declare the method to shift the location of the point by the given amount
    def translate(self, dx, dy) :
        self.__x += dx
        self.__y += dy
    #Step 1.2: Define the setter and getter methods for the x-coordinate of the point
    def set_x(self, new_x) :
        self.__x = new_x
    def get_x(self) :
        return self.__x
    #Step 1.3: Define the setter and getter methods for the y-coordinate of the point
    def set_y(self, new_y) :
        self.__y = new_y
    def get_y(self) :
        return self.__y
#Step 2: Test the class
p1 = Point1()
p1.set_x(7)
p1.set_y(2)
p1.translate(11, 6)
print("p1 coordinates: (" + str(p1.get_x()) + ", " + str(p1.get_y()) + ")")



#CODE_SNIPPET
#exercise type: py
#exercise name: py_point2
#problem description: Construct a class that represents a point in the Euclidean plane. The class should contain data that represents the point’s integer coordinates (x,y). The point's coordinates could be accessed or changed only through the getter and setter methods. The class should also include a method to calculate and return the point's distance from the origin (0,0).
#Step 1: Define the class
class Point2 :
    #Step 1.1: Declare the method to calculate and return the point's distance from the origin
    def distance_from_origin(self) :
        return (self.__x * self.__x + self.__y * self.__y) ** 0.5
    #Step 1.2: Define the setter and getter methods for the x-coordinate of the point
    def set_x(self, new_x) :
        self.__x = new_x
    def get_x(self) :
        return self.__x
    #Step 1.3: Define the setter and getter methods for the y-coordinate of the point
    def set_y(self, new_y) :
        self.__y = new_y
    def get_y(self) :
        return self.__y
#Step 2: Test the class
p2 = Point2()
p2.set_x(7)
p2.set_y(2)
print("p2 coordinates: (" + str(p2.get_x()) + ", " + str(p2.get_y()) + ")")
print("Distance of p2 from origin = " + str(p2.distance_from_origin()))



#CODE_SNIPPET
#exercise type: py
#exercise name: objects_classes_account
#problem description : Construct a class that represents a basic bank account. This class should contain data representing the name of the account’s owner, the account number, and the account’s current balance; all of which could be accessed or changed only through the getter and setter methods. An instance of the class should be created by specifying three parameters that are used to initialize the instance (i.e., object) data. The other methods of this class should perform various services on the account (making deposits, withdrawals, adding interest to the account). These methods should examine the data passed into them to make sure the requested transaction is valid.
#Step 1: Define the class
class Account1 :
    #Step 1.1: Initialize the account with the specified values
    def __init__(self, owner, account, initial) :
        self.__acct_name = owner
        self.__acct_number = account
        self.__balance = initial
    #Step 1.2: Define a method to perform the deposit transaction
    def deposit(self, amount) :
        if (amount > 0) :
            self.__balance = self.__balance + amount
        return self.__balance
    #Step 1.3: Define a method to perform a withdraw transaction
    def withdraw(self, amount, fee) :
        if (amount > 0 and fee >= 0 and amount+fee < self.__balance) :
            self.__balance = self.__balance - amount - fee
        return self.__balance
    #Step 1.4: Define a method to add interest to the account
    def add_interest(self) :
        self.__balance += (self.__balance * 0.035)
        return self.__balance
    #Step 1.5: Define the methods to get the  state of the account
    def get_name(self) :
        return self.__acct_name
    def get_balance(self) :
        return self.__balance
    def get_acct_number(self) :
        return self.__acct_number
#Step 2: Test the class
acct1 = Account1("Tina Murphy", 72354, 25.59)
acct2 = Account1("Angelica Adams", 69713, 500.00)
acct3 = Account1("Edward Demsey", 93757, 769.32)
acct1.deposit(44.10)
adams_balance = acct2.deposit(75.25)
print("{:s}'s balance after deposit: {:.2f}".format(acct2.get_name(), adams_balance))
print("{:s}'s balance after deposit: {:.2f}".format(acct2.get_name(), acct2.withdraw (480, 1.50)))
acct3.withdraw(-100.00, 1.50)
acct2.add_interest()
print("{:s}'s balance after adding interest: {:.2f}".format(acct2.get_name(), acct2.get_balance()))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_account2
#problem description: Construct a class that represents a basic bank account. This class should contain data representing the name of the account’s owner, the account number, and the account’s current balance; all of which could be accessed or changed only through the getter and setter methods. An instance of the class should be created by specifying three parameters that are used to initialize the instance (i.e., object) data. The other methods of this class should: - provide a one-line description of the account, and - perform various services on the account (making deposits, withdrawals, adding interest to the account). These methods should examine the data passed into them to make sure the requested transaction is valid.
#Step 1: Define the class
class Account2 :
    #Step 1.1: Initialize the account with the specified values
    def __init__(self, owner, account, initial) :
        self.__acct_name = owner
        self.__acct_number = account
        self.__balance = initial
    #Step 1.2: Define a method to provide a one-line description of the account
    def __str__(self) :
        return "{:d}{:>20s}{:>10.2f}".format(self.__acct_number, self.__acct_name, self.__balance)
    #Step 1.3: Define a method to perform the deposit transaction
    def deposit(self, amount) :
        if (amount > 0) :
            self.__balance = self.__balance + amount
        return self.__balance
    #Step 1.4: Define a method to perform a withdraw transaction
    def withdraw(self, amount, fee) :
        if (amount > 0 and fee >= 0 and amount+fee < self.__balance) :
            self.__balance = self.__balance - amount - fee
        return self.__balance
    #Step 1.5: Define a method to add interest to the account
    def add_interest(self) :
        self.__balance += (self.__balance * 0.035)
        return self.__balance
    #Step 1.6: Define the methods to get the  state of the account
    def get_name(self) :
        return self.__acct_name
    def get_balance(self) :
        return self.__balance
    def get_acct_number(self) :
        return self.__acct_number
#Step 2: Test the class
acct1 = Account2("Tina Murphy", 72354, 25.59)
acct2 = Account2("Angelica Adams", 69713, 500.00)
acct3 = Account2("Edward Demsey", 93757, 769.32)
print(acct1)
print(acct2)
print(acct3)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_char_dict
#problem description: Construct a program that has a function which receives a string from the user and creates a dictionary that maps each character in the given string to its frequency, that is, how many times that character appears in the given string. For example, if the given string is "book", the program creates the following dictionary: b : 1, o : 2, k : 1
#Step 1: Define the function
def create_dictionary(s):
    #Step 1.1: Create an empty dictionary
    counts = {}
    #Step 1.2: Update the dictionary entries as we iterate through the string characters
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    #Step 1.3: Print the dictionary
    print("The character counts for", s)
    for char in counts:
        print(char, ":", counts[char])
#Step 2: Call the function
s = input("Enter a string: ")
create_dictionary(s)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_first_char_words_dict
#problem description: Construct a program that has a function which receives a string and creates a dictionary that maps each character to the list of distinct words in the given string that start with that character. The dictionary should be case insensitive. For example, if the given string is "This is my test score", the program creates the following dictionary: t : ['this', 'test'], i : ['is'], m : ['my'], s : ['score']
#Step 1: Define the function
def create_dictionary(s):
    #Step 1.1: Create an empty dictionary
    res_dict = {}
    #Step 1.2: Split the given string into words
    s = s.lower()
    words = s.split()
    #Step 1.3: Update the dictionary entries as we iterate through the words
    for word in words:
        if word[0] in res_dict:
            if word not in res_dict[ word[0] ] :
                res_dict[ word[0] ].append(word)
        else:
            res_dict[ word[0] ] = [ word ]
    #Step 1.4: Print the dictionary
    for char in res_dict:
        print(char, ":", res_dict[char])
#Step 2: Call the function
s = input("Enter a string: ")
create_dictionary(s)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_hello
print("Hello world!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_variables
a = 2
a = a + 3
print("The result is now", a)
a = 1 + a
print("The result is now", a)
a = 9
print("The result is now", a)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_simple_arithmetics
a = 5 + 2
b = a * 3
print("The result is:", b)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_arithmetics2
a = 2 + 3 * 9
b = a * (50 - a) / 2.5
print("The end result is", b)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_swap
first = 3
second = 8
temp = second
second = first
first = temp
print("The first is now", first, "and the second is", second)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_comparison
number1 = 45
number2 = 30
print("Number 1 is bigger than number 2:", number1 > number2)
print("Number 1 is smaller than number 2:", number1 < number2)
print("Number 1 is the same as number 2:", number1 == number2)
print("Number 1 is not the same as number 2:", number1 != number2)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_logic
account1 = 2540
account2 = 13250
price = 3400
can_afford = account1 >= price or account2 >= price
can_afford = account2 >= price or account1 >= price
account2 = account2 - price
money_left = account1 > 0 and account2 > 0
limit_exceeded = account1 < 0 and account2 < 0


#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_greet
name = input("What is your name?\n")
print("Hello,", name)
print("Nice to meet you!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_input1
first = int(input("Give an integer:\n"))
second = int(input("Give another integer:\n"))
print("Sum is:", first + second)
print("Product is:", first * second)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_input2
radius = float(input("Give the radius:\n"))
area = 3.14 * radius * radius
print("Area of the circle is:", area)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_hiscore1
score = 678
hi_score = 732
if score > hi_score:
    hi_score = score
    print("New High Score!")
print("Game over!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_hiscore2
score = 834
hi_score = 732
if score > hi_score:
    hi_score = score
    print("New High Score!")
print("Game over!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_ifelse
number = 53
if number % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")
print("That's it!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_ifelifelse
points = 63
if points > 70:
    grade = "A"
elif points > 65:
    grade = "B"
elif points > 60:
    grade = "C"
elif points > 55:
    grade = "D"
elif points > 50:
    grade = "E"
else:
    grade = "F"
print("Your grade is:", grade)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_nested_if
age = 17
hour = 14
if age >= 15:
    if hour < 13:
        print("The ticket costs $2")
    else:
        print("The ticket costs $4")
else:
    print("Free entrance!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_while
number = 2
while number < 15:
    print("Number is now", number)
    number = number * 2
print("Now it's too big. Time to end!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_for
for i in range(1, 6):
    print("2 *", i, "=", 2 * i)
print("Iteration ready!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_strings
start = "This is "
end = "my first sentence!"
sentence = start + end
print(sentence)
length = len(sentence)
print("It has", length, "characters.")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_lists1
my_list = [1, 5, 9]
my_list.append(6)
length = len(my_list)
first = my_list[0]
last = my_list[-1]
print("My list has", length, "items")
print("The first item is", first)
print("The last item is", last)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_lists2
my_list = [1, 4, 7]
for element in my_list:
    print(element)
print("These were the items in my list.")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_lists3
my_list = [1, 4, 7]
for element in my_list:
    print(element)
print("These were the items in my list.")
my_list = [7, 2, 3]
for i in range(len(my_list)):
    my_list[i] = my_list[i] * 2
print(my_list)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_format1
first = 4
second = 5
print("The values are {:d} and {:d}".format(first, second))



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_format2
pi = 3.141592653589793238
print("Pi is ca. {:.3f}".format(pi))



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_findmax
my_list = [2, 6, 14, 9]
biggest = my_list[0]
for value in my_list:
    if value > biggest:
        biggest = value
print("The biggest value is", biggest)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_functions1
def greet(name):
    print("Hello,", name)
    print("Nice to meet you!")
greet("John")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_returnvalue
def convert_to_euros(dollars):
  ratio = 0.8669
  return dollars * ratio
amount = float(input("Give the sum in dollars:\n"))
euros = convert_to_euros(amount)
print("It is {:.2f} euros.".format(euros))



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_functions2
def average(first, second):
    sum = first + second
    return sum / 2
result = average(2, 6)
print("The average is", result)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_functions3
def add_discount(sum, percentage):
    return sum * (1 - percentage)
def add_taxes(sum, percentage):
    return sum * (1 + percentage)
products = 23.5 + 12.2 + 4.75
total = add_taxes(add_discount(products, 0.05), 0.13)
print("The total sum is", total)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_recursion
def factorial(n):
    if n < 3:
        return n
    else:
        return factorial(n - 1) * n
print("Factorial of 4 is:", factorial(4))



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_dict1
def add_numbers(phonebook):
  phonebook["George"] = "555-4523"
  phonebook["Mike"] = "555-7412"
  phonebook["Lisa"] = "555-6398"
def main():
  numbers = {}
  add_numbers(numbers)
  count = len(numbers)
  print("Number count:", count)
  if "Mike" in numbers:
    print(numbers["Mike"])
  else:
    print("There is no number for Mike.")
  numbers["Mike"] = "555-6852"
  mike = numbers["Mike"]
  if "Marissa" in numbers:
    print(numbers["Marissa"])
  else:
    print("There is no number for Marissa.")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_dict2
def main():
  points = {}
  points["Mary"] = 5
  points["John"] = 10
  points["Mary"] = points["Mary"] + 15
  print("Mary's points:", points["Mary"])
  print("John's points:", points["John"])
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_dict3
def main():
  ages = {}
  ages["Mark"] = 7
  ages["Susan"] = 16
  ages["Bill"] = 36
  ages["Lisa"] = 22
  oldest = None
  max_age = None
  for person in ages:
    if oldest == None or ages[person] > max_age:
      oldest = person
      max_age = ages[person]
  print("The oldest is:", oldest)
  print("Years:", max_age)
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_objects1
car = Car(30)
car.fuel(20)
gallons = car.fuel(60)
print(gallons)
car.drive(10)
print(car.get_fuel())
another_car = Car(40)
another_car.fuel(10)


#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_objects2
class Car:
  def __init__(self, tank_size):
    self.tank_size = tank_size
    self.gas = 0
  def fuel(self, gallons):
    added = min(gallons, self.tank_size - self.gas)
    self.gas = self.gas + added
    return added
  def drive(self, consumption):
    if self.gas < consumption:
      return False
    self.gas = self.gas - consumption
    return True
  def get_fuel(self):
    return self.gas
  def has_more_fuel(self, another):
    return self.gas > another.gas
car = Car(30)
gallons = car.fuel(60)
print(gallons)
car.drive(10)
print(car.get_fuel())
another_car = Car(30)
print(car.has_more_fuel(another_car))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_concat_str_num
#problem description: Construct a program that uses variables x, y, and z to print "Python was invented in 1989.".
#Step 1: Assign initial values to the variables x, y, and z
x = "Python was invented in "
y = 1989
z = "."
#Step 2: Print the text using the variables initialized above
print(x + str(y) + z)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_concat_str_num2
#problem description: Construct a program that uses variables x, y, and z to print "x * 2 = 4".
#Step 1: Assign initial values to the variables x, y, and z
x = 2
y = "x * 2 = "
z = x * 2
#Step 2: Print the text using the variables initialized above
print(y + str(z))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_concat_string_num3
#problem description: Construct a program that uses variables x, y, and z to print "10 + 20 = 30".
#Step 1: Assign initial values to the variables x, y, and z
x = 10
y = 20
z = x + y
#Step 2: Print the text using the variables initialized above
print(str(x) + " + " + str(y) + " = " + str(z))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_time_conversion
#problem description: Construct a program that obtains minutes and remaining seconds from the input amount of time in seconds. For example, 500 seconds contains 8 minutes and 20 seconds.
#Step 1: Read the seconds
text = input("Enter an integer for seconds: ")
seconds = int(text)
#Step 2: Obtain minutes and remaining seconds from the input seconds
minutes = seconds // 60
remaining_seconds = seconds % 60
#Step 3: Display the result
print(seconds , "seconds is" , minutes , "minutes and" , remaining_seconds , "seconds.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_display_time2
#problem description: Construct a program that obtains hours, minutes, and seconds from an amount of time in milliseconds.
#Step 1: Read the milliseconds
text = input("Enter the milliseconds: ")
milliseconds = int(text)
#Step 2: Obtain hours, minutes, and seconds from the milliseconds
total_secs = milliseconds // 1000
hours = total_secs // 3600
mins = ( total_secs // 60 ) % 60
secs = total_secs % 60
#Step 3: Display the result
print(milliseconds, "milliseconds is", hours, "hours and" , mins , "minutes and" , secs , "seconds.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_bmi_calculator
#problem description: BMI is a measure of body fat based on height and weight that applies to adult men and women. BMI Categories are as follows:Underweight = <18.5, Normal weight = 18.5–24.9, Overweight = 25–29.9, Obesity = BMI of 30 or greater., English BMI Formula (Imperial) is: BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703., Construct a program that calculates the Body Mass Index (BMI) according to this formula.
#Step 1: Receive the weight and height from the user
text = input("Enter the weight in pounds:")
weight = float(text)
text = input("Enter the height in inches:")
height = float(text)
#Step 2: Calculate BMI
bmi = weight / height ** 2 * 703
#Step 3: Print the result
print("The BMI is:", bmi)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_bmi_calculator2
#problem description: BMI is a measure of body fat based on height and weight that applies to adult men and women. BMI Categories are as follows: Underweight = <18.5, Normal weight = 18.5–24.9, Overweight = 25–29.9, Obesity = BMI of 30 or greater., English BMI Formula (Imperial) is: BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703., BMI results are usually displayed as integers (values without decimal points). Construct a program to round the BMI result to the nearest integer.
#Step 1: Receive the weight and height from the user
text = input("Enter the weight in pounds:")
weight = float(text)
text = input("Enter the height in inches:")
height = float(text)
#Step 2: Calculate BMI
bmi = weight / height ** 2 * 703
#Step 3: Round up BMI
bmi = round(bmi)
#Step 4: Print results
print("The BMI rounded to the nearest integer is:", bmi)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_pythagorean_theorem
#problem description: Construct a program that accepts two input values from the user, one for each side of a right-angle triangle. The program uses the Pythagorean theorem (c^2 = a^2 + b^2) to calculate the length of the triangle's hypotenuse.
#Step 1: Receive the values for each side of a right-angle triangle
text = input("Enter the length of side A:")
side_A = float(text)
text = input("Enter the length of side B:")
side_B = float(text)
#Step 2: Calculate square of side A
squareside_A = side_A ** 2
#Step 3: Calculate square of side B
squareside_B = side_B ** 2
#Step 4: Use Pythagorean theorem to calculate the length of the triangle's hypotenuse
hypotenuse = ( squareside_A + squareside_B ) ** 0.5
#Step 5: Print the result
print("Given that side A is", side_A, "and side B is", side_B, ", the hypotenuse is", hypotenuse)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_pythagorean_theorem2
#problem description: Suppose that the user provides two input values for a right-angle triangle. The first input is for the length of an adjacent side in the triangle and the second input is for the hypotenuse of that triangle. The program calculates the second adjacent side of the triangle using these two input values. Use the Pythagorean theorem (c^2 = a^2 + b^2) to find the length of the second adjacent side.
#Step 1: Receive the values for the first side of a right-angle triangle and the hypotenuse
text = input("Enter the length of side A:")
side_A = float(text)
text = input("Enter the length of the hypotenuse:")
hypotenuse = float(text)
#Step 2: Calculate square of side A
square_side_A = side_A ** 2
#Step 3: Calculate square of hypotenuse
square_hypotenuse = hypotenuse ** 2
#Step 4: Use Pythagorean theorem to calculate the length of the triangle's other adjacent side
side_B = (square_hypotenuse - square_side_A) ** 0.5
#Step 5: Print the result
print("Given that side A is", side_A, "and the hypotenuse is", hypotenuse, ", side B is", side_B)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_f_to_c_conversion
#problem description: Construct a program that computes the Fahrenheit equivalent of an input Celsius value using the formula F = (9/5)C + 32. The input Celsius value is an integer.
#Step 1: Assign initial values to the variables which we need for this program
base = 32
conversion_factor = 9 / 5
#Step 2: Read the input Celsius value
text = input("Enter the Celsius value: ")
celsius_temp = int(text)
#Step 3: Compute the  Fahrenheit equivalent of the Celsius value
fahrenheit_temp = celsius_temp * conversion_factor + base
print("Celsius Temperature:" , celsius_temp)
print("Fahrenheit Equivalent:" , fahrenheit_temp)


#CODE_SNIPPET
#exercise type: py
#exercise name:  py_fahrenheit_to_celsius
#problem description: Construct a program that computes the Celsius equivalent of an input Fahrenheit value using the formula C = (F - 32) (5/9). The input Fahrenheit value is an integer.
#Step 1: Assign initial values to the variables which we need for this program
base = 32
conversion_factor = 5 / 9
#Step 2: Read the input Fahrenheit value
text = input("Enter the Fahrenheit value: ")
fahrenheit_temp = int(text)
#Step 3: Compute the Celsius equivalent of the Fahrenheit value
celsius_temp = (fahrenheit_temp - base) * conversion_factor
print("Fahrenheit Temperature:" , fahrenheit_temp)
print("Celsius Equivalent:" , celsius_temp)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_vending_machine
#problem description: Suppose we have a vending machine that gives change. A customer selects an item for purchase and inserts a bill into the vending machine. The vending machine dispenses the purchased item and gives change. We will assume that all item prices are multiples of 25 cents, and the machine gives all change in dollar and quarters. Construct a program that computes how many dollars and quarters to return to the customer.
#Step 1: Assign initial values to the variables which we need for this program
pennies_per_dollar = 100
pennies_per_quarter = 25
#Step 2: Read the bill value and item price
text = input("Enter bill value in dollars (1 = $1 bill, 5 = $5 bill, etc.): ")
bill_value = int(text)
text = input("Enter item price in pennies: ")
item_price = int(text)
#Step 3: Compute the change due
change_due = pennies_per_dollar * bill_value - item_price
#Step 4: Compute the number of dollars and update the change due after taking away the dollars
dollars = change_due // pennies_per_dollar
change_due = change_due % pennies_per_dollar
#Step 5: Compute the number of quarters in the remaining change due
quarters = change_due // pennies_per_quarter
#Step 6: Display the result
print("Your change consists of:")
print(dollars, "dollars")
print(quarters, "quarters")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_vending_machine2
#problem description: Suppose we have a vending machine that gives change. A customer selects an item for purchase and inserts a bill into the vending machine. The vending machine dispenses the purchased item and gives change. We will assume that all item prices are multiples of 5 cents, and the machine gives all change in quarters, dimes, and nickels. Construct a program that computes how many quarters, dimes, and nickels to return to the customer.
#Step 1: Assign initial values to the variables which we need for this program
pennies_per_dollar = 100
pennies_per_quarter = 25
pennies_per_dime = 10
pennies_per_nickel = 5
#Step 2: Read the bill value and item price
text = input("Enter bill value in dollars (1 = $1 bill, 5 = $5 bill, etc.): ")
bill_value = int(text)
text = input("Enter item price in pennies: ")
itemPrice = int(text)
#Step 3: Compute the change due
change_due = pennies_per_dollar * bill_value - itemPrice
#Step 4: Compute the number of quarters in the change due and update the change due after taking away the quarters
quarters = change_due // pennies_per_quarter
change_due = change_due % pennies_per_quarter
#Step 5: Compute the number of dimes in the remaining change due and update the change due after taking away the dimes
dimes = change_due // pennies_per_dime
change_due = change_due % pennies_per_dime
#Step 6: Compute the number of nickels in the remaining change due
nickels = change_due // pennies_per_nickel
#Step 7: Display the result
print("Your change consists of:")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_nested_if_min_max
#problem decsription: Construct a program that determines the smallest of the three integer values entered by the user.
#Step 1: Read the three integers
text = input("Enter the first integer: ")
num1 = int(text)
text = input("Enter the second integer: ")
num2 = int(text)
text = input("Enter the third integer: ")
num3 = int(text)
#Step 2: Determine the minimum integer
if num1 < num2 :
    if num1 < num3 :
        min_num = num1
    else :
        min_num = num3
else :
    if num2 < num3 :
        min_num = num2
    else :
        min_num = num3
#Step 3: Print the minimum integer
print("Minimum value:", min_num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_nested_if_max_of_three
#problem description: Construct a program that determines the largest of the three integer values entered by the user.
#Step 1: Read the three integers
text = input("Enter the first integer: ")
num1 = int(text)
text = input("Enter the second integer: ")
num2 = int(text)
text = input("Enter the third integer: ")
num3 = int(text)
#Step 2: Determine the maximum integer
if num1 > num2 :
    if num1 > num3 :
        max_num = num1
    else :
        max_num = num3
else :
    if num2 > num3 :
        max_num = num2
    else :
        max_num = num3
#Step 3: Print the maximum integer
print("Maximum value:", max_num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_nested_if_temperature
#problem description: Construct a program that receives the temperature for today and yesterday and warns the user when it is getting colder or warmer or neither. The temperature values could have a decimal point.
#Step 1: Read the temperature for today and yesterday
text = input("Enter the yesterday's temperature: ")
yesterday = float(text)
text = input("Enter the today's temperature: ")
today = float(text)
#Step 2: Warn the user about the changes in the temperature
if  today < yesterday :
    print("It is getting colder!")
else :
    if  today > yesterday :
        print("It is getting warmer!")
    else :
        print("Temperature is the same as yesterday!")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_nested_if_temperature2
#problem description: Construct a program that receives the temperature and humidity for today and yesterday and warns the user when it is getting colder or warmer or neither. When it is getting warmer, the program should also warn the user about the changes in humidity. In particular, it should warn the user when today's humidity is more, less, or has not changed compared to yesterday's humidity. Note that the temperature and humidity values could have a decimal point.
#Step 1: Read the temperature for today and yesterday
text = input("Enter the yesterday's temperature: ")
yesterday = float(text)
text = input("Enter the today's temperature: ")
today = float(text)
#Step 2: Read the humidity for today and yesterday
text = input("Enter yesterday's humidity: ")
humidity_yesterday = float(text)
text = input("Enter today's humidity: ")
humidity_today = float(text)
#Step 3: Warn the user about the changes in the temperature
if today < yesterday :
    print("It is getting colder!")
else :
    if today > yesterday :
        #Step 3.1: Determine and warn the user about the changes in humidity when it is getting warmer
        if humidity_today < humidity_yesterday :
            print("It is getting warmer but less humid!")
        elif humidity_today > humidity_yesterday :
            print("It is getting warmer and more humid!")
        else :
            print("It is getting warmer but humidity has not changed!")
    else :
        print("Temperature is the same as yesterday!")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_if_else_grade
#problem description: Construct a program that receives a score from the user and determines the grade as follows:A for scores ≥ 90, B for scores ≥ 80, C for scores ≥ 70, D for scores ≥ 60, F for scores < 60
#Step 1: Read the score
text = input("Enter a score: ")
score = int(text)
#Step 2: Determine the grade for the score
if score >= 90 :
    grade = "A"
elif score >= 80 :
    grade = "B"
elif score >= 70 :
    grade = "C"
elif score >= 60 :
    grade = "D"
else :
    grade = "F"
#Step 3: Print the grade
print("Grade =", grade)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_ifelseif_grade2
#problem description: Construct a program that receives a grade from the user and prints the numeric range for that grade using the following grading rules: A for scores ≥ 90, B for scores ≥ 80, C for scores ≥ 70, D for scores ≥ 60, F for scores < 60, For example, if the user enters the grade D, the program prints "Score is in range [60-70)". 
#Step 1: Read the letter grade
grade = input("Enter a grade letter in uppercase: ")
#Step 2: Determine and print the numeric range for the input letter grade
if grade == "A" :
    print("Score is greater than or equal 90.")
elif grade == "B" :
    print("Score is in range [80-90).")
elif grade == "C" :
    print("Score is in range [70-80).")
elif grade == "D" :
    print("Score is in range [60-70).")
else :
    print("Score is below 60.")



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_dictionary:q_py_dict_access1
dict = {"a": 7, 7: "a", "7":"aa"}
print(dict["a"])
print(dict["7"])
print(dict[7])


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_dictionary:q_py_dict_access2
dict = {"Name": "Superman", "friends": 100}
dict["friends"] = dict["friends"] + 43
dict["enemies"] = 50
print(dict["friends"] - dict["enemies"])
print(len(dict))


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_exceptions:q_py_exception_assertion
def test(arr):
    new_list = []
    eCount = 0
    for item in arr:
        try:
            assert isinstance(item,int)
        except AssertionError:
            eCount += 1
            new_list.append(item)
    print(eCount)
    print(new_list)
arr = [5, 4, "six", 7, 0, "12", 9, "eleven", "1", 8, "nine", "1"]
test(arr)


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_exceptions:q_py_exceptions_addarr
def num(arr):
    total = 0
    letter_len = 0
    for number in arr:
        try:
            temp = number // 2
            total += temp
        except TypeError:
            letter_len += len(number)
    return letter_len + total
arr = ["12", "eight", 7, 11, "nine", 8, "14", "five", "six", 3, 0, "1"]
print(num(arr))


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_exceptions:q_py_list_except1
the_list = (1, 2, 3, 4, 5)
sum = 0
error = 0
for i in range(10):
      try:
          sum += the_list[i]
      except:
          error += 1
print(sum)
print(error)


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_exceptions:q_py_value_except1
def str_to_int(var):
    try:       
        print(int(var))
    except ValueError:
        print("Please give a number!")
my_list = ["one", "1", "two", "2", "three", "3"]
str_to_int(my_list[1])


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_file_processing:q_py_file1
import io
file = open("text.txt", "r")
print(file.read(8))



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_functions:q_py_fun_car1
def fuel(gallons, gas, tank_size):
    gas = min(gallons + gas, tank_size)
    return gas
gas = 50-20
gallons = fuel(25, gas, 50)
print(gallons)



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_functions:q_py_fun_car2
def fuel(gallons, gas, tank_size):
    gas = min(gallons + gas, tank_size)
    return gas
def drive(gas, consumption):
        if gas < consumption:
            gas = 0
        else:
            gas = gas - consumption
        return gas
gas = 50-42
gallons = fuel(25, gas, 50)
print(gallons)
gallons = drive(gallons, 20)
print(gallons)



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_if_statement:q_py_if_elif1
var = -1
if var == 0:
    print("Got zero")
elif var % 2 == 0:
    print("Got an even value")
else:
    print("Got an odd value")



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_if_statement:q_py_nested_if1
x, y, z = 3, 5, 10
if x > y:
    if x < z:
        print(x)
    else:
        print(z)
else:
    if y < z:
        print(y)
    else:
        print(z)



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_if_statement:q_py_nested_if_elif1
var = 18
if var % 2 == 0:
    if var >= 10:
        print("Got a large even value")
    else:
        print("Got a small even value")
else:
    if var >= 10:
        print("Got a large odd value")
    else:
        print("Got a small odd value")


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_if_statement:q_py_nested_if_elif2
side1 = 52
side2 = 55
side3 = 51
if (side1 + side2) > side3 \
	and (side1 + side3) > side2 \
	and (side2 + side3) > side1:
    if side1 == side2 == side3:
        print("equilateral triangle")
    elif (side1 == side2 and side3 != side1) \
	or (side1 == side3 and side2 != side1) \
	or (side2 == side3 and side2 != side1):
        print("isosceles triangle")
    elif (side1 != side2) \
		and (side1 != side3) \
		and  (side2 != side3):
        print("scalene triangle")
else:
    print("it is not a triangle")


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_lists:q_py_add_two_lists1
a = [1,2,3,4]
b = []
for i in range(len(a)):
    b.append(a[i] + 2)
c = a + b
print(c)


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_lists:q_py_list_access1
my_list = [1, 4, 14, -3, 9]
my_list[4] = 2
print(my_list)


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_lists:q_py_list_access2
my_list = [1, 2, 3]
for i in range(len(my_list)):
    my_list[i] = my_list[i] * 9
print(my_list)


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_lists:q_py_list_append1
my_list = []
for i in range(0, 10):
    my_list.append(i + 1)
print(len(my_list))
print(my_list[0])
print(my_list[-1])


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_lists:q_py_list_remove1
a =  [1, 4, 14, -3, 9]
a.pop()
print(a)
a.pop(-1)
print(a)


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_logical_operators:q_py_account_logic1
account1 = 145
account2 = 145 + 50
price = 250
can_afford = account1 >= price or account2 >= price
account2 = account2 - price
money_left = account1+account2 > 0
result = money_left


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_logical_operators:q_py_comparison_logic1
number1 = 9
number2 = 5
print(number1 < number2)
print(number1 != number2)



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_loops:q_py_for_loop1
a = 1
for i in range(0,4):
    print(a + i)



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_loops:q_py_nested_while1
i = 0
while i < 2:
    j = 0
    while j < 4:
        print(j)
        j = j + 1
    i = i + 1



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_loops:q_py_while_loop1
a = 0
while (a < 3):
   print(a)
   a = a + 1



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_loops:q_py_while_loop2
n = 5
i = 1
a = 0
b = 1
print(b)
while i < n:
    c = a + b
    print(c)
    a = b
    b = c
    i = i + 1



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_output_formatting:q_py_output1
print("precision:{0:3.1f}".format(1.57))


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_output_formatting:q_py_output2
print("various precision:{0:6.2f},{0:6.3f}".format(1.23))


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_output_formatting:q_py_output3
a = -9
b = -9*3
c = -9*2+1
print("{0}, {1}".format(a, c))
print("{1}, {0}".format(c, b))


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_output_formatting:q_py_output4
print("Arguments:{0:3d},{2:6.2f},{1:7.3f}".format(859, 50.859, 14.859))


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_references:q_py_int_ref1
def modify(number):
    number = 5 * 2
    print(number)
    return number
def main():
    number = 5
    print(number)
    new_number = modify(number)
    print(number)
    print(new_number)  
main()



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_references:q_py_list_int_ref1
def main():
    numbers = [1, 3, 5, 7, 11, 13]
    print(numbers)
    original = numbers
    numbers[3] = 2
    print(original)
    original[3+1] = 4
    print(numbers)    
main()


#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_references:q_py_list_str_ref1
def modify(the_list):
    the_list[0] = the_list[0].replace("7", "0")
    return the_list
def main():
    outer_list = ["I have watched 7 movies."]
    print(outer_list[0])
    modify(outer_list)
    print(outer_list[0])
    outer_list = modify(outer_list)
    print(outer_list[0])
main()



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_references:q_py_str_ref1
def modify(the_string):
    the_string = the_string.replace("7", "0")
    return the_string
def main():
    outer_string = "I have watched 7 movies."
    print(outer_string)
    modify(outer_string)
    print(outer_string)
    outer_string = modify(outer_string)
    print(outer_string)
main()



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_strings:q_py_concat_strings1
sep = "!"
result = ""
i = 0
while i < 3:
    result += "ha" + sep
    i += 1
print(result)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_objects3
class Account:
  def __init__(self):
    self.balance = 0
  def deposit(self, sum):
    self.balance += sum
  def withdraw(self, sum):
    self.balance -= sum
  def get_balance(self):
    return self.balance
def main():
  accounts = {}
  accounts[259] = Account()
  accounts[632] = Account()
  accounts[259].deposit(500)
  accounts[632].deposit(800)
  accounts[259].withdraw(25)
  print(accounts[259].get_balance())
  print(accounts[632].get_balance())
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_intro
dollars = 200 + 250
euros = dollars * 1.122



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_assignment
my_var = 3
my_var = my_var + 1
my_var = 1 + my_var
my_var = my_var + my_var



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_input
name = input("What is your name?")
print("What a lovely name", name)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_float
celsius = input("Give temperature in Celsius:")
fahrenheit = 1.8 * float(celsius) + 32
print(fahrenheit)


#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_if
line = input("Give a number:")
value = float(line)
if value > 5000:
    print("Quite a big number!")
else:
    print("It was not that big...")
print("It's over now!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_while
positive = 0
value = int(input("Give an integer:"))
while value != 0:
  if value > 0:
    positive = positive + 1
  value = int(input("Give an integer:"))
print("Positive numbers:", positive)


#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_for
print("The two times table starts with:")
for i in range(3):
  print(i, "* 2 =", i * 2)
print("That's it!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_function
def calculate_area(width, height):
  print("Dimensions are:", width, height)
  result = width * height
  return height
def main():
  side1 = 12
  side2 = 10
  area = calculate_area(side1, side2)
  print("Area is:", area)
  print("Area is:", calculate_area(2+3, 7+2))
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_list
def find(values, limit):
  bigger = []
  for value in values:
    if value > limit:
      bigger.append(value)
  return bigger
def main():
  my_list = [2, 5, 4, 9]
  my_list.append(16)
  my_list[1] = 6
  first = my_list[0]
  found = find(my_list, 8)
  if len(found) > 0:
    print(found)
  else:
    print("No values.")
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_split
def main():
  values = "45,23,67"
  my_list = values.split(",")
  if len(my_list) > 0:
    biggest = int(my_list[0])
    sum = 0
    for value in my_list:
      value = int(value)
      sum = sum + value
      if value > biggest:
        biggest = value
      print("Sum is:", sum)
    print("The biggest is:", biggest)
  else:
    print("You did not give any numbers.")
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_file
def main():
  my_file = open("items.txt", "r")
  for line in my_file:
    line = line.rstrip()
    parts = line.split(";")
    count = int(parts[0])
    if count < 10:
       print(parts[1])
  my_file.close()
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_class1
bus1 = Bus(50)
bus1.take_passengers(40)
taken = bus1.take_passengers(60)
print(taken)
bus1.leave_passengers(10)
print(bus1.get_passenger_count())
bus2 = Bus(60)
bus2.take_passengers(10)



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_python_class2
class Bus:
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = 0
  def take_passengers(self, count):
    added = min(count, self.capacity - self.passengers)
    self.passengers = self.passengers + added
    return added
  def leave_passengers(self, count):
    if self.passengers < count:
      return False
    self.passengers = self.passengers - count
    return True
  def get_passenger_count(self):
    return self.passengers
  def is_bigger_than(self, other):
    return self.capacity > other.capacity
bus1 = Bus(50)
count = bus.take_passengers(60)
print(count)
bus1.leave_passengers(10)
print(bus1.get_passenger_count())
bus2 = Bus(30)
print(bus1.has_more_passengers(bus2))


#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_vals_refs1
def change(number):
  number = 9
  print("Number is now:", number)
def main():
  number = 5
  change(number)
  print("In main, number is now:", number)
  print("It did not change!")
main()


#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_vals_refs2
def change(numbers):
  numbers[0] = 5
  print(numbers)
def main():
  numbers = [2, 8, 14]
  change(numbers)
  print(numbers)
main()


#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_vals_refs3
def main():
  numbers = [1, 7, 18]
  original = numbers
  numbers[2] = 11
  print(original)
  print(numbers)
  print("They both changed!")
main()


#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_tryexcept1
try:
  a = "1"
  b = "two"
  c = int(a) + int(b)
  print("Sum is:", c)
except ValueError:
  print("Conversion failed!")
print("All done!")



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_tryexcept2
def average(a, b):
  sum = int(a) + int(b)
  return sum / 2
def main():
  try:
    avg = average("1", "two")
    print("Avg is:", avg)
  except ValueError:
    print("Error occurred!")
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_file1
def main():
  my_file = open("visitors.txt", "r")
  sum = 0
  count = 0
  for line in my_file:
    visitors = int(line)
    sum = sum + visitors
    count = count + 1
  my_file.close()
  print("On average", sum / count, "visitors.")
main()



#CODE_SNIPPET
#exercise type: ae
#exercise name: ae_adl_file2
def main():
  my_file = open("courses.txt", "r")
  category = "math"
  print("Courses in this category:")
  for line in my_file:
    line = line.rstrip()
    parts = line.split(";")
    if parts[0] == category:
      print(parts[1])
  my_file.close()
main()



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_strings:q_py_substring1
a = "Hello World"
print(a[:6])
print(a[6+2:])
print(a[6:6+2])



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_two_dimensional_array:q_py_2d_arrays1
multiD = [[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[15, 16, 17, 18]]
a = multiD[2][2]
b = multiD[2][3]
result = a + b



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_two_dimensional_array:q_py_2d_arrays2
num_rows = 4
num_cols = 4
array = [[0] * num_cols for i in range(num_rows)]
for i in range(0, len(array)):
	for j in range(0, len(array)):
		array[i][j] = i + j
result = array[2+1][2-1]



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_two_dimensional_array:q_py_2d_arrays3
rows = 2
columns = 3
numbers = [[0] * columns for i in range(rows)]
for i in range(0,rows):
   for j in range(0,columns):
       numbers[i][j] = 1 + j - i
for i in range(0,rows):
   for j in range(0,columns):
       print(numbers[i][j])



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_two_dimensional_array:q_py_2d_arrays4
data = [[0, 2, 5, -1],
		[1 ,2, 4, 3],
		[0, 7, -1, 0],
		[0, -1, 2, 9]]
result = 0
for i in range(0,len(data)): 
	for j in range(0,len(data)): 
		if data[i][j] > -1:
			result += 1



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_variables:q_py_arithmetic1
luckyNumber1 = 9
luckyNumber2 = 9 - luckyNumber1 // 9
print(luckyNumber2)



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_variables:q_py_arithmetic2
i = 2
result = 2 * i + 2 ** i



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_variables:q_py_exchange1
dollars_per_euro = 1.1
commission = 4
euros = 13
dollars = euros * dollars_per_euro - commission
result = dollars



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_variables:q_py_exchange2
dollars_per_euro = 1.1
commission = 4
dollars = 14
euros = int(dollars / dollars_per_euro) - commission        
result = euros



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_py_topic_variables:q_py_swap1
luckyNumber1 = 9
luckyNumber2 = 9 + 5
temp =  luckyNumber1
luckyNumber1 = luckyNumber2
luckyNumber2 = temp
print(luckyNumber1)
print(luckyNumber2)



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_topic_classes_objects:q_py_inheritance_animal1
class Aminal:
    def set_age(self, age):
        self.age = age
    def get_age(self):
          return self.age
    def speak(self):
          return "gibberish"
class Dog(Aminal):
    def speak(self):
        return "wow-wow"
class Man(Aminal): 
    def speak(self):
        return "How are you doing?"
def main():
    m = Man()
    m.set_age(9*2)
    d = Dog()
    d.set_age(9)
    print(m.speak())
    print(m.get_age())
    print(d.speak())
    print(d.get_age())
main()



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_topic_classes_objects:q_py_obj_account1
class Account:
    def __init__(self, deposit=0):
        self.balance = deposit
    def deposit(self, sum):
        self.balance += sum
    def withdraw(self, sum):
        self.balance -= sum
    def get_balance(self):
        return self.balance
def main():
    accounts = {}
    accounts[0] = Account()
    accounts[1] = Account(244)
    accounts[0].deposit(244)
    accounts[1].deposit(244)
    accounts[0].withdraw(244-50)
    accounts[1].withdraw(244-100)
    print(accounts[0].get_balance() + accounts[1].get_balance())
main()



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_topic_classes_objects:q_py_obj_bus1
class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = 0
    def take_passengers(self, count):
        added = min(count, self.capacity - self.passengers)
        self.passengers = self.passengers + added
        return added
    def leave_passengers(self, count):
        if self.passengers < count:
          return False
        self.passengers = self.passengers - count
        return True
    def get_passenger_count(self):
        return self.passengers
    def is_bigger_than(self, other):
        return self.capacity > other.capacity
    def has_more_passengers(self, other):
        return self.passengers > other.passengers
def main():
    bus1 = Bus(41)
    bus2 = Bus(25)
    print(bus1.is_bigger_than(bus2))
    added = bus1.take_passengers(30)
    print(added)
    print(bus1.get_passenger_count())
    bus2.leave_passengers(10)
    print(bus1.has_more_passengers(bus2))
main()



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_topic_classes_objects:q_py_obj_car1
class Car:
    def __init__(self, tank_size, gas):
        self.tank_size = tank_size
        self.gas = gas
    def fuel(self, gallons):
        added = min(gallons, self.tank_size - self.gas)
        self.gas = self.gas + added
        return added
    def drive(self, consumption):
        if self.gas < consumption:
            self.gas = 0
            return False
        self.gas = self.gas - consumption
        return True
    def get_fuel(self):
        return self.gas
car = Car(30, 0)
gallons = car.fuel(25)
print(gallons)
car.drive(15)
print(car.get_fuel())



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_topic_classes_objects:q_py_obj_car2
class Car:
    def __init__(self, tank_size, gas):
        self.tank_size = tank_size
        self.gas = gas
    def fuel(self, gallons):
        added = min(gallons, self.tank_size - self.gas)
        self.gas = self.gas + added
        return added
    def drive(self, consumption):
        if self.gas < consumption:
            self.gas = 0
            return False
        self.gas = self.gas - consumption
        return True
    def get_fuel(self):
        return self.gas
 
    def has_more_fuel(self, another):
        return self.gas > another.gas
car = Car(43, 5)
gallons = car.fuel(25)
print(gallons)
car.drive(15)
print(car.get_fuel())
another_car = Car(43, 5)
another_car.fuel(10)
print(car.has_more_fuel(another_car))



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_topic_classes_objects:q_py_obj_point1
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def set_point(self, x, y):
        self.x = x
        self.y = y
def above(pt1, pt2):
    if pt1.y > pt2.y:
        return "Above!"
    elif pt1.y > pt2.y:
        return "Same!"
    else:
        return "Below!"
def main():
    p1 = Point(2, 5)
    p2 = Point()
    p2.set_point(6-2, 6)
    print(above(p1, p2))
main()



#CODE_SNIPPET
#exercise type: q_py
#exercise name: q_topic_classes_objects:q_py_obj_student1
class Student:
    def __init__(self, name, quiz, hw, project):
        self.name = name
        self.quiz = float(quiz)
        self.hw = float(hw)
        self.project = float(project)
    def get_name(self):
        return self.name
    def score(self):
        return (self.quiz + self.hw + self.project) / 3.0
def main():
    students = []
    students.append(Student("Mike", 70, 60, 80))
    students.append(Student("Rose", 50, 72, 90))
    students.append(Student("Michele", 60, 50, 72+10))
    students.append(Student("Sofia", 80, 72-10,  80))
    # process subsequent lines of the file
    highest = students[0]
    for i in range(1, len(students)):
        if students[i].score() > highest.score():
            highest = students[i]
    print(highest.get_name())
    print(int(highest.score()))
main()



#CODE_SNIPPET
#exercise type: py
#exercise name: py_if_else_wage
#problem description: Construct a program for the payment department of a company to calculate the wage of an employee based on the number of hours that the employee has worked. If an employee works over 40 hours in a week, the payment amount should take into account the overtime hours. The overtime hours are paid at a rate one and a half times the regular pay rate.
#Step 1: Assign initial values to the variables which we need for this program
rate = 8.25
standard = 40
#Step 2: Read the number of hours that the employee has worked
text = input("Enter the number of hours that the employee has worked: ")
hours = int(text)
#Step 3: Pay overtime at "time and a half" of the regular rate of pay
if hours > standard :
    wage = standard * rate + ( hours - standard ) * ( rate * 1.5 )
else :
    wage = hours * rate
#Step 4: Print the calculated wage
print("Wage:", wage)


#CODE_SNIPPET
#exercise type: py
#exercise name:  py_if_else_wage2
#problem description: Construct a program for the payment department of a company to calculate the wage of an employee who works at the customer service call center. Like other employees in the company, the employees at the customer service call center are paid based on the hours that they work. If they work over 40 hours in a week, the payment amount should take into account the overtime hours. The overtime hours are paid at a rate one and a half times the regular pay rate. The company's policy is to pay more to those employees at the customer service call center who work during weekends. Therefore, the minimum extra pay that the employees could receive for each day of work during weekends is $30. The extra pay increases to the maximum of $50 for the employees who have at least 5 days of work during weekends.
#Step 1: Assign initial values to the variables which we need for this program
rate = 8.25
standard = 40
weekend_pay_min = 30
weekend_pay_max = 50
#Step 2: Read the input data
text = input("Enter the number of hours that the employee has worked: ")
hours = int(text)
text = input("Enter the number of days that the employee has worked during weekends: ")
no_weekend_days = int(text)
#Step 3: Pay overtime at "time and a half" of the regular rate of pay
if hours > standard :
    wage = standard * rate + ( hours-standard ) * ( rate * 1.5 )
else :
    wage = hours * rate
#Step 4: Take into account the extra pay for the work during weekends days
if no_weekend_days < 5 :
    wage += (no_weekend_days * weekend_pay_min)
else :
    wage += (no_weekend_days * weekend_pay_max)
#Step 5: Print the calculated wage
print("Wage:", wage)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_check_adjacent
#problem description: Construct a program that checks whether a sequence of numbers, entered one at a time, contains adjacent duplicates. The user enters -1 to indicate the end of the input. For example, 4 is a duplicate in the sequence of numbers 1, 3, 4, 4, -1.
#Step 1: Read the first number that the user enters
text = input("Enter a number: ")
num = float(text)
#Step 2: Read the rest of the numbers that the user enters and check for adjacent duplicates
while num != -1 :
    previous = num
    text = input("Enter a number: ")
    num = float(text)
    if num == previous :
        print("Duplicate input for number:", num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_adjacent_consecutive
#problem description: Construct a program that checks whether a sequence of integers, entered one at a time, contains adjacent integers that are consecutive. The user enters -1 to indicate the end of the input. Note that integers which follow each other in order, without gaps, from smallest to largest are consecutive numbers. For example, 12, 13, 14 and 15 are consecutive numbers.
#Step 1: Read the first integer that the user enters
text = input("Enter an integer: ")
num = int(text)
#Step 2: Read the rest of the integers that the user enters and check for adjacent consecutive numbers
while num != -1 :
    previous = num
    text = input("Enter an integer: ")
    num = int(text)
    if num != -1 and num - previous == 1 :
        print(previous, "and", num, "are consecutive.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_adjacent_greater
#problem description: Construct a program that checks whether a sequence of non-zero numbers, entered one at a time, contains adjacent numbers in ascending order. Numbers are said to be in ascending order when they are arranged from the smallest to the largest number. For example, 5, 9, 13, 17 and 21 are arranged in ascending order. Note that you need to think what value should the program use to indicate the end of the input.
#Step 1: Read the first number that the user enters
text = input("Enter a number: ")
num = float(text)
#Step 2: Read the rest of the numbers that the user enters and check for adjacent numbers in ascending order
while num != 0 :
    previous = num
    text = input("Enter a number: ")
    num = float(text)
    if num != 0 and num > previous :
        print(previous,"and", num, "are in ascending order.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_win_percentage
#problem description: Construct a program that receives from the user the number of games that a sports team won in a tournament of 12 games and calculates the winning percentage of that sports team. The program must ask for the number of the games won until the user enters a valid number.
#Step 1: Assign initial values to the variables which we need for this program
total_games = 12
#Step 2: Read the number that the user enters
text = input("Enter the number of games that the sports team won in the tournament: ")
wins = int(text)
#Step 3: Validate the user input, ask for a valid input as long as the user enters an invalid number; otherwise stop
while wins < 0 or wins > total_games :
    text = input("Enter the number of games that the sports team won in the tournament: ")
    wins = int(text)
#Step 4: Calculate and print the percentage of games won by a team
ratio = wins / total_games
print("Winning percentage:", ratio)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_win_percentage_input
#problem description: Construct a program that receives from the user the number of games in a tournament and the number of the games that a sports team won in the tournament, and calculates the winning percentage of that sports team. The program must ask the user for each of the two inputs until the user enters a valid number.
#Step 1: Read the number of games in the tournament
text = input("Enter the number of games in the tournament: ")
total_games = int(text)
#Step 2: Validate the user input for the number of games in the tournament, ask for a valid input as long as the user enters an invalid number; otherwise stop
while total_games <= 0 :
    text = input("Enter the number of games in the tournament: ")
    total_games = int(text)
#Step 3: Read the number of games that the sports team won in the tournament
text = input("Enter the number of games that the sports team won in the tournament: ")
wins = int(text)
#Step 4: Validate the user input for the number of games that the sports team won in the tournament, ask for a valid input as long as the user enters an invalid number; otherwise stop
while wins < 0 or wins > total_games :
    text = input("Enter the number of games that the sports team won in the tournament: ")
    wins = int(text)
#Step 5: Calculate and print the percentage of games won by a team
ratio = wins / total_games
print("Winning percentage:", ratio)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_win_percentage_won_equal
#problem description: Construct a program that receives from the user the number of games that a sports team won and tied in a tournament of 12 games and calculates the winning percentage of the sports team, counting ties as half wins. The program must ask the user for each of the two inputs until the user enters a valid number.
#Step 1: Assign initial values to the variables which we need for this program
total_games = 12
#Step 2: Read the number of games that the sports team won in the tournament
text = input("Enter the number of games that the sports team won in the tournament: ")
wins = int(text)
#Step 3: Validate the user input for the number of wins, ask for a valid input as long as the user enters an invalid number; otherwise stop
while wins < 0 or wins > total_games :
    text = input("Enter the number of games that the sports team won in the tournament: ")
    wins = int(text)
#Step 4: Read the number of games that the sports team tied in the tournament
text = input("Enter the number of games tied: ")
ties = int(text)
#Step 5: Validate the user input for the number of ties, ask for a valid input as long as the user enters an invalid number; otherwise stop
while ties < 0 or total_games < (ties + wins) :
    text = input("Enter the number of games tied: ")
    ties = int(text)
#Step 6: Calculate and print the percentage of games won by a team, counting ties as half wins
ratio = ( wins + ties // 2) / total_games
print("Winning percentage:", ratio)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_find_average
#problem description: Construct a program that reads a series of integers from the user, sums them up, and calculates their average. The user enters 0 to indicate the end of the input.
#Step 1: Assign initial values to the variables which we need for this program
total = 0
count = 0
#Step 2: Read the first integer that the user enters
text = input("Enter an integer (0 to quit): ")
num = int(text)
#Step 3: Process the integer that the user has entered, then receive and process the next integers as long as the user enters a non-zero integer; otherwise stop
while num != 0 :
    count += 1
    total += num
    print("The sum so far is", total, ", count =", count)
    text = input("Enter an integer (0 to quit): ")
    num = int(text)
#Step 4: Calculate and print the average of the integers entered by the user
if count == 0 :
    print("No integers were entered.")
else :
    average = total / count
print("The average is:", average)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_average_even_nums
#problem description: Construct a program that reads a series of integer values from the user, sums up the integers that are an even number, and calculate their average. The user enters 0 to indicate the end of the input
#Step 1: Assign initial values to the variables which we need for this program
total = 0
count = 0
#Step 2: Read the first integer that the user enters
text = input("Enter an integer (0 to quit): ")
num = int(text)
#Step 3: Process the integer that the user has entered, then receive and process the next integers as long as the user enters a non-zero integer; otherwise stop
while num != 0 :
    if num % 2 == 0 :
        count += 1
        total += num
    print("The sum of even numbers so far is", total, ", count of even numbers =", count)
    text = input("Enter an integer (0 to quit): ")
    num = int(text)
#Step 4: Calculate and print the average of the even integers entered by the user
if count == 0 :
    print("No even integers were entered.")
else :
    average = total / count
print("The average is:", average)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_average_float
#problem description: Construct a program that reads a series of non-negative floating-point numbers from the user, sums them up, and calculate their average. Note that you need to think what value should the program use to indicate the end of the input.
#Step 1: Define the variables that we need for this program
total = 0
count = 0
#/Step 2: Read the first number that the user enters
text = input("Enter a number: ")
num = float(text)
#Step 3: Process the number that the user has entered, then receive and process the next numbers as long as the user enters a non-negative number; otherwise stop
while num >= 0.0 :
    count += 1
    total += num
    print("The sum so far is", total, ", count =", count)
    text = input("Enter a number: ")
    num = float(text)
#Step 4: Calculate and print the average of the numbers entered by the user
if count == 0 :
    print("No numbers were entered.")
else :
    average = total / count
print("The average is:", average)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list2d_basic
#problem description : Construct a program that initializes a 3x4 two-dimensional matrix that has the numbers 1 through 12 for entries, updates the last row to a list filled with 5s, then sets the left-most element in the middle row of the matrix to be 20, and finally prints the matrix.
#Step 1: Define a 3x4 two-dimensional list
matrix = [[ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12]]
#Step 2: Update the two-dimensional list
matrix[2] = [5, 5, 5, 5]
matrix[1][0] = 20
#Step 3: Print the list
print(matrix)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list2d_basic2
#problem description: Construct a program that initializes a 3x3 two-dimensional matrix that has the numbers 1 through 9 for entries, updates the middle row to a list filled with 1s, then sets the top-right element of the matrix to be 10, and finally prints the matrix.
#Step 1: Define a 3x3 two-dimensional list
matrix = [[ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]]
#Step 2: Update the two-dimensional list
matrix[1] = [1, 1, 1]
matrix[0][2] = 10
#Step 3: Print the list
print(matrix)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list2d_basic3 
#problem description: Construct a program that initializes a 2x4 two-dimensional matrix that has multiples of 10 from 10 to 80 for entries, updates the last row to a list holding values 1,3,5,7, then sets the second element of the first row to be 8, and finally prints the matrix.
#Step 1: Define a 2x4 two-dimensional list
matrix = [[ 10, 20, 30, 40 ],
        [ 50, 60, 70, 80 ]]
#Step 2: Update the two-dimensional list
matrix[1] = [1, 3, 5, 7]
matrix[0][1] = 8
#Step 3: Print the list
print(matrix)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_basic
#problem description: Construct a program that initializes a list with three values, changes the first element in the list, and finally, prints the list.
#Step 1: Define a list of three integer values
lst = [123, 100, 39]
#Step 2: Update the list element
lst[0] = 2
#Step 3: Print the list
print(lst)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_basic2
#problem description: Construct a program that initializes a list with five floating-point numbers, changes the second element in the list, and finally, prints the list.
#Step 1: Define a list of five floating-point numbers
lst = [1.1, 2.2, 3.3, 4.4, 5.5]
#Step 2: Update the list element
lst[1] = 20.5
#Step 3: Print the list
print(lst)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_basic3
#problem description: Construct a program that initializes a list with four string values, changes the last element in the list, and finally, prints the list.
#Step 1: Define a list of four string values
lst = ["a", "b", "c", "d"]
#Step 2: Update the list elements
lst[3] = "e"
#Step 3: Print the list
print(lst)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_change
#problem description: Construct a program that increments all values of the list by 1.
#Step 1: Define and initialize the list
lst = [1, 2, 3, 4, 5, 6]
#Step 2: Iterate through the list elements
for i in range(len(lst)):
    #Step 2.1: Increment the element at index i by 1
    lst[i] += 1
#Step 3: Print the list
print(lst)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_swap_adjacent_elements
#problem description: Construct a program that swaps pairs of adjacent elements of the list. For example, if the list is [1, 2, 3, 4, 5, 6], the program will change it to [2, 1, 4, 3, 6, 5]. This program assumes that the list has always an even number of elements.
#Step 1: Define and initialize the list
lst = [1, 2, 3, 4, 5, 6]
#Step 2: Iterate through the pairs of adjacent elements in the list
for i in range(0, len(lst), 2):
    #Step 2.1: Swap the element at index i with the element at index i+1
    temp = lst[i]
    lst[i] = lst[i+1]
    lst[i+1] = temp
#Step 3: Print the list
print(lst)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_fill
#problem description: Construct a program that creates a list of first ten positive odd numbers.
#Step 1: Create an empty list
lst = []
#Step 2: Add the odd numbers to the list one by one
for i in range(10):
    lst.append( 2 * i + 1 )
#Step 3: Print the list
print(lst)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_fill_user_input
#problem description: Construct a program that creates a list of eight string values received from the user.
#Step 1: Create an empty list
lst = []
#Step 2: Add the user inputs to the list one by one
for i in range(8):
    lst.append( input("Enter a value:") )
#Step 3: Print the list
print(lst)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_min_max
#problem description: Write a program that finds the maximum value in a list.
#Step 1: Define and initialize the list
values = [5, 8, 4, 78, 95, 12, 1, 0, 6, 35, 46]
#Step 2: Set the first value to be the maximum value so far.
max_value = values[0]
#Step 3: Iterate through the remaining values in the list and decide which one is the maximum value
for i in range(1, len(values)):
    # Step 3.1: Determine if the element at index i is the maximum value so far
    if (values[i] > max_value):
        max_value = values[i]
#Step 4: Print the maximum value in the list
print("Maximum value:", max_value)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_min
#problem description: Write a program that finds the minimum value in a list.
#Step 1: Define and initialize the list
values = [5, 8, 4, 78, 95, 12, 1, 0, 6, 35, 46]
#Step 2: Set the first value to be the minimum value so far.
min_value = values[0]
#Step 3: Iterate through the remaining values in the list and decide which one is the minimum value
for i in range(1, len(values)):
    # Step 3.1: Determine if the element at index i is the minimum value so far
    if (values[i] < min_value):
        min_value = values[i]
#Step 4: Print the minimum value in the list
print("Minimum value:", min_value)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_rotate
#problem description: Construct a program that has a function that receives a list of values and returns the list rotated to the left by 1 position so that the value at the front of the list goes to the back and the order of the other values stays the same. For example, if the list is [1, 2, 3, 4, 5, 6], the program will change it to [2, 3, 4, 5, 6, 1].
#Step 1: Define the function
def rotate_left(lst):
    #Step 1.1: Store the value at the front in a local variable
    first = lst[0]
    #Step 1.2: Rotate the remaining values of the list to the left
    for i in range(len(lst)-1):
        lst[i] = lst[i + 1]
    #Step 1.3: Move the value at the front to the back of the list
    lst[len(lst)-1] = first
    return lst
#Step 2: Call the function
values =  [3, 8, 9, 8, 7, 5]
print("Original list:", values)
print("Rotated list: ", rotate_left(values))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_rotate_left_twice
#problem description: Construct a program that has a function that receives a list of values and returns the list rotated to the left by 2 position so that the value at the front of the list goes to the second last position, the second value of the list goes to the back, and the order of the other values stays the same. For example, if the list is [1, 2, 3, 4, 5, 6], the program will change it to [3, 4, 5, 6, 1, 2].
#Step 1: Define the function
def rotate_left_by_2(lst):
    #Step 1.1: Store the first two values of the list in local variables
    first = lst[0]
    second = lst[1]
    #Step 1.2: Rotate the remaining values of the list to the left by 2 position
    for i in range(len(lst)-2):
        lst[i] = lst[i + 2]
    #Step 1.3: Move the first two values of the list to the back of the list
    lst[len(lst)-2] = first
    lst[len(lst)-1] = second
    return lst
#Step 2: Call the function
values = [3, 8, 9, 8, 7, 5]
print("Original list:", values)
print("Rotated list: ", rotate_left_by_2(values))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_rotate_right
#problem description: Construct a program that has a function that receives a list of values and returns the list rotated to the right by one position so that the value that is currently at the end of the list is moved to the front, shifting the remaining values to the right. For example, if the list is [1, 2, 3, 4, 5, 6], the program will change it to [6, 1, 2, 3, 4, 5].
#Step 1: Define the function
def rotate_right(lst):
    #Step 1.1: Store the value at the end of the list in a local variable
    last = lst[len(lst)-1]
    #Step 1.2: Rotate the remaining values of the list to the right
    for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i - 1]
    #Step 1.3: Move the value at the end to the front of the list
    lst[0] = last
    return lst
#Step 2: Call the function
values = [3, 8, 9, 8, 7, 5]
print("Original list:", values)
print("Rotated list: ", rotate_right(values))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_rotate_right_twice
#problem description: Construct a program that has a function that receives a list of values and returns the list rotated to the right by 2 position so that the value that is currently at the end of the list is moved to the second position, the second last value of the list is moved to the front of the list, and the remaining values are shifted to the right. For example, if the list is [1, 2, 3, 4, 5, 6], the program will change it to [5, 6, 1, 2, 3, 4].
#Step 1: Define the function
def rotate_right_by_2(lst):
    #Step 1.1: Store the last two values of the list in local variables
    last = lst[len(lst)-1]
    second_last = lst[len(lst)-2]
    #Step 1.2: Rotate the remaining values of the list to the right by 2 position
    for i in range(len(lst)-1, 1, -1):
        lst[i] = lst[i - 2]
    #Step 1.3: Move the last two values of the list to the front of the list
    lst[0] = second_last
    lst[1] = last
    return lst
#Step 2: Call the function
values = [3, 8, 9, 8, 7, 5]
print("Original list:", values)
print("Rotated list: ", rotate_right_by_2(values))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_print_medals
#problem description: Assume that we have a 7x4 matrix that stores the number of medals that seven countries won in the skating competitions at the Winter Olympic. This matrix looks like as follows: [[ "Canada", 1, 0, 1 ],[ "China", 1, 1, 0 ],...] Each row of this matrix corresponds to the medal counts for the country in that row. The second, third, and fourth numbers within a row represent the number of Gold, Silver, and Bronze medals won by the corresponding country in that row. Construct a program that takes this matrix and prints a table of medal counts with row total that shows the number of Gold, Silver, Bronze, and Total medals for each of the countries who participated in the competition. The output table should look like as follows:
#    Country    Gold  Silver  Bronze   Total
#     Canada        1       0       1            2
#      China        1       1       0            2
#Step 1: Define a 7x4 matrix that stores the number of medals won by seven countries
medal_counts = [[ "CAN", 1, 0, 1 ],
                [ "CHN", 1, 1, 0 ],
                [ "GER", 0, 0, 1 ],
                [ "KOR", 1, 0, 0 ],
                [ "JPN", 0, 1, 1 ],
                [ "RUS", 0, 1, 1 ],
                [ "USA", 1, 1, 0 ]]
#Step 2: Print the header of the output table
print("{:>4s}{:>3s}{:>3s}{:>3s}{:>4s}".format("Name","G","S","B","All"))
#Step 3: Iterate through the rows in the medal counts matrix
for i in range(len(medal_counts)):
    #Step 3.1: Assign initial values to variables we need for printing row i
    line = "{:>4s}".format(medal_counts[i][0])
    row_total = 0
    #Step 3.2: Iterate through the columns that have medal counts
    for j in range(1, len(medal_counts[0])):
        #Step 3.2.1: Append medal counts to the content of row i
        line += "{:>3d}".format(medal_counts[i][j])
        #Step 3.2.2: Update the row total for row i
        row_total += medal_counts[i][j]
    #Step 3.3: Add the row total to the content of the output table for row i
    line += "{:>3d}".format(row_total)
    #Step 3.4: Print the content of the output table for row i
    print(line)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_print_medals_row_column_total
#problem description: Assume that we have a 7x4 matrix that stores the number of medals that seven countries won in the skating competitions at the Winter Olympic. This matrix looks like as follows:[[ "Canada", 1, 0, 1 ],[ "China", 1, 1, 0 ],...] Each row of this matrix corresponds to the medal counts for the country in that row. The second, third, and fourth numbers within a row represent the number of Gold, Silver, and Bronze medals won by the corresponding country in that row. Construct a program that takes this matrix and prints a table of medal counts with row and column totals. The column totals are the sum of the gold, silver, and bronze medals won in the competition. The output table should look like as follows:
#      Country    Gold  Silver  Bronze   Total
#         Canada        1       0       1          2
#            China        1       1       0          2
#           ...
#Column Total      4       4       4
#Step 1: Define a 7x4 matrix that stores the number of medals won by seven countries
medal_counts = [[ "CAN", 1, 0, 1 ],
                [ "CHN", 1, 1, 0 ],
                [ "GER", 0, 0, 1 ],
                [ "KOR", 1, 0, 0 ],
                [ "JPN", 0, 1, 1 ],
                [ "RUS", 0, 1, 1 ],
                [ "USA", 1, 1, 0 ]]
#Step 2: Create a list to store column totals
column_totals = [0] * ( len(medal_counts[0]) - 1 )
#Step 3: Print the header of the output table
print("{:>4s}{:>3s}{:>3s}{:>3s}{:>4s}".format("Name","G","S","B","All"))
#Step 4: Iterate through the rows in the medal counts matrix
for i in range(len(medal_counts)):
    #Step 4.1: Assign initial values to variables we need for printing row i
    line = "{:>4s}".format(medal_counts[i][0])
    row_total = 0
    #Step 4.2: Iterate through the columns that have medal counts
    for j in range(1, len(medal_counts[0])):
        #Step 4.2.1: Append medal counts to the content of row i
        line += "{:>3d}".format(medal_counts[i][j])
        #Step 4.2.2: Update the row total for row i
        row_total += medal_counts[i][j]
        #Step 4.2.3: Update the column total for the column j
        column_totals[j-1] += medal_counts[i][j]
    #Step 4.3: Add the row total to the content of the output table for row i
    line += "{:>3d}".format(row_total)
    #Step 4.4: Print the content of the output table for row i
    print(line)
#Step 5: Print the column totals
line = "{:>4s}".format("All")
for j in range(len(column_totals)):
    line += "{:>3d}".format(column_totals[j])
print(line)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_list_process_elements
#problem description: Construct a program that has a function that receives a list and calculates the sum of the values in that list.
#Step 1: Define the function
def calculate_list_sum(lst):
    #Step 1.1: Assign initial value to the variable which we need for this program
    total = 0
    #Step 1.2: Iterate through the list values and add each value to the running total
    for x in lst:
        total += x
    #Step 1.3: Print the sum of the list values
    print("The sum of all values in the list:", total)
#Step 2: Call the function
values = [6, 15, 9, 12, 1, 8]
calculate_list_sum(values)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_average_list_elements 
#problem description: Construct a program that has a function that receives a list and calculates the average of the values in that list. The program should handle lists with arbitrary number of values (including an empty list).
#Step 1: Define the function
def calculate_list_average(lst):
    #Step 1.1: Assign initial value to the variable which we need for this program
    total = 0
    #Step 1.2: Iterate through the list values and add each value to the running total
    for x in lst:
        total += x
    #Step 1.3: Calculate and print the average of the list values
    if len(lst) == 0 :
        print("The list has no values.")
    else :
        average = total / len(lst)
        print("Average is:", average)
#Step 2: Call the function
values = [6, 15, 9, 12, 1, 8]
calculate_list_average(values)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_search_list
#problem description: Construct a program that has a function that receives two lists and prints the values in the 2nd list that exist in the 1st list.
#Step 1: Define the function
def search_lists(lst1, lst2):
    #Step 1.1: Iterate through the values in the 2nd list
    for val2 in lst2:
        #Step 1.1.1: Print the value in the 2nd list if it exists in the 1st list
        if val2 in lst1:
            print(val2, "exists in both list.")
#Step 2: Call the function
values_1 = [2.0, 11, 4, 5, 3, 3.5, 4, 10, 16]
values_2 =  [7, 11, 3]
search_lists(values_1, values_2)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_search_list_total_count
#problem description: Construct a program that has a function that receives two lists and prints the total number of times the elements in the 2nd list appear in the 1st list. For example, if the 1st list is [1, 2, 3, 3, 4, 4, 5, 6] and the 2nd list is [3, 4, 5, 6, 7], then the total number of times that the elements in the 2nd list appear in the 1st list is 6. Note that we need to count matches for all values in the 2nd list (including duplicate values, if any).
# Step 1: Define the function
def search_lists(lst1, lst2):
    #Step 1.1: Iterate through the values in the 2nd list
    count = 0
    for val2 in lst2:
        #Step 1.1.1: Iterate through the values in the 1st list
        for val1 in lst1:
            #Step 1.1.1.1: Increment the number of matches if we find a match
            if val2 == val1:
                count += 1
    print("Total number of times the elements in the 2nd list appear in the 1st list is", count)
#Step 2: Call the function
values_1 = [2.0, 11, 11, 4, 5, 3, 3, 3.5, 4, 10, 16]
values_2 =  [7, 11, 3]
search_lists(values_1, values_2)



#CODE_SNIPPET
#exercise type: py
#exercise name:py_search_list_count_each
#problem description: Construct a program that has a function that receives two lists and creates a list that contains the number of times each element in the 2nd list appears in the 1st list. For example, if the 1st list is [1, 2, 3, 3, 4, 4, 5, 6] and the 2nd list is [3, 4, 5, 6, 7], then the list that contains the number of times each element in the 2nd list appears in the 1st list is [2, 2, 1, 1, 0]. Assume that all elements in the 2nd list are unique.
#Step 1: Define the function
def search_lists(lst1, lst2):
    #Step 1.1: Create a list that we need to store the number of matches
    counts = [0] * len(lst2)
    #Step 1.2: Iterate through the values in the 2nd list
    for val2 in lst2:
        #Step 1.2.1: Iterate through the values in the 1st list
        for val1 in lst1:
            #Step 1.2.1.1: Increment the number of matches for val2 if we find a match for that
            if val2 == val1:
                counts[ lst2.index(val2) ] += 1
    print("The list that contains the number of times each element in the 2nd list appears in the 1st list:", counts)
#Step 2: Call the function
values_1 = [2.0, 11, 11, 4, 5, 3, 3, 3.5, 4, 10, 16]
values_2 =  [7, 11, 3]
search_lists(values_1, values_2)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_soda_survey
#problem description: Suppose a soda manufacturer held a taste test for four new flavors to determine if people liked them. The manufacturer got 10 people to try each new flavor and give it a score from 1 to 5, where 1 equals poor and 5 equals excellent. The results of that survey is stored in a matrix. Each row of the matrix holds the responses that all testers gave for one particular soda flavor, and each column holds the responses of one person for all sodas. Construct a program that determines the maximum rating that each of the four new flavors of soda received.
#Step 1: Define a 4x10 two-dimensional list
ratings_data = [[3, 4, 5, 2, 1, 4, 3, 2, 4, 4],
                [2, 4, 3, 4, 3, 3, 2, 1, 2, 2],
                [3, 5, 4, 5, 5, 3, 2, 5, 5, 5],
                [1, 1, 1, 3, 1, 2, 1, 3, 2, 4]]
#Step 2: Get the dimensions of the list that stores the ratings data
num_sodas = len(ratings_data)
num_respondents = len(ratings_data[0])
#Step 3: Create a list to store the maximum rating of each soda flavor
soda_max = [0] * num_sodas
#Step 4: Iterate through the sodas
for i in range(num_sodas):
    #Step 4.1: Find the maximum rating of soda i+1 by iterating through its ratings
    for j in range(num_respondents):
        if ratings_data[i][j] > soda_max[i] :
            soda_max[i] = ratings_data[i][j]
#Step 5: Print the maximum rating for each soda
print("Maximums:")
for i in range(num_sodas):
    print("Soda # {:d} : {:d}".format((i+1), soda_max[i]))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_soda_survey_soda_avg
#problem description: Suppose a soda manufacturer held a taste test for four new flavors to determine if people liked them. The manufacturer got 10 people to try each new flavor and give it a score from 1 to 5, where 1 equals poor and 5 equals excellent. The results of that survey is stored in a matrix. Each row of the matrix holds the responses that all testers gave for one particular soda flavor, and each column holds the responses of one person for all sodas. Construct a program that determines the average ratings that respondents provided to four new flavors of soda.
#Step 1: Define a 4x10 two-dimensional list
ratings_data = [[3, 4, 5, 2, 1, 4, 3, 2, 4, 4],
                [2, 4, 3, 4, 3, 3, 2, 1, 2, 2],
                [3, 5, 4, 5, 5, 3, 2, 5, 5, 5],
                [1, 1, 1, 3, 1, 2, 1, 3, 2, 4]]
#Step 2: Get the dimensions of the list that stores the ratings data
num_sodas = len(ratings_data)
num_respondents = len(ratings_data[0])
#Step 3: Create a list to store the sum of rating of each soda flavor
soda_sum = [0] * num_sodas
#Step 4: Iterate through the sodas
for i in range(num_sodas):
    #Step 4.1: Calculate the sum of the ratings for the soda i+1
    for j in range(num_respondents):
        soda_sum[i] += ratings_data[i][j]
#Step 5: Calculate and print the average rating for each soda
print("Averages:")
for i in range(num_sodas):
    print("Soda # {:d} : {:.2f}".format((i+1), soda_sum[i]/num_respondents))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_soda_survey_soda_respondent_avg
#problem description: Suppose a soda manufacturer held a taste test for four new flavors to determine if people liked them. The manufacturer got 10 people to try each new flavor and give it a score from 1 to 5, where 1 equals poor and 5 equals excellent. The results of that survey is stored in a matrix. Each row of the matrix holds the responses that all testers gave for one particular soda flavor, and each column holds the responses of one person for all sodas. Construct a program that determines the average ratings that respondents provided to four new flavors of soda.
#Step 1: Define a 4x10 two-dimensional list
ratings_data = [[3, 4, 5, 2, 1, 4, 3, 2, 4, 4],
                [2, 4, 3, 4, 3, 3, 2, 1, 2, 2],
                [3, 5, 4, 5, 5, 3, 2, 5, 5, 5],
                [1, 1, 1, 3, 1, 2, 1, 3, 2, 4]]
#Step 2: Get the dimensions of the list that stores the ratings data
num_sodas = len(ratings_data)
num_respondents = len(ratings_data[0])
#Step 3: Create a list to store the sum of rating of each soda flavor
soda_sum = [0] * num_sodas
#Step 4: Create a list to store the sum of rating of each respondent
respondent_sum = [0] * num_respondents
#Step 5: Iterate through the sodas
for i in range(num_sodas):
    #Step 5.1: Iterate through the respondents
    for j in range(num_respondents):
        #Step 5.1.1: Update sum of ratings given to soda i+1
        soda_sum[i] += ratings_data[i][j]
        #Step 5.1.2: Update sum of ratings from respondent j+1
        respondent_sum[j] += ratings_data[i][j]
#Step 6: Calculate and print the average rating for each soda
print("Averages:")
for i in range(num_sodas):
    print("Soda # {:d} : {:.2f}".format((i+1), soda_sum[i]/num_respondents))
#Step 7: Calculate and print the average rating for each respondent
for j in range(num_respondents):
    print("Respondent # {:d} : {:.2f}".format((j+1), respondent_sum[j]/num_sodas))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_temperature
#problem description : Construct a program that reads a series of temperatures and reports the average temperature and the number of the days that are above the average. Assume that the input values could have a decimal point.
#Step 1: Read the number of days that we have to enter their temperature data
num_days = int(input("Enter the number of temperature values that will be entered: "))
#Step 2: Read the temperature values
temps = []
total = 0
for i in range(num_days):
    val = float(input("Enter the temperature: "))
    temps.append(val)
    total += val
#Step 3: Calculate the average temperature
average = 0
if num_days == 0:
    print("No temperature values were entered.")
else:
    average = total / num_days
#Step 4: Count the number of the days that are above the average temperature
above = 0
for x in temps:
    if x > average:
        above += 1
#Step 5: Display the results
print("Average temperature:", average)
print(above, "days above average.")


#CODE_SNIPPET
#exercise type: py
#exercise name:py_temperature_list_days_above_threshold
#Problem description : Construct a program that reads a series of temperatures and reports the days that are above 32 degrees Fahrenheit. Assume that the temperature values are in Fahrenheit. Also assume that input values could have a decimal point.
#Step 1: Read the number of days that we have to enter their temperature data
num_days = int(input("Enter the number of temperature values that will be entered: "))
#Step 2: Read the temperature values
temps = []
for i in range(num_days):
    val = float(input("Enter the temperature: "))
    temps.append(val)
#Step 3: Create a list that contains the days that are above 32 degrees Fahrenheit
days_above_32 = []
for i in range(len(temps)) :
    if temps[i] > 32:
        days_above_32.append("Day " + str(i+1))
#Step 4: Print the result
print("Days above 32 degrees Fahrenheit:", days_above_32)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_digits
#problem description: Construct a program that prints the digits of an integer from right to left.
#Step 1: Assign initial values to the variables which we need for this program
num = 1234
#Step 2: Print the digits of the integer from right to left
while num > 0 :
    #Step 2.1: Get the last digit in the integer
    last_digit = num % 10
    #Step 2.2: Print the extracted digit
    print(last_digit)
    #Step 2.3: Remove the last digit from the integer
    num = num // 10



#CODE_SNIPPET
#exercise type: py
#exercise name: py_sum_digits
#problem description: Construct a program that calculates the sum of the digits of an integer.
#Step 1: Assign initial values to the variables which we need for this program
num = 1234
total = 0
#Step 2: Sum up the digits of the integer
while num > 0 :
    #Step 2.1: Get the last digit in the integer
    last_digit = num % 10
    #Step 2.2:?Add the last digit to the sum of digits so far
    total = total + last_digit
    #Step 2.3: Remove the last digit from the integer
    num = num // 10
    print("last digit:", last_digit, ", sum:", total, ", integer:", num)
print("The sum of the digits:", total)



#CODE_SNIPPET
#exercise type: py
#exercise name:py_reverse_number
#problem description: Construct a program that reverses the digits of an integer mathematically. 
#Step 1: Assign initial values to the variables which we need for this program
num = 1234
reverse = 0
#Step 2: Reverse the digits of the integer mathematically
while num > 0 :
    #Step 2.1: Get the last digit in the integer
    last_digit = num % 10
    #Step 2.2:?Append the last digit to reverse
    reverse = (reverse * 10) + last_digit
    #Step 2.3: Remove the last digit from the integer
    num = num // 10
    print("last digit:", last_digit, ", reverse:", reverse, ", integer:", num)
print("The reversed integer is:", reverse)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_work_hours
#problem description: Suppose we have an input file that contains information about how many hours each employee of a company has worked. The file looks like the following (Employee's name, Hours):
#Erica 7.5 8.5 10.25 8 8.5
# Erin 10.5 11.5 12 11 10.75
# Simone 8 8 8
# ...
# Construct a program that reads this file and calculates the total number of hours worked by each individual. Make sure that the program handles each specific exception that could occur. 
#Step 1: Define the function
def report_work_hours(file_name):
    #Step 1.1: Enclose the code that might throw an exception within the try block
    try :
        #Step 1.1.1: Open the file and process each line in the file
        myfile = open( file_name, "r")
        for line in myfile:
            tokens = line.split()
            name = tokens[0]
            total = 0.0;
            for i in range(1, len(tokens)) :
                try :
                    total += float(tokens[i])
                except ValueError:
                    print("Error in the hour.")
            print("Total hours worked by " + name  + " = " + str(total))
        #Step 1.1.2: Close the file
        myfile.close()
    #Step 1.2: Handle all possible exceptions that may be thrown in the try block
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Problem with the file!")
#Step 2: Call the function
name = input("Enter the full path of a file: ")
report_work_hours(name)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_work_hours2
#problem description: Suppose we have an input file that contains information about how many hours each employee of a company has worked. The file looks like the following (Employee's identification number, Employee's name, Hours):
# 101 Erica 7.5 8.5 10.25 8 8.5
# 783 Erin 10.5 11.5 12 11 10.75
# 114 Simone 8 8 8
# ...
# Construct a program that reads this file and calculates the total number of hours worked by each individual. Make sure that the program handles each specific exception that could occur. 
#Step 1: Define the function
def report_work_hours(file_name):
    #Step 1.1: Enclose the code that might throw an exception within the try block
    try :
        #Step 1.1.1: Open the file and process each line in the file
        myfile = open( file_name, "r")
        for line in myfile:
            tokens = line.split()
            #Try to get the id of the employee as a number
            try :
                eid = int(tokens[0])
            except ValueError :
                print("Error in the employee's id.")
            name = tokens[1]
            total = 0.0
            for i in range(2, len(tokens)) :
                try :
                    total += float(tokens[i])
                except ValueError:
                    print("Error in the employee's hour.")
            print("Total hours worked by " + name  + " = " + str(total))
        #Step 1.1.2: Close the file
        myfile.close()
    #Step 1.2: Handle all possible exceptions that may be thrown in the try block
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Problem with the file!")
#Step 2: Call the function
name = input("Enter the full path of a file: ")
report_work_hours(name)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_check_product_code
#problem description: Suppose a hypothetical company uses codes to represent its various products. A product code includes, among other information, a character in the tenth position that represents the zone from which that product was made. Due to some reorganization, products from zone R are banned from being sold. Construct a program that reads product codes from the user and counts the number of valid and banned codes entered. Make sure that the program handles all possible exceptions. The program must ask the user for an input until the user enters STOP.
#Step 1: Define the function
def check_product_code():
    #Step 1.1: Assign initial values to the variables that we need for counts
    valid = 0
    banned = 0
    #Step 1.2: Ask for a valid input as long as the user does'nt enter STOP; otherwise stop
    code = input("Enter product code: ")
    while ( code != "STOP") :
        #Step 1.2.1: Enclose the code that might throw an exception within the try block
        try :
            zone = code[9]
            valid += 1
            if zone == "R" :
                banned += 1
        #Step 1.2.2: Handle all possible exceptions that may be thrown in the try block
        except IndexError :
            print("Improper code length.")
        code = input("Enter product code: ")
    #Step 1.3: Print the result
    print("# of valid codes entered:", valid)
    print("# of banned codes entered:", banned)
#Step 2: Call the function
check_product_code()



#CODE_SNIPPET
#exercise type: py
#exercise name:py_check_product_code2
#problem description: Suppose a hypothetical company uses codes to represent its various products. A product code includes, among other information, a character in the tenth position that represents the zone from which that product was made, and a four-digit integer representing the district in which it will be sold. This four-digit integer begins at the 4th character and extends to the 7th character in the input code (inclusive). Due to some reorganization, products from zone R are banned from being sold in districts with a designation of 2000 or higher. Construct a program that reads product codes from the user and counts the number of valid and banned codes entered. Make sure that the program handles all possible exceptions. The program must ask the user for an input until the user enters STOP.
#Step 1: Define the function
def check_product_code():
    #Step 1.1: Assign initial values to the variables that we need for counts
    valid = 0
    banned = 0
    #Step 1.2: Ask for a valid input as long as the user does'nt enter STOP; otherwise stop
    code = input("Enter product code: ")
    while ( code != "STOP") :
        #Step 1.2.1: Enclose the code that might throw an exception within the try block
        try :
            zone = code[9]
            district = int(code[3:7])
            valid += 1
            if zone == "R" and district >= 2000:
                banned += 1
        #Step 1.2.2: Handle all possible exceptions that may be thrown in the try block
        except IndexError :
            print("Improper code length.")
        except ValueError :
            print("Error! District is not numeric.")
        code = input("Enter product code: ")
    #Step 1.3: Print the result
    print("# of valid codes entered:", valid)
    print("# of banned codes entered:", banned)
#Step 2: Call the function
check_product_code()


#CODE_SNIPPET
#exercise type: py
#exercise name: py_concat_char_two_str
#problem description: Construct a program that has a function that receives two strings and returns a string formed from the given strings such that the first character of each string is omitted. For example, the new string that will be formed from the strings 'abc' and 'xyz' is 'bcyz'. Assume that both strings have at least one character.
#Step 1: Define the function
def concat_chars(a, b):
    return a[1:] + b[1:]
#Step 2: Call the function
print(concat_chars("Hello", "There"))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_concat_char_two_str2
#problem description: Construct a program that has a function that receives two strings and returns a string formed from the given strings separated by a space character such that the first two characters of the given strings are swapped. For example, the new string that will be formed from the strings 'abc' and 'xyz' is 'xyc abz'. Assume that both strings have at least two characters.
#Step 1: Define the function
def concat_chars(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return (new_a + " " + new_b)
#Step 2: Call the function
print(concat_chars("Hello", "There"))


#CODE_SNIPPET
#exercise type: py
#exercise name: py_str_repeat_chars
#problem description: Construct a program that has a function that receives a string and creates a new string that has each character of the given string repeated two times. For example, the new string that will be formed from the string 'abc' is 'aabbcc'.
#Step 1: Define the function
def double_char(s):
    #Step 1.1: Assign initial value to the variable that we need for the new string
    new_s = ""
    #Step 1.2: Iterate through the characters in the given string
    for char in s:
        #Step 1.2.1: Add the repeated character to the the new string
        new_s += char * 2
    #String 1.3: Print the new string
    print(new_s)
#Step 2: Call the function
double_char("Hi There")



#CODE_SNIPPET
#exercise type: py
#exercise name: py_str_repeat
#problem description: Construct a program that has a function that receives a string and creates a new string that has every other character of the given string, starting with the first character, repeated two times. For example, the new string that will be formed from the string 'abcde' is 'aaccee'.
#Step 1: Define the function
def double_char(s):
    #Step 1.1: Assign initial value to the variable that we need for the new string
    new_s = ""
    #Step 1.2: Iterate through every other characters in the given string
    for i in range(0, len(s), 2) :
        #Step 1.2.1: Add the repeated character to the the new string
        new_s += s[i] * 2
    #String 1.3: Print the new string
    print(new_s)
#Step 2: Call the function
double_char("Hi There")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_str_count
#problem description: Construct a program that has a function that receives a string and returns the number of times that the string "hi" appears anywhere in the given string, ignoring the case.
#Step 1: Define the function
def count_hi(s):
    #Step 1.1: Assign initial value to the variable that we need for the counts
    count = 0
    #Step 1.2: Iterate through the characters in the given string
    for i in range(len(s)-1):
        #Step 1.2.1: Increment the counts by 1 if we find a match
        if s[i:i+2].lower() == "hi":
            count += 1
    #Step 1.3: Return the counts
    return count
#Step 2: Call the function
print(count_hi("hiabc Hi ho hIx"))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_str_count2
#problem description: Construct a program that has a function that receives a string and returns the number of times that the string "hi?t" appears anywhere in the given string where '?' could be any letter. For example, "hint" and "hilt" would count as a match. All string comparisons should be case-insensitive.
#Step 1: Define the function
def count_hi(s):
    #Step 1.1: Assign initial value to the variable that we need for the counts
    count = 0
    #Step 1.2: Iterate through the characters in the given string
    for i in range(len(s)-3):
        #Step 1.2.1: Increment the counts by 1 if we find a match
        if s[i:i+2].lower() == "hi" and s[i+3].lower() == "t":
            count += 1
    #Step 1.3: Return the counts
    return count
#Step 2: Call the function
print(count_hi("hiatc?Hi ho hIx"))



#CODE_SNIPPET
#exercise type: py
#exercise name: py_if_else_num
#problem description: Construct a program that determines whether an integer is positive, negative, or zero.
#Step 1: Read the integer
text = input("Enter an integer: ")
num = int(text)
#Step 2: Determine whether the integer is positive, negative, or zero
if num > 0 :
    print("The integer is positive.")
elif num < 0 :
    print("The integer is negative.")
else :
    print("The integer is zero.")



#CODE_SNIPPET
#exercise type: py
#exercise name: py_ifelse_odd_even
#problem description: Construct a program that determines whether an integer is even or odd
#Step 1: Read the integer
text = input("Enter an integer: ")
num = int(text)
#Step 2: Determine whether the integer is even or odd
if num % 2 == 0 :
    print("The integer is even.")
else :
    print("The integer is odd.")


#CODE_SNIPPET
#exercise type: py
#exercise name: py_range_one
#problem description: Construct a program that prints a sequence of numbers from 0 (inclusive) to 10 (exclusive).
#Step 1: Iterate through the numbers in the sequence
for num in range(10):
    #Step 1.1: Print each number in the sequence
    print(num)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_range1_2
#problem description: Construct a program that prints a sequence of numbers from 0 (inclusive) to 6 (exclusive).
#Step 1: Iterate through the numbers in the sequence
for num in range(6):
    #Step 1.1: Print each number in the sequence
    print(num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_range_three
#problem description: Construct a program that prints a sequence of numbers from 1 (inclusive) to 16 (exclusive) in increments of 4.
#Step 1: Iterate through the numbers in the sequence
for num in range(1, 15, 4):
    #Step 1.1: Print each number in the sequence
    print(num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_range3_2
#problem description: Construct a program that prints a sequence of numbers from 7 (inclusive) to 35 (inclusive) in increments of 7.
#Step 1: Iterate through the numbers in the sequence
for num in range(7, 36, 7):
    #Step 1.1: Print each number in the sequence
    print(num)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_range_two
#problem description : Construct a program that prints a sequence of numbers from 1 (inclusive) to 9 (inclusive).
#Step 1: Iterate through the numbers in the sequence
for num in range(1, 10):
    #Step 1.1: Print each number in the sequence
    print(num)
    


#CODE_SNIPPET
#exercise type: py
#exercise name: py_range2_2
#problem description: Construct a program that prints a sequence of numbers from 8 (inclusive) to 14 (inclusive).
#Step 1: Iterate through the numbers in the sequence
for num in range(8, 15):
    #Step 1.1: Print each number in the sequence
    print(num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_squares
#problem description: Construct a program to write out the squares of even positive integers less than or equal to 10.
#Step 1: Iterate through the numbers in the sequence
for num in range(2, 11, 2):
    #Step 1.1: Square and print each number in the sequence
    print(num, "squared =", num * num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_write_squares_odd
#problem description: Construct a program to write out the squares of odd positive integers less than 10.
#Step 1: Iterate through the numbers in the sequence
for num in range(1, 10, 2):
    #Step 1.1: Square and print each number in the sequence
    print(num, "squared =", num * num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_write_squares_range
#problem description: Construct a program to write out the squares of every number between 20 and 25, both inclusive.
#Step 1: Iterate through the numbers in the sequence
for num in range(20, 26):
    #Step 1.1: Square and print each number in the sequence
    print(num, "squared =", num * num)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_repeated_sequence
#problem description: Construct a program that receives an integer N from the user and prints a sequence of space-separated numbers from 1 to N such that each number in the sequence is repeated 5 times.
#Step 1: Read the integer N that the user enters
N = int(input("Enter the integer N: "))
#Step 2: Print N space-separated numbers
for i in range(1, N+1):
    #Step 2.1: Print the i-th number five times
    for j in range(1, 6):
        print(i)


#CODE_SNIPPET
#exercise type: py
#exercise name: py_repeated_sequence2
#problem description: Construct a program that receives an integer N from the user and prints a sequence of space-separated numbers from 1 to N such that the N-th number in the sequence is repeated N times.
#Step 1: Read the integer N that the user enters
N = int(input("Enter the integer N: "))
#Step 2: Print N space-separated numbers
for i in range(1, N+1):
    #Step 2.1: Print the i-th number i times
    for j in range(1, i+1):
        print(i)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_star_patterns
#problem description: 
#A Right triangle star pattern contains N asterisks in N-th row. Construct a program that receives the number of rows in the right triangle star pattern and prints that triangle. For example, when the number of rows in the right triangle star pattern is 5, the program prints the following output:
#*
#**
#***
#****
#*****
#Step 1: Read the number of rows in the right triangle star pattern
N = int(input("Enter the number of rows in the right triangle star pattern: "))
#Step 2: Print the rows in the star pattern, one by one
for i in range(1, N+1):
    #Step 2.1: Generate the asterisks in the i-th row
    row = ""
    for j in range(1, i+1):
        row = row + "*"
    #Step 2.2: Print the asterisks in the i-th row
    print(row)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_stars_2
#problem description: An inverted right triangle star pattern of N rows contains N-i+1 asterisks in the i-th row. Construct a program that receives the number of rows in the inverted right triangle star pattern and prints that triangle. For example, when the number of rows in the inverted right triangle star pattern is 5, the program prints the following output:
#*****
#****
#***
#**
#*
#Step 1: Read the number of rows in the inverted right triangle star pattern
N = int(input("Enter the number of rows in the inverted right triangle star pattern:"))
#Step 2: Print the rows in the star pattern, one by one
for i in range(1, N+1):
    #Step 2.1: Generate the asterisks in the i-th row
    row = ""
    for j in range(1, N-i+2):
        row = row + "*"
    #Step 2.2: Print the asterisks in the i-th row
    print(row)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_divisor
#problem description: Construct a program that finds the smallest divisor (other than 1) of a positive number. For example, the smallest divisor of 4 is 2.
#Step 1: Assign initial values to the variables which we need for this program
num = 15
divisor = 2
#Step 2: Find the smallest divisor of the number
while num % divisor != 0 :
    divisor += 1
print("The smallest divisor of", num, "is", divisor)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_largest_divisor
#Problem description: Construct a program that finds the largest divisor of a positive number, excluding the number itself. For example, the largest divisor of 24 is 12.
#Step 1: Assign initial values to the variables which we need for this program
num = 15
divisor = num-1
#Step 2: Find the largest divisor of the number
while num % divisor != 0 :
    divisor -= 1
print("The largest divisor of", num, "is", divisor)



#CODE_SNIPPET
#exercise type: py
#exercise name: py_input
#problem description: Construct a program that receives an integer from the user, outputs that integer, and stops receiving integers when the user enters a negative integer.
#Step 1: Read the first integer that the user enters
text = input("Enter an integer:")
num = int(text)
#Step 2: Print the integer that the user has entered, then receive the next integers as long as the user enters an integer that is not negative;; otherwise stop
while num >= 0 :
    print("The integer entered is:", num)
    text = input("Enter an integer:")
    num = int(text)
print("End of input.")



#CODE_SNIPPET
#exercise type: py
#exercise name: py_input2
#problem description: Construct a program that receives an integer from the user, outputs that integer, and stops receiving integers when the user enters an integer that is not in the range of 30 to 90 both inclusive.
#Step 1: Read the first integer that the user enters
text = input("Enter an integer:")
num = int(text)
#Step 2: Print the integer that the user has entered, then receive the next integers as long as the user enters an integer that is in the range of 30 to 90 both inclusive; otherwise stop
while num >= 30 and num <= 90 :
    print("The integer entered is:", num)
    text = input("Enter an integer:")
    num = int(text)
print("End of input.")



#CODE_SNIPPET
#exercise type: py
#exercise name:  py_input3
#problem description: Construct a program that receives an integer from the user, outputs that integer, and stops receiving integers when the user enters a negative integer or an integer greater than 1000.
#Step 1: Read the first integer that the user enters
text = input("Enter an integer:")
num = int(text)
#Step 2: Print the integer that the user has entered, then receive the next integers as long as the user enters an integer that is not negative and is not greater than 1000; otherwise stop
while num >= 0 and num <= 1000 :
    print("The integer entered is:", num)
    text = input("Enter an integer:")
    num = int(text)
print("End of input.")



#CODE_SNIPPET
#exercise type: py
#exercise name: py_input4
#problem description: Construct a program that receives an integer from the user, outputs that integer, and stops receiving integers when the user enters an even integer less than 10.
#Step 1: Read the first integer that the user enters
text = input("Enter an integer:")
num = int(text)
#Step 2: Print the integer that the user has entered, then receive the next integers as long as the user enters an integer that is not even or is not less than 10; otherwise stop
while num % 2 != 0 or num >= 10 :
    print("The integer entered is:", num)
    text = input("Enter an integer:")
    num = int(text)
print("End of input.")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_hello
#problem description: Construct a program that prints out hello and world on separate lines.
print("hello")
print("world")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_simple_function
#problem description : Construct a program that prints out Hello functions.
def func():
    print("Hello functions!")
func()



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_simple_params
#problem description: Construct a program that prints out 3
#problem description: 
def add_two(a):
    return a+2
print(add_two(1))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_return_bigger_or_none
#problem description: Construct a function that returns the bigger value of the given arguments. If a and b are equal, it should return None.
def return_bigger_or_none(a,b):
    if a < b:
        return b
    elif a > b:
        return a
    pass
    return None



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_addition
#problem description: Construct a program that prints the value 8.
first = 3
first = first + 1
first = first + first
print(first)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_iteration_addition
#problem description: Construct a program that prints the value 8.
i = 0
while i < 7:
    i = i + 2
print(i)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_iteration_multiplication
#problem description: Construct a program that prints values 1,2,4,8 and finally prints "The end!".
value = 1
while value < 9:
    print(value)
    value = value * 2
print("The end!")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_calculate_function
#problem description: Define a function that returns the second value multiplied by two and added by the first value. The program should print 23 at the end.
def calculate(first, second):
    return second * 2 + first
result = calculate(3, 2)
print(calculate(result, result + 1))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_calls
#problem description: First define a calculate function and then define double function (that returns the given value doubled). Then write a program that first prints out 20 and then 36.
def calculate(first, second):
    return second * 3 + first
def double(value):
    return value * 2
print(double(double(5)))
print(calculate(double(3), 2 + calculate(5, 1)))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_recursive_factorial
#problem description: Define a function that returns the factorial of a given positive integer.
def factorial(n):
    if n < 3:
        return n
    else:
        return factorial(n-1) * n


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_class_person
#problem description: Write a program that will print out "Safiira. Nice to meet you!"
class Person:
    def __init__(self, firstname, profession):
        self.__name = firstname
    def greet(self):
        return self.__name + ". Nice to meet you!"
safira = Person("Safiira", "biologist")
print(safira.greet())



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_modulo_is_even
#problem description: Construct a function that will return True if a given number is even, otherwise false.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_iteration_zoo
#problem description: Construct a program that prints out all the animals in the zoo-variable.
zoo = ["bear", "lion", "camel"]
for animal in zoo:
    print(animal)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_lists_indexing
#problem description: Construct a program that first prints out [[1, 2, 3], [4, 5, 6]], then [4, 5, 6], and finally 6.
some_list = [[1, 2, 3], [4, 5, 6]]
print(some_list)
print(some_list[1])
print(some_list[1][2])



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_string_indexing
#problem description: Construct a program that first prints out strings "Py", "th", "o", and "n"
word = "Python"
print(word[:2])
print(word[2:4])
print(word[-2])
print(word[5:])



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_dict_keys
#problem description: storage-dictionary stores the amount of certain items in storage. Construct a program that prints out a list of all the items that there are more than one currently stored.
storage = {"cup": 7, "pen": 0, "lamp": 4}
for item in storage:
    if storage[item] > 0:
        print(item)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_dict_values
#problem description: Construct a program that prints out how many items in total are in storage. You can assume that a dictionary called storage has already been initialized.
total_items = 0
for item_count in storage.values():
    total_items += item_count
print(total_items)


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_to_dict
#problem description: Construct a program that prints out moo and oink, in that order.
pairs = [("pig", "oink"), ("cow", "moo")]
animals = dict(pairs)
print(animals.get("cow"))
print(animals.get("pig"))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_dict_filter
#problem description: Construct a program that prints out all the circles that are larger than 5.
circles = {"blue": 8, "red": 5, "grey": 7}
for circle in circles.items():
    if(circle[1] > 5):
        print(circle[0], "circle is larger than", 5)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_bigger_than
#problem description: Assume that num1 and num2 have been initialized to numbers, so that number1 is bigger. Construct a program that correctly prints out that number1 is indeed bigger
print("num1 is bigger:", num1 > num2)


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_conditionals_temperature
#problem description: Construct a program that prints out 'Cold', when the temperature is 15 degrees celcius or below, 'Moderate' when it is over 15 degrees but no more than 25 degrees, and 'Hot' when the temperature is over 25 degrees.
if temperature <= 15:
    print("Cold")
elif temperature > 15:
    if temperature <= 25:
        print("Moderate")
    else:
        print("Hot")


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_printing_file_contents
#problem description: Construct a program that opens up a file and prints out each line of the file
try:
    file_to_read = open(filename, "r")
    row = file_to_read.readline()
    while row != "":
        print(row)
        row = file_to_read.readline()
    file_to_read.close()
except OSError:
    print("Error reading the file. The program execution ends.")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_try_except
#problem description: Construct a program that prints out various Celcius temperatures in Fahrenheit.
def centigrade_to_fahrenheit(temp):
    try:
        if temp < -273.15:
            raise ValueError("Temperature below absolute zero!")
        return temp*1.8+32
    except ValueError:
        print("Temperature set impossibly low!")
print(centigrade_to_fahrenheit(temp_to_convert))


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_ifs
#problem description: Construct a program that prints out a sentence depending on the time of day. Night is considered to be before 7 a.m., morning is from 7 a.m. until noon, afternoon is until 5 p.m. and rest is considered evening.
if am_or_pm == "am":
    if hour < 7:
        print("It is still night")
    else:
        print("It is morning")
elif am_or_pm == "pm":
    if hour <= 5:
        print("It is afternoon")
    else:
        print("It is evening")


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_comparisons
#problem description: Construct a program that prints out whether variable a is bigger than b.
a_is_bigger = a > b
print(a_is_bigger)


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_add_to_list
#problem description: Construct a function that adds a given amount to all items in a list.
def add_to_list_items(alist, amount):
    for x in range(len(alist)):
        alist[x] += amount


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_swap
#problem description: Construct a program that swaps the values of x and y variables.
tmp = x
x = y
y = tmp


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_xor
#problem description: Construct a program that mimics a XOR gate (exclusive or). When input_a and input_b are the same, it should print out 0 and in other cases print out 1.
if input_a == 1 and input_b == 1:
    print(0)
elif input_a == 0 and input_b == 0:
    print(0)
else:
    print(1)


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_for_odd_or_even
#problem description: Construct a program that goes through a list of numbers and prints out whether they are odd or even.
for number in some_list:
    if number%2 == 0:
        print("Even")
    else:
        print("Odd")


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_string_join
#problem description: Construct a program that prints out a sentence from a given list of words.
words = ["this", "is", "a", "sentence"]
sentence = " ".join(words)
print(sentence.capitalize() + ".")


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_try_adding
#problem description: Construct a function that adds two numbers together and handles non-numeric input.
def add_two_numbers(a,b):
    try:
        return a + b
    except TypeError:
        print("Can only add numbers together.")


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_class_point
#probem description: Construct a class Point which has a method to tell distance from another instance of Point.
from math import sqrt
class Point:
    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y
    def distance_from(self, another_point):
        x_dist = self.x - another_point.x
        y_dist = self.y - another_point.y
        return sqrt(x_dist * x_dist + y_dist * y_dist)


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_2d_list
#problem description: Construct a program that prints out [[0, 1, 2], [3, 4, 5], [6, 7, 99]]
COUNT = 3
list1 = []
for i in range(COUNT):
    list2 = [0] * COUNT
    for j in range(COUNT):
        list2[j] = i * COUNT + j
    list1.append(list2)
list1[2][2] = 99
print(list1)


#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_loops
#problem description: Construct a program that first prints out 15, then 14, then 12, then 9 and finally 5 on consecutive lines.
MAX = 5
i = 0
while i < MAX:
    sum = 0
    j = MAX
    while j > i:
        sum = sum + j
        j = j - 1
    print(sum)
    i = i + 1