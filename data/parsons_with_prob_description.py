#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_hello
#problem description: Construct a program that prints out hello and world on separate lines.
print("hello")
print("world")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_simple_function
#problem description: Construct a program that prints out Hello functions.
def func():
	print("Hello functions!")
func()



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_simple_params
#problem description: Construct a program that prints out 3
def add_two(a):
	return a+2
print(add_two(1))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_return_bigger_or_none
#problem description: Construct a function that returns the bigger value of the given arguments. If a and b are equal, it should return None.
pass
def return_bigger_or_none(a,b):
return a
if a <span class="jsparson-toggle" data-type="ab"></span> b:
return b
elif a <span class="jsparson-toggle" data-type="ab"></span> b:
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
print("num1 is bigger:", num1 < num2) #distractor



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_conditionals_temperature
#problem description: Construct a program that prints out 'Cold', when the temperature is 15 degrees celcius or below, 'Moderate' when it is over 15 degrees but no more than 25 degrees, and 'Hot' when the temperature is over 25 degrees.
if temperature  $$toggle::<::>::<=::>=$$ $$toggle::15::25$$:
if temperature  $$toggle::<::>::<=::>=$$ $$toggle::15::25$$:
print("Cold")
elif temperature $$toggle::<::>::<=::>=$$ $$toggle::15::25$$:
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
	if temp < -273.15:
		raise ValueError("Temperature below absolute zero!") 
	return temp*1.8+32
try:
	print(centigrade_to_fahrenheit(temp_to_convert))
except ValueError:
	print("Temperature set impossibly low!")



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
a_is_bigger = a $$toggle::<::>::<=::>=$$ b
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
$$toggle::x::y::tmp$$ = $$toggle::x::y::tmp$$
$$toggle::x::y::tmp$$ = $$toggle::x::y::tmp$$
$$toggle::x::y::tmp$$ = $$toggle::x::y::tmp$$



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_xor
#problem description: Construct a program that mimics a XOR gate (exclusive or). When input_a and input_b are the same, it should print out 0 and in other cases print out 1.
if input_a == 1 $$toggle::and::or::not::$$ input_b == 1:
	print($$toggle::0::1::$$)
elif input_a == 0 $$toggle::and::or::not::$$ input_b == 0:
	print($$toggle::0::1::$$)
else:
	print($$toggle::0::1::$$)



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
#problem description: Construct a class Point which has a method to tell distance from another instance of Point.
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



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_3digit_combinations
#problem description: Construct a program which creates and prints all three-digit combinations from numbers 1-4 such that each number appears at most once and the combinations are listed from the smallest to the greatest. The program must also output the total number of the combinations. For example, output 123, 124, 132 ... total: 24.
amount = 0
i = 0
while i < 4:
  i += 1
  j = 0
  while j < 4:
    j += 1
    k = 0
    while k < 4:
      k += 1
      if k != i and k != j and i != j:
          amount += 1
          print(i, j, k)

print("The total number of 3 digit combinations is", amount)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_3digit_combinations2
#problem description: Construct a program which creates and prints all three-digit combinations from numbers 1-4 such that each number appears at most once and the combinations are listed from the smallest to the greatest. The program must also output the total number of the combinations. For example, output 123, 124, 132 ... total: 24.
amount = 0
i = 0
while i < 4:
  i += 1
  j = 0
  while j < 4:
    j += 1
    k = 0
    while k < 4:
      k += 1
      if k != i $$toggle::and::or::not::$$ k != j $$toggle::or::and::not::$$ i != j:
          amount += 1
          print(i, j, k)

print("The total number of 3 digit combinations is", amount)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_divsible_by1
#problem description: Construct a program which checks whether each of the integers in interval from 1 to 100 is divisible by 2, 5, or both.
def divisible_by(num):
    for i in range(1, num + 1):
        if i % 2 == 0 and i % 5 == 0:
            print(i, "is divisible by 2 & 5")
        elif i % 5 == 0:
            print(i, "is only divisible by 5")
        elif i % 2 == 0:
            print(i, "is only divisible by 2")
        else:
            print(i, "is not divisible by 2 nor 5")

divisible_by(100)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_divisible_by2
#problem description: Construct a program which checks whether each of the integers in interval from 1 to 100 is divisible by 2, 5, or both.
num = 100
for i in range(1, num + 1):
    if i % 2 == 0 and i % 5 == 0:
        print(i, "is divisible by 2 & 5")
    elif i % 5 == 0:
        print(i, "is only divisible by 5")
    elif i % 2 == 0:
        print(i, "is only divisible by 2")
    else:           
        print(i, "is not divisible by 2 nor 5")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_divisible_by3
#problem description: Construct a program which checks which of the integers in interval from 1 to 50 is divisible by only 2, only 5, or both. The program should store each group in its own list and finally print the lists in this order.
num = 50
list = []
list2= []
list3= []
    
for i in range(1, num + 1):
    if i % 2 == 0 and i % 5 == 0:
        list.append(i)
    elif i % 2 == 0:
        list2.append(i)
    elif i % 5 == 0:
        list3.append(i)
print("divisible by only 2:")
print(list)
print("divisible by only 5:")
print(list2)
print("divisible by 2 & 5:")
print(list3)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_freq_of_char1
#problem description: Construct a function which counts the frequency of each character in the string given as a parameter and returns a dictionary containing the fequencies.
def freq_of_char(str):
    num_of_char = {}
    for letter in str:
        if letter in num_of_char:
            num_of_char[letter] += 1
        else:
            num_of_char[letter] = 1
    return num_of_char



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_freq_of_char2
#problem description: Construct a program which counts the frequency of each character in string 'Summer' and stores it in a dictionary. Finally, the program should print the dictionary.
str = "Summer"
num_of_char = {}
for letter in str:
    if letter in num_of_char:
        num_of_char[letter] += 1
    else:
        num_of_char[letter] = 1

print(num_of_char)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_palindrome1
#problem description: Construct a function which determines whether the string given as a paramter is a palindrome. The function should be case insensitive i.e. upper and lowercase letters are intepreted as being the same.
def is_palindrome(str):
    n_str = str.lower()
    revers_str = ""
    for char in n_str:
        revers_str = char + revers_str
    if n_str == revers_str:
            print("This string is a palindrome!")
    else:
        print("The string is not a palindrome!")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_palindrome2
#problem description: Construct a program which determines whether the original string is a palindrome. The function should be case insensitive i.e. upper and lowercase letters are intepreted as being the same.
str = "Madam"
n_str = str.lower()
revers_str = ""
for char in n_str:
    revers_str = char + revers_str
if n_str == revers_str:
    print("This string is a palindrome!")
else:
    print("The string is not a palindrome!")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_palindrome3
#problem description: Construct a function which determines whether the string given as a paramter is a palindrome. The function should be case insensitive i.e. upper and lowercase letters are intepreted as being the same.
def is_palindrome(str):
    n_str = str.lower()
    revers_str = ""
    for char in n_str:
        revers_str = char + revers_str
    if n_str == revers_str:
        return True
    else:
        return False



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_palindrome4
#problem description: Construct a function that checks if the string is a palindrome or not. The function should be case insensitive i.e. upper and lowercase letters are intepreted as being the same
def is_palindrome(str):
    i = 0
    j = len(str) - 1
    n_str = str.lower()
    while i < j:
        if n_str[i] != n_str[j]:
            return False
        i += 1
        j -= 1
    return True



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_of_remainders1
#problem description: Construct a function which calculates the remainder of each element of the first list and the element with the same index in the second list. The remainders are stored in a new list. If the number in the second list is 0, the function should directly add number 2 to the new list instead of the remainder.
def list_of_remainders(list1, list2):
    new_list = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list2[i] == 0:
                new_list.append(2)
            else:
                result = list1[i] % list2[i]
                new_list.append(result)
    return new_list

list1 = [19, 3, 4, 2]
list2 = [4, 2, 1, 0]
print(list_of_remainders(list1, list2))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_of_remainders2
#problem description: Construct a program which calculates the remainder of each element of the first list and the element with the same index in the second list. The remainders are stored in a new list. If the number in the second list is 0, the program should directly add number 2 to the new list instead of the remainder. Finally, the program should print the new list.
list1 = [19, 3, 4, 2]
list2 = [4, 2, 1, 9]

new_list = []
if len(list1) == len(list2):
    for i in range(len(list1)):
        if list2[i] == 0:
            new_list.append(2)
        else:
            result = list1[i] % list2[i]
            new_list.append(result)

print(new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse1
#problem description: Construct a program which creates a new list that is reverse of list [1, 2, 3, 4, 5].
def list_reverse(lst):
    new_list = []
    i = 0
    while i < len(lst):
        element = lst[i]
        new_list.insert(0, element)
        i += 1
    return new_list


list1 = [1, 2, 3, 4, 5]
list2 = list_reverse(list1)
print(list2)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse2
#problem description: Construct a program which creates a new list that is the reverse of the orginal list.
list1 = [1, 2, 3, 4, 5]
new_list = []
i = 0
while i < len(list1):
    element = list1[i]
    new_list.insert(0, element)
    i += 1
print(new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse3
#problem description: Construct a program which creates a new list that is reverse of list [1, 2, 3, 4, 5].
def list_reverse(lst):
    new_list = [0] * len(lst)
    i = 0
    j = len(lst) - 1
    while i < len(lst):
        j = j - 1
        new_list[j] = lst[i]
        i += 1
    return new_list

list1 = [1, 2, 3, 4, 5]
list2 = list_reverse(list1)
print(list2)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse4
#problem description: Construct a program which creates a new list that is the reverse of the orginal list.
list1 = [1, 2, 3, 4, 5]
new_list = [0] * len(list1)
i = 0
j = len(list1) - 1
while i < len(list1):
    j = j - 1
    new_list[j] = list1[i]
    i += 1
print(new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse5
#problem description: Construct a program which creates a new list that is reverse of list [1, 2, 3, 4, 5].
def list_reverse(lst):
    new_list = [0] * len(lst)
    j = len(lst) - 1
    for i in range(len(lst)):
        j = j - 1
        new_list[j] = lst[i]
    return new_list

list1 = [1, 2, 3, 4, 5]
list2 = list_reverse(list1)
print(list2)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse6
#problem description: Construct a program which creates a new list that is the reverse of the orginal list.
list1 = [1, 2, 3, 4, 5]
new_list = [0] * len(list1)
j = len(list1)
for i in range(len(list1)):
    j = j - 1
    new_list[j] = list1[i]
    print(new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse7
#problem description: Construct a program which creates a new list that is reverse of list [1, 2, 3, 4, 5].
def list_reverse(lst):
    new_list = [0] * len(lst)
    j = len(lst)
    for number in lst:
        j = j - 1
        new_list[j] = number 
    return new_list

list1 = [1, 2, 3, 4, 5]
list2 = list_reverse(list1)
print(list2)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse8
#problem description: Construct a program which creates a new list that is the reverse of the orginal list.
list1 = [1, 2, 3, 4, 5]
new_list = [0] * len(list1)
j = len(list1)
for number in list1:
    j = j - 1 
    new_list[j] = number
print(new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_sum_of_two1
#problem description: Construct a function which determines whether one of the paraters is the sum of the two other parameters.
def sum_of_two(x, y, z):
    if x + y == z $$toggle::and::or::not$$ x + z == y $$toggle::and::or::not$$ y + z == x:
        return True
    else:
        return False



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_sum_of_two2
#problem description: Construct a program which determines whether the value of one of variables x, y, and z is the sum of the values of the two other variables.
if x + y == z $$toggle::and::or::not$$ x + z == y $$toggle::and::or::not$$ y + z == x:
    print("True")
else:
    print("False")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square1
#problem description: Construct a function which finds even numbers from the list given as a parameter, calculates the square of each such number and adds the squares to a new list. The function should return the new list.
def find_and_square(lst):
    new_list = []
    i = 0
    while i < len(lst):
        num = lst[i]
        if num % 2 == 0:
            new_list.append(num * num)
        i += 1
    return new_list



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square2
#problem description: Construct a program which finds even numbers from the original list, calculates the square of each such number and adds the squares to a new list. The program should print the new list.
list1 = [1, 2, 3, 4, 5]
new_list = []
i = 0
while i < len(list1):
    num = list1[i]
    if num % 2 == 0:
        new_list.append(num * num)
    i += 1
print(new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square3
#problem description: Construct a function which finds even numbers from the list given as a parameter, calculates the square of each such number and adds the squares to a new list. The function should return the new list.
def find_and_square(lst):
    new_list = []
    for i in range(len(lst)):
        num = lst[i]
        if num % 2 == 0:
            new_list.append(num * num)
    return new_list



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square4
#problem description: Construct a function which finds even numbers from the list given as a parameter, calculates the square of each such number and adds the squares to a new list. The function should return the new list.
def find_and_square(lst):
    new_list = []
    for i in lst:
        num = i
        if num % 2 == 0:
            new_list.append(num * num)
    return new_list



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square5
#problem description: Construct a program which finds even numbers from the original list, calculates the square of each such number and adds the squares to a new list. The program should print the new list.
list1 = [1, 2, 3, 4, 5]
new_list = []
for i in range(len(list1)):
    num = list1[i]
    if num % 2 == 0:
        new_list.append(num * num)
print(new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square6
#problem description: Construct a program which finds even numbers from the original list, calculates the square of each such number and adds the squares to a new list. The program should print the new list.
list1 = [1, 2, 3, 4, 5]
    new_list = []
    for i in list1:
        num = i
        if num % 2 == 0:
            new_list.append(num * num)
    print(new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_easy_power1
#problem description: Construct a function which takes the base and the exponent as parameters and returns the base raised to the exponent. Call the function to calculate 2 raised to the power of 5.
def power(base, exp):

    result = 1
    i = 1
    while i $$toggle::<::>::<=::>=$$ exp:
        result = result * base
        i += 1

    return result

new_num = power(2, 5)
print(new_num)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_easy_power2
#problem description: Construct a program which calculates the base raised to the power of the non-negative exponent.
base = 2
exp = 5
if exp == 0 and base == 0 or exp < 0:
    print("Error!")
else:
    result = 1
    i = 1
    while i <= exp:
        result = result * base
        i += 1
    print(result)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_fast_power1
#problem description: Construct a program which calculates the base raised to the power of the exponent.
base = 2
exp = 5
temp = 1
while exp > 0:
    if exp % 2 == 0:
        base = base * base
        exp = exp // 2
    else:
        temp = base * temp
        exp = exp - 1
result = temp
print(result)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_fast_power2
#problem description: Construct a function which calculates the power of a number. The function takes two integers as parameters (the base number and a non-negative exponent) and calculates the power.
def power(base, exp):
    temp = 1.0
    while exp > 0:
        if exp % 2 == 0:
            base = base * base
            exp = exp // 2
        else:
            temp = base * temp
            exp = exp - 1
    result = temp
    return result



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_power_with_loops1
#problem description: Construct a function which takes a base and a non-negative exponent as parameters and calculates the base raised to the power of the exponent without using multiplication.
def power(base, exp):
    if exp == 0:
        return 1

    result = base
    temp = base

    for i in range(1, exp):
        for j in range(1, base):
            result += temp
        temp = result
    return result



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_power_with_loops2
#problem description: Construct a program that calculates the base raised to the power of the non-negative exponent without using multiplication.
base = 2
exp = 5

if(exp == 0):
    print(1)

else:
    result = base
    temp = base

    for i in range(1, exp):
        for j in range (1, base):
            result += temp
        temp = result
    print(result)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_remove_dublicates
#problem description: Construct a function which creates a new list where it stores all elements except the duplicates from the list given as a parameter. Finally, the function should return a new list.
def remove_dup(list_of_num):
    new_list = []
    for element in list_of_num:
        if element not in new_list:
            new_list.append(element)
    return new_list



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_remove_dublicates2
#problem description: Construct a program which creates a new list where it stores all elements except the duplicates from the original list. Finally, the program should print the original list and the new list.
new_list = []
for element in old_list:
    if element not in new_list:
        new_list.append(element)

print("The original list:", old_list)
print("The new list:", new_list)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_even_first1
#problem description: Construct a program which partition the original list of integers such that all even numbers come first and all odd numbers come after them.
list_num = [7, 2, 4, 1, 3, 5, 6, 8]
i = 0
j = len(list_num) - 1
while i < j:
    while i <= j and list_num[i] % 2 == 0:
        i += 1
    while i <= j and list_num[j] % 2 != 0:
        j -= 1
    if i < j:
        temp = list_num[i]
        list_num[i] = list_num[j]
        list_num[j] = temp

print(list_num)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_even_first2
#problem description: Construct a function which partition the original list of integers such that all even numbers come first and all odd numbers come after them.
def even_first(num_list):
    i = 0
    j = len(num_list) - 1
    while i < j:
        while i < j and num_list[i] % 2 == 0:
            i += 1
        while i < j and num_list[j] % 2 != 0:
            j -= 1
        if i < j:
            temp = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = temp
    return num_list



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_even_first3
#problem description: Construct a function which partition the list of integers given as a parameter such that all even numbers come first and all odd numbers come after them.
def even_first(num_list):
    result = []
    odds = []
    for n in num_list:
        if n % 2 == 0:
            result.append(n)
        else:
            odds.append(n)

    for i in range(len(odds)):
        result.append(odds[i])
    return result



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_even_first4
#problem description: Construct a program which partition the original list of integers such that all even numbers come first and all odd numbers come after them.
lst = [8, 3, 2, 5, 7, 5, 6]
result = []
odds = []
for n in lst:
    if n % 2 == 0:
        result.append(n)
    else:
        odds.append(n)

for i in range(len(odds)):
    result.append(odds[i])
print(result)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_file_reading_third_element
#problem description: Construct a program that opens up a file and prints out the third element in each line of the file
try:
	myfile=open(filename, "r")
	linenum=1
	for line in myfile:
		words = line.split()
		word=words[2]
		print("The third word in line",linenum,"is",word)
		linenum+=1
except OSError:
	print("Error reading the file.")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_math_library
#problem description: Construct a program that accesses math.pi and check its type
import math
a = math.pi
print(type(a) is int)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_data_type
#problem description: Construct a program that calculate two variables' modulus and check the type of the modulus
a, b = 7.0, 5.0
c = a % b
print(type(c))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_whiles
#problem description: Construct a program to print an upside-down right triangle. Assume that 'size' is defined, and holds an integer value.
while size > 0:
	m=0
	while m < size:
		print("*",end="")
		m=m+1
	size=size-1
	print()



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_loop_2
#problem description: Construct a program to print a multiplication chart given the chart_size. Assume that chart_size is set to a positive integer.
j = 1
while j < chart_size + 1:
	for i in range(1, chart_size + 1):
		print(i * j, " ", end = "")
	print()
	j += 1



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_class_inheritance
#problem description: Construct a program using inheritance of classes to display a student’s name and score. Consider student as an instance of class Score.
class Student():
	def __init__(self, name):
		self.name=name
	def getName(self):
		return self.name
class Score(Student):
	def __init__(self, name, score):
		self.score=score
		Student.__init__(self,name)
	def getScore(self):
		return self.score



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_print_specific_element
#problem description: Construct a program that prints a blue Toyota car.
car = cardict["brand"]
color = cardict["colors"]
print("The car"s brand is", car[2],"and it is",color[2] )



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_calculation_in_dictionary
#problem description: Construct  a program that calculates each student’s average score by using `studentdict` dictionary that is already defined as follows:
for item in studentdict.items():
	name=item[0]
	scores=item[1]
	total=0
	for score in scores:
		total+=score
	ave = total/len(scores)
	print("The average score of",name, "is",ave)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_add_to_list_2
#problem description: Construct a function that add k values to the given list. The added values is k's increment (increment by 1) in each iteration.
def add(alist,k):
	for i in range(k):
		alist.append(k)
		k=k+1
	return alist



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_search_min_index
#problem description: Construct a program that finds the index of the minimum element in a list. num_list is a test case where you need to find the min index from. The program then needs to print the index of the minimum element.
index_min = 0
for index in range(1,len(num_list)):
	if (num_list[index] < num_list[index_min]):
		index_min = index
print(index_min)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_search_min_max_index
#problem description: Construct a program that finds the indexes of both the max and min elements in a list. num_list is a test case where you need to find the min and max indexes from. The program then needs to print the index of the minimum and the maximum elements. This program does not need to consider duplicate elements.
index_min = 0
index_max = 0
for index in range(1, len(num_list)):
	if num_list[index] < num_list[index_min]:
		index_min = index
	if num_list[index] > num_list[index_max]:
		index_max = index
print(index_min, index_max)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_stack
#problem description: Construct a program that creates two functions in a  Stack Structure. The first one is "push" function and the second one is "pop" function. Your pop function should also check if the current stack is empty. is_empty() is a predefined function.
def push(self, item):
	self.items.insert(0, item)
def pop(self):
	if self.is_empty():
		print("error stack is empty")
	else:
		return self.items.pop(0)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_queue
#problem description: Construct a function that uses Queue Structure to solve a Josephus problem that removes the kth element in a given list and returns the last left element. All Queue's functions are predefined (is_empty(), enqueue() and dequeue()). Your function should also return a "The list is empty" message if the given list is empty.
def circle(k,name_list):
	q = Queue()
	if not q.is_empty():
		for i in range(len(name_list)):
			q.enqueue(name_list[i])
		i = 1
		while q.size()!=1:
			temp=q.dequeue()
			if i != k+1:
				q.enqueue(temp)
			else:
				i = 0
			i += 1
	else:
		return (\'the list is empty!\')
	return q.dequeue()



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_linked_list_traversal
#problem description: Construct a function that prints all elements of a Doubly Linked List in forwards and then reverse order.<br/>DoublyLinkedList class implementation is given below.
def traverse_list(doubly_linked_list):
  current = doubly_linked_list.head
  while current:
    print(current.data, end=" ")
    last = current
    current = current.next
  while last:
    print(last.data, end=" ")
    last = last.prev



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_linked_list_size
#problem description: Construct a function that calculates the number of elements in a singly linked list.<br/>LinkedList class implementation is given below.
def get_size(linked_list):
	count = 0
	temp = linked_list.head
	while temp:
		count = count + 1
		temp = temp.next
	return count



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_merge_sort
#problem description: Construct a merge function that recursively splits a numeric array and takes a list as a parameter called data.<br/>Consider that merge_sort() function is already defined and given below.
def merge(data):
	if len(data) <= 1:
		return data
	middle = len(data)//2
	left = merge(data[:middle])
	right = merge(data[middle:])
	return merge_sort(left, right)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_quick_sorting
#problem description: Construct a function that implements quick sort algorithm. The partition() function has been pre defined and displayed below.<br/>Consider data is a list, first is the first element's index and last is the last element's index
def quick_sort(data, first, last):
	if first < last:
		pivot = partition(data, first, last)
		quick_sort(data, first, pivot-1)
		quick_sort(data, pivot+1, last)
	return data



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_tree_inorder_traversal
#problem description: Construct an inorder traversal function that recursively traverse a tree from left node, root node and right node. We store the traversed tree in a list called res=[]. The traversal function is inside of the tree class. Consider the tree class has been predefined.
def inorder_traversal(self, root):
	res = []
	if root:
		res = self.inorder_traversal(root.left)
		res.append(root.data)
		res = res + self.inorder_traversal(root.right)
	return res



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_tree_preorder_traversal
#problem description: Construct a preorder traversal function that recursively traverse a tree from root node, left node and right node. We store the traversed tree in a list called res=[]. The traversal function is inside of the tree class. Consider the tree class has been predefined.
def preorder_traversal(self, root):
	res = []
	if root:
		res.append(root.data)
		res = res + self.preorder_traversal(root.left)
		res = res + self.preorder_traversal(root.right)
	return res



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_csedpad_java_tallest_person
#problem description: Find the tallest among three individuals whose heights are given.
public class TallestPerson{
	public static void main(String[] args) {
		int Mary = 140, Lisa = 150, Rose = 140;

		if( Mary >= Lisa && Mary >= Rose)
			System.out.println(" Mary is the tallest");
		else if (Lisa >= Mary && Lisa >= Rose)
			System.out.println("Lisa is the tallest");
		else
			System.out.println("Rose is the tallest");
	}
}



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_hello_es
#problem description: Construye un programa que imprima hola y mundo en lineas separadas.
print("hola")
print("mundo")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_simple_function_es
#problem description: Construye un programa que imprima Hola funciones.
def funcion():
	print("Hola funciones!")
funcion()



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_simple_params_es
#problem description: Construye un programa que imprima 3
def sumar_dos(numero):
	return numero+2
print(sumar_dos(1))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_return_bigger_or_none_es
#problem description: Construye una funcion que devuelva el valor mayor de los argumentos dados. Si a y b son iguales, debe devolver None.
pass
def devolver_mayor_o_none(a,b):
return a
if a <span class="jsparson-toggle" data-type="ab"></span> b:
return b
elif a <span class="jsparson-toggle" data-type="ab"></span> b:
return None



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_addition_es
#problem description: Construye un programa que imprima el valor 8.
primero = 3
primero = primero + 1
primero = primero + primero
print(primero)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_iteration_addition_es
#problem description: Construye un programa que imprima el valor 8.
i = 0
while i < 7:
  i = i + 2
print(i)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_iteration_multiplication_es
#problem description: Construye un programa que imprima los valores 1,2,4,8 y finalmente imprima "El fin!".
valor = 1
while valor < 9:
  print(valor)
  valor = valor * 2
print("El fin!")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_calculate_function_es
#problem description: Define una funcion que devuelva el segundo valor multiplicado por dos y sumado al primer valor. El programa debe imprimir 23 al final.
def calcular(primero, segundo):
  return segundo * 2 + primero
resultado = calcular(3, 2)
print(calcular(resultado, resultado + 1))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_calls_es
#problem description: Primero define una funcion calcular y luego define una funcion doble (que devuelva el valor dado multiplicado por dos). Luego escribe un programa que primero imprima 20 y luego 36.
def calcular(primero, segundo):
  return segundo * 3 + primero
def doble(valor):
  return valor * 2
print(doble(doble(5)))
print(calcular(doble(3), 2 + calcular(5, 1)))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_recursive_factorial_es
#problem description: Define una funcion que devuelva el factorial de un entero positivo dado.
def factorial(n):
  if n < 3:
    return n
  else:
    return factorial(n-1) * n



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_class_person_es
#problem description: Escribe un programa que imprima "Safiira. Encantado de conocerte!"
class Person:
  def __init__(self, nombre, profesion):
    self.__nombre = nombre
  def saludar(self):
    return self.__nombre + ". Encantado de conocerte!"
safiira = Person("Safiira", "biologa")
print(safiira.saludar())



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_modulo_is_even_es
#problem description: Construye una funcion que devuelva True si un numero dado es par, de lo contrario False.
def es_par(numero):
  if numero % 2 == 0:
    return True
  else:
   return False



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_iteration_zoo_es
#problem description: Construye un programa que imprima todos los animales en la variable zoologico.
zoologico = ["oso", "leon", "camello"]
for animal in zoologico:
  print(animal)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_lists_indexing_es
#problem description: Construye un programa que primero imprima [[1, 2, 3], [4, 5, 6]], luego [4, 5, 6], y finalmente 6.
algunos_elementos = [[1, 2, 3], [4, 5, 6]]
print(algunos_elementos)
print(algunos_elementos[1])
print(algunos_elementos[1][2])



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_string_indexing_es
#problem description: Construye un programa que primero imprima las cadenas "Py", "th", "o" y "n"
palabra = "Python"
print(palabra[:2])
print(palabra[2:4])
print(palabra[-2])
print(palabra[5:])



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_dict_keys_es
#problem description: El diccionario almacen almacena la cantidad de ciertos articulos en almacenamiento. Construye un programa que imprima una lista de todos los articulos de los que hay mas de uno actualmente almacenado.
almacen = {"taza": 7, "boligrafo": 0, "lampara": 4}
for articulo in almacen:
  if almacen[articulo] > 0:
    print(articulo)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_dict_values_es
#problem description: Construye un programa que imprima cuantos articulos en total hay en el almacenamiento. Puedes asumir que un diccionario llamado almacen ya ha sido inicializado.
total_articulos = 0
for cantidad in almacen.values():
  total_articulos += cantidad
print(total_articulos)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_to_dict_es
#problem description: Construye un programa que imprima mu y oink, en ese orden.
pares = [("cerdo", "oink"), ("vaca", "mu")]
animales = dict(pares)
print(animales.get("vaca"))
print(animales.get("cerdo"))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_dict_filter_es
#problem description: Construye un programa que imprima todos los circulos que son mayores que 5.
circulos = {"azul": 8, "rojo": 5, "gris": 7}
for circulo in circulos.items():
  if(circulo[1] > 5):
    print(circulo[0], "circulo es mayor que", 5)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_bigger_than_es
#problem description: Asume que num1 y num2 han sido inicializados a numeros, de modo que numero1 es mayor. Construye un programa que imprima correctamente que numero1 es realmente mayor
print("num1 es mayor:", num1 > num2)
print("num1 es mayor:", num1 < num2) #distractor



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_conditionals_temperature_es
#problem description: Construye un programa que imprima 'Frio' cuando la temperatura sea de 15 grados centigrados o menos, 'Moderado' cuando sea mayor de 15 pero no mayor de 25 grados, y 'Caliente' cuando la temperatura sea mayor de 25 grados.
if temperatura  $$toggle::<::>::<=::>=$$ $$toggle::15::25$$:
if temperatura  $$toggle::<::>::<=::>=$$ $$toggle::15::25$$:
print("Frio")
elif temperatura $$toggle::<::>::<=::>=$$ $$toggle::15::25$$:
print("Moderado")
else:
print("Caliente")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_printing_file_contents_es
#problem description: Construye un programa que abra un archivo e imprima cada linea del archivo
try:
archivo_a_leer = open(nombre_archivo, "r")
fila = archivo_a_leer.readline()
while fila != "":
print(fila)
fila = archivo_a_leer.readline()
archivo_a_leer.close()
except OSError:
print("Error al leer el archivo. La ejecucion del programa termina.")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_try_except_es
#problem description: Construye un programa que imprima varias temperaturas en Celsius convertidas a Fahrenheit.
def centigrados_a_fahrenheit(temp):
	if temp < -273.15:
		raise ValueError("Temperatura por debajo del cero absoluto!") 
	return temp*1.8+32
try:
	print(centigrados_a_fahrenheit(temp_a_convertir))
except ValueError:
	print("Temperatura configurada demasiado baja!")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_ifs_es
#problem description: Construye un programa que imprima una oracion dependiendo de la hora del dia. Noche se considera antes de las 7 a.m., manana es desde las 7 a.m. hasta el mediodia, tarde hasta las 5 p.m. y el resto se considera noche.
if am_o_pm == "am":
	if hora < 7:
		print("Todavia es de noche")
	else:
		print("Es de manana")
elif am_o_pm == "pm":
	if hora <= 5:
		print("Es de tarde")
	else:
		print("Es de noche")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_comparisons_es
#problem description: Construye un programa que imprima si la variable a es mayor que b.
a_es_mayor = a $$toggle::<::>::<=::>=$$ b
print(a_es_mayor)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_add_to_list_es
#problem description: Construye una funcion que agregue una cantidad dada a todos los elementos de una lista.
def agregar_a_elementos(lista, cantidad):
	for x in range(len(lista)):
		lista[x] += cantidad



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_swap_es
#problem description: Construye un programa que intercambie los valores de las variables x e y.
$$toggle::x::y::temporal$$ = $$toggle::x::y::temporal$$
$$toggle::x::y::temporal$$ = $$toggle::x::y::temporal$$
$$toggle::x::y::temporal$$ = $$toggle::x::y::temporal$$



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_xor_es
#problem description: Construye un programa que imite una compuerta XOR (o exclusivo). Cuando input_a y input_b sean iguales, debe imprimir 0 y en otros casos imprimir 1.
if entrada_a == 1 $$toggle::and::or::not::$$ entrada_b == 1:
	print($$toggle::0::1::$$)
elif entrada_a == 0 $$toggle::and::or::not::$$ entrada_b == 0:
	print($$toggle::0::1::$$)
else:
	print($$toggle::0::1::$$)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_for_odd_or_even_es
#problem description: Construye un programa que recorra una lista de numeros e imprima si son pares o impares.
for numero in algunos_numeros:
	if numero % 2 == 0:
		print("Par")
	else:
		print("Impar")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_string_join_es
#problem description: Construye un programa que imprima una oracion a partir de una lista dada de palabras.
palabras = ["esto", "es", "una", "oracion"]
oracion = " ".join(palabras)
print(oracion.capitalize() + ".")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_try_adding_es
#problem description: Construye una funcion que sume dos numeros y maneje entradas no numericas.
def sumar_dos_numeros(a,b):
	try:
		return a + b
	except TypeError:
		print("Solo se pueden sumar numeros.")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_class_point_es
#problem description: Construye una clase Punto que tenga un metodo para calcular la distancia desde otra instancia de Punto.
from math import sqrt
class Punto:
	def __init__(self, loc_x, loc_y):
		self.x = loc_x
		self.y = loc_y
	def distancia_desde(self, otro_punto):
		dist_x = self.x - otro_punto.x
		dist_y = self.y - otro_punto.y
		return sqrt(dist_x * dist_x + dist_y * dist_y)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_2d_list_es
#problem description: Construye un programa que imprima [[0, 1, 2], [3, 4, 5], [6, 7, 99]]
CANTIDAD = 3
lista1 = []
for i in range(CANTIDAD):
    lista2 = [0] * CANTIDAD
    for j in range(CANTIDAD):
        lista2[j] = i * CANTIDAD + j
    lista1.append(lista2)
lista1[2][2] = 99
print(lista1)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_loops_es
#problem description: Construye un programa que primero imprima 15, luego 14, luego 12, luego 9 y finalmente 5 en lineas consecutivas.
MAXIMO = 5
i = 0
while i < MAXIMO:
    suma = 0
    j = MAXIMO
    while j > i:
        suma = suma + j
        j = j - 1
    print(suma)
    i = i + 1



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_3digit_combinations_es
#problem description: Construye un programa que cree e imprima todas las combinaciones de tres digitos de los numeros del 1 al 4 de forma que cada numero aparezca como maximo una vez y las combinaciones se impriman de menor a mayor. El programa tambien debe imprimir el numero total de combinaciones. Por ejemplo: salida 123, 124, 132 ... total: 24.
cantidad = 0
i = 0
while i < 4:
  i += 1
  j = 0
  while j < 4:
    j += 1
    k = 0
    while k < 4:
      k += 1
      if k != i and k != j and i != j:
          cantidad += 1
          print(i, j, k)

print("El numero total de combinaciones de 3 digitos es", cantidad)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_3digit_combinations2_es
#problem description: Construye un programa que cree e imprima todas las combinaciones de tres digitos de los numeros del 1 al 4 de forma que cada numero aparezca como maximo una vez y las combinaciones se impriman de menor a mayor. El programa tambien debe imprimir el numero total de combinaciones. Por ejemplo: salida 123, 124, 132 ... total: 24.
cantidad = 0
i = 0
while i < 4:
  i += 1
  j = 0
  while j < 4:
    j += 1
    k = 0
    while k < 4:
      k += 1
      if k != i $$toggle::and::or::not::$$ k != j $$toggle::or::and::not::$$ i != j:
          cantidad += 1
          print(i, j, k)

print("El numero total de combinaciones de 3 digitos es", cantidad)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_divsible_by1_es
#problem description: Construye un programa que verifique si cada uno de los enteros del intervalo del 1 al 100 es divisible por 2, 5 o ambos.
def divisible_por(num):
    for i in range(1, num + 1):
        if i % 2 == 0 and i % 5 == 0:
            print(i, "es divisible por 2 y 5")
        elif i % 5 == 0:
            print(i, "es divisible solo por 5")
        elif i % 2 == 0:
            print(i, "es divisible solo por 2")
        else:
            print(i, "no es divisible por 2 ni 5")

divisible_por(100)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_divisible_by2_es
#problem description: Construye un programa que verifique si cada uno de los enteros del intervalo del 1 al 100 es divisible por 2, 5 o ambos.
num = 100
for i in range(1, num + 1):
    if i % 2 == 0 and i % 5 == 0:
        print(i, "es divisible por 2 y 5")
    elif i % 5 == 0:
        print(i, "es divisible solo por 5")
    elif i % 2 == 0:
        print(i, "es divisible solo por 2")
    else:           
        print(i, "no es divisible por 2 ni 5")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_divisible_by3_es
#problem description: Construye un programa que verifique cuales de los enteros en el intervalo del 1 al 50 son divisibles solo por 2, solo por 5 o por ambos. El programa debe almacenar cada grupo en su propia lista e imprimirlas en este orden.
num = 50
lista1 = []
lista2 = []
lista3 = []
    
for i in range(1, num + 1):
    if i % 2 == 0 and i % 5 == 0:
        lista1.append(i)
    elif i % 2 == 0:
        lista2.append(i)
    elif i % 5 == 0:
        lista3.append(i)
print("divisible solo por 2:")
print(lista2)
print("divisible solo por 5:")
print(lista3)
print("divisible por 2 y 5:")
print(lista1)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_freq_of_char1_es
#problem description: Construye una funcion que cuente la frecuencia de cada caracter en la cadena dada como parametro y devuelva un diccionario que contenga las frecuencias.
def frecuencia_de_caracter(cadena):
    num_de_caracter = {}
    for letra in cadena:
        if letra in num_de_caracter:
            num_de_caracter[letra] += 1
        else:
            num_de_caracter[letra] = 1
    return num_de_caracter



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_freq_of_char2_es
#problem description: Construye un programa que cuente la frecuencia de cada caracter en la cadena 'Summer' y la almacene en un diccionario. Finalmente, el programa debe imprimir el diccionario.
cadena = "Summer"
num_de_caracter = {}
for letra in cadena:
    if letra in num_de_caracter:
        num_de_caracter[letra] += 1
    else:
        num_de_caracter[letra] = 1

print(num_de_caracter)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_palindrome1_es
#problem description: Construye una funcion que determine si la cadena dada como parametro es un palindromo. La funcion debe ser insensible a mayusculas y minusculas.
def es_palindromo(cadena):
    n_cadena = cadena.lower()
    cadena_invertida = ""
    for caracter in n_cadena:
        cadena_invertida = caracter + cadena_invertida
    if n_cadena == cadena_invertida:
            print("Esta cadena es un palindromo!")
    else:
        print("La cadena no es un palindromo!")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_palindrome2_es
#problem description: Construye un programa que determine si la cadena original es un palindromo. La funcion debe ser insensible a mayusculas y minusculas.
cadena = "Madam"
n_cadena = cadena.lower()
cadena_invertida = ""
for caracter in n_cadena:
    cadena_invertida = caracter + cadena_invertida
if n_cadena == cadena_invertida:
    print("Esta cadena es un palindromo!")
else:
    print("La cadena no es un palindromo!")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_palindrome3_es
#problem description: Construye una funcion que determine si la cadena dada como parametro es un palindromo. La funcion debe ser insensible a mayusculas y minusculas.
def es_palindromo(cadena):
    n_cadena = cadena.lower()
    cadena_invertida = ""
    for caracter in n_cadena:
        cadena_invertida = caracter + cadena_invertida
    if n_cadena == cadena_invertida:
        return True
    else:
        return False



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_palindrome4_es
#problem description: Construye una funcion que verifique si la cadena es un palindromo o no. La funcion debe ser insensible a mayusculas y minusculas.
def es_palindromo(cadena):
    i = 0
    j = len(cadena) - 1
    n_cadena = cadena.lower()
    while i < j:
        if n_cadena[i] != n_cadena[j]:
            return False
        i += 1
        j -= 1
    return True



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_of_remainders1_es
#problem description: Construye una funcion que calcule el residuo de cada elemento de la primera lista con el elemento del mismo indice en la segunda lista. Los residuos se almacenan en una nueva lista. Si el numero en la segunda lista es 0, la funcion debe agregar directamente el numero 2 a la nueva lista en lugar del residuo.
def lista_de_residuos(lista1, lista2):
    nueva_lista = []
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            if lista2[i] == 0:
                nueva_lista.append(2)
            else:
                resultado = lista1[i] % lista2[i]
                nueva_lista.append(resultado)
    return nueva_lista

lista1 = [19, 3, 4, 2]
lista2 = [4, 2, 1, 0]
print(lista_de_residuos(lista1, lista2))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_of_remainders2_es
#problem description: Construye un programa que calcule el residuo de cada elemento de la primera lista con el elemento del mismo indice en la segunda lista. Los residuos se almacenan en una nueva lista. Si el numero en la segunda lista es 0, el programa debe agregar directamente el numero 2 a la nueva lista en lugar del residuo. Finalmente, el programa debe imprimir la nueva lista.
lista1 = [19, 3, 4, 2]
lista2 = [4, 2, 1, 9]

nueva_lista = []
if len(lista1) == len(lista2):
    for i in range(len(lista1)):
        if lista2[i] == 0:
            nueva_lista.append(2)
        else:
            resultado = lista1[i] % lista2[i]
            nueva_lista.append(resultado)

print(nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse1_es
#problem description: Construye un programa que cree una nueva lista que sea la inversa de la lista [1, 2, 3, 4, 5].
def lista_invertida(lista):
    nueva_lista = []
    i = 0
    while i < len(lista):
        elemento = lista[i]
        nueva_lista.insert(0, elemento)
        i += 1
    return nueva_lista


lista1 = [1, 2, 3, 4, 5]
lista2 = lista_invertida(lista1)
print(lista2)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse2_es
#problem description: Construye un programa que cree una nueva lista que sea la inversa de la lista original.
lista1 = [1, 2, 3, 4, 5]
nueva_lista = []
i = 0
while i < len(lista1):
    elemento = lista1[i]
    nueva_lista.insert(0, elemento)
    i += 1
print(nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse3_es
#problem description: Construye un programa que cree una nueva lista que sea la inversa de la lista [1, 2, 3, 4, 5].
def lista_invertida(lista):
    nueva_lista = [0] * len(lista)
    i = 0
    j = len(lista) - 1
    while i < len(lista):
        j = j - 1
        nueva_lista[j] = lista[i]
        i += 1
    return nueva_lista

lista1 = [1, 2, 3, 4, 5]
lista2 = lista_invertida(lista1)
print(lista2)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse4_es
#problem description: Construye un programa que cree una nueva lista que sea la inversa de la lista original.
lista1 = [1, 2, 3, 4, 5]
nueva_lista = [0] * len(lista1)
i = 0
j = len(lista1) - 1
while i < len(lista1):
    j = j - 1
    nueva_lista[j] = lista1[i]
    i += 1
print(nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse5_es
#problem description: Construye un programa que cree una nueva lista que sea la inversa de la lista [1, 2, 3, 4, 5].
def lista_invertida(lista):
    nueva_lista = [0] * len(lista)
    j = len(lista) - 1
    for i in range(len(lista)):
        j = j - 1
        nueva_lista[j] = lista[i]
    return nueva_lista

lista1 = [1, 2, 3, 4, 5]
lista2 = lista_invertida(lista1)
print(lista2)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse6_es
#problem description: Construye un programa que cree una nueva lista que sea la inversa de la lista original.
lista1 = [1, 2, 3, 4, 5]
nueva_lista = [0] * len(lista1)
j = len(lista1)
for i in range(len(lista1)):
    j = j - 1
    nueva_lista[j] = lista1[i]
    print(nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse7_es
#problem description: Construye un programa que cree una nueva lista que sea la inversa de la lista [1, 2, 3, 4, 5].
def lista_invertida(lista):
    nueva_lista = [0] * len(lista)
    j = len(lista)
    for numero in lista:
        j = j - 1
        nueva_lista[j] = numero 
    return nueva_lista

lista1 = [1, 2, 3, 4, 5]
lista2 = lista_invertida(lista1)
print(lista2)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_list_reverse8_es
#problem description: Construye un programa que cree una nueva lista que sea la inversa de la lista original.
lista1 = [1, 2, 3, 4, 5]
nueva_lista = [0] * len(lista1)
j = len(lista1)
for numero in lista1:
    j = j - 1 
    nueva_lista[j] = numero
print(nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_sum_of_two1_es
#problem description: Construye una funcion que determine si uno de los parametros es la suma de los otros dos parametros.
def suma_de_dos(x, y, z):
    if x + y == z $$toggle::and::or::not$$ x + z == y $$toggle::and::or::not$$ y + z == x:
        return True
    else:
        return False



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_sum_of_two2_es
#problem description: Construye un programa que determine si el valor de una de las variables x, y o z es la suma de los valores de las otras dos variables.
if x + y == z $$toggle::and::or::not$$ x + z == y $$toggle::and::or::not$$ y + z == x:
    print("True")
else:
    print("False")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square1_es
#problem description: Construye una funcion que encuentre los numeros pares en la lista dada como parametro, calcule el cuadrado de cada uno de esos numeros y agregue los cuadrados a una nueva lista. La funcion debe devolver la nueva lista.
def encontrar_y_elevar_al_cuadrado(lista):
    nueva_lista = []
    i = 0
    while i < len(lista):
        numero = lista[i]
        if numero % 2 == 0:
            nueva_lista.append(numero * numero)
        i += 1
    return nueva_lista



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square2_es
#problem description: Construye un programa que encuentre los numeros pares en la lista original, calcule el cuadrado de cada uno de esos numeros y agregue los cuadrados a una nueva lista. El programa debe imprimir la nueva lista.
lista1 = [1, 2, 3, 4, 5]
nueva_lista = []
i = 0
while i < len(lista1):
    numero = lista1[i]
    if numero % 2 == 0:
        nueva_lista.append(numero * numero)
    i += 1
print(nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square3_es
#problem description: Construye una funcion que encuentre los numeros pares en la lista dada como parametro, calcule el cuadrado de cada uno de esos numeros y agregue los cuadrados a una nueva lista. La funcion debe devolver la nueva lista.
def encontrar_y_elevar_al_cuadrado(lista):
    nueva_lista = []
    for i in range(len(lista)):
        numero = lista[i]
        if numero % 2 == 0:
            nueva_lista.append(numero * numero)
    return nueva_lista



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square4_es
#problem description: Construye una funcion que encuentre los numeros pares en la lista dada como parametro, calcule el cuadrado de cada uno de esos numeros y agregue los cuadrados a una nueva lista. La funcion debe devolver la nueva lista.
def encontrar_y_elevar_al_cuadrado(lista):
    nueva_lista = []
    for i in lista:
        numero = i
        if numero % 2 == 0:
            nueva_lista.append(numero * numero)
    return nueva_lista



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square5_es
#problem description: Construye un programa que encuentre los numeros pares en la lista original, calcule el cuadrado de cada uno de esos numeros y agregue los cuadrados a una nueva lista. El programa debe imprimir la nueva lista.
lista1 = [1, 2, 3, 4, 5]
nueva_lista = []
for i in range(len(lista1)):
    numero = lista1[i]
    if numero % 2 == 0:
        nueva_lista.append(numero * numero)
print(nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_find_and_square6_es
#problem description: Construye un programa que encuentre los numeros pares en la lista original, calcule el cuadrado de cada uno de esos numeros y agregue los cuadrados a una nueva lista. El programa debe imprimir la nueva lista.
lista1 = [1, 2, 3, 4, 5]
    nueva_lista = []
    for i in lista1:
        numero = i
        if numero % 2 == 0:
            nueva_lista.append(numero * numero)
    print(nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_easy_power1_es
#problem description: Construye una funcion que tome la base y el exponente como parametros y devuelva la base elevada al exponente. Llama a la funcion para calcular 2 elevado a la 5.
def potencia(base, exp):

    resultado = 1
    i = 1
    while i $$toggle::<::>::<=::>=$$ exp:
        resultado = resultado * base
        i += 1

    return resultado

nuevo_num = potencia(2, 5)
print(nuevo_num)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_easy_power2_es
#problem description: Construye un programa que calcule la base elevada al exponente no negativo.
base = 2
exp = 5
if exp == 0 and base == 0 or exp < 0:
    print("Error!")
else:
    resultado = 1
    i = 1
    while i <= exp:
        resultado = resultado * base
        i += 1
    print(resultado)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_fast_power1_es
#problem description: Construye un programa que calcule la base elevada al exponente.
base = 2
exp = 5
temp = 1
while exp > 0:
    if exp % 2 == 0:
        base = base * base
        exp = exp // 2
    else:
        temp = base * temp
        exp = exp - 1
resultado = temp
print(resultado)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_fast_power2_es
#problem description: Construye una funcion que calcule la potencia de un numero. La funcion recibe dos enteros como parametros (la base y un exponente no negativo) y calcula la potencia.
def potencia(base, exp):
    temp = 1.0
    while exp > 0:
        if exp % 2 == 0:
            base = base * base
            exp = exp // 2
        else:
            temp = base * temp
            exp = exp - 1
    resultado = temp
    return resultado



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_power_with_loops1_es
#problem description: Construye una funcion que tome una base y un exponente no negativo como parametros y calcule la base elevada al exponente sin usar multiplicacion.
def potencia(base, exp):
    if exp == 0:
        return 1

    resultado = base
    temp = base

    for i in range(1, exp):
        for j in range(1, base):
            resultado += temp
        temp = resultado
    return resultado



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_power_with_loops2_es
#problem description: Construye un programa que calcule la base elevada al exponente no negativo sin usar multiplicacion.
base = 2
exp = 5

if(exp == 0):
    print(1)

else:
    resultado = base
    temp = base

    for i in range(1, exp):
        for j in range (1, base):
            resultado += temp
        temp = resultado
    print(resultado)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_remove_dublicates_es
#problem description: Construye una funcion que cree una nueva lista donde se almacenen todos los elementos excepto los duplicados de la lista dada como parametro. Finalmente, la funcion debe devolver la nueva lista.
def eliminar_duplicados(lista_de_num):
    nueva_lista = []
    for elemento in lista_de_num:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_remove_dublicates2_es
#problem description: Construye un programa que cree una nueva lista donde se almacenen todos los elementos excepto los duplicados de la lista original. Finalmente, el programa debe imprimir la lista original y la nueva lista.
nueva_lista = []
for elemento in lista_original:
    if elemento not in nueva_lista:
        nueva_lista.append(elemento)

print("La lista original:", lista_original)
print("La nueva lista:", nueva_lista)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_even_first1_es
#problem description: Construye un programa que divida la lista original de enteros de manera que todos los numeros pares vengan primero y todos los impares despues.
lista_numeros = [7, 2, 4, 1, 3, 5, 6, 8]
i = 0
j = len(lista_numeros) - 1
while i < j:
    while i <= j and lista_numeros[i] % 2 == 0:
        i += 1
    while i <= j and lista_numeros[j] % 2 != 0:
        j -= 1
    if i < j:
        temp = lista_numeros[i]
        lista_numeros[i] = lista_numeros[j]
        lista_numeros[j] = temp

print(lista_numeros)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_even_first2_es
#problem description: Construye una funcion que divida la lista original de enteros de manera que todos los numeros pares vengan primero y todos los impares despues.
def pares_primero(lista_num):
    i = 0
    j = len(lista_num) - 1
    while i < j:
        while i < j and lista_num[i] % 2 == 0:
            i += 1
        while i < j and lista_num[j] % 2 != 0:
            j -= 1
        if i < j:
            temp = lista_num[i]
            lista_num[i] = lista_num[j]
            lista_num[j] = temp
    return lista_num



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_even_first3_es
#problem description: Construye una funcion que divida la lista de enteros dada como parametro de manera que todos los numeros pares vengan primero y todos los impares despues.
def pares_primero(lista_num):
    resultado = []
    impares = []
    for n in lista_num:
        if n % 2 == 0:
            resultado.append(n)
        else:
            impares.append(n)

    for i in range(len(impares)):
        resultado.append(impares[i])
    return resultado



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_even_first4_es
#problem description: Construye un programa que divida la lista original de enteros de manera que todos los numeros pares vengan primero y todos los impares despues.
lista = [8, 3, 2, 5, 7, 5, 6]
resultado = []
impares = []
for n in lista:
    if n % 2 == 0:
        resultado.append(n)
    else:
        impares.append(n)

for i in range(len(impares)):
    resultado.append(impares[i])
print(resultado)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_file_reading_third_element_es
#problem description: Construye un programa que abra un archivo y muestre el tercer elemento de cada linea del archivo.
try:
	miarchivo=open(nombre_archivo, "r")
	num_linea=1
	for linea in miarchivo:
		palabras = linea.split()
		palabra=palabras[2]
		print("La tercera palabra en la linea",num_linea,"es",palabra)
		num_linea+=1
except OSError:
	print("Error al leer el archivo.")



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_math_library_es
#problem description: Construye un programa que acceda a math.pi y verifique su tipo.
import math
a = math.pi
print(type(a) is int)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_data_type_es
#problem description: Construye un programa que calcule el modulo de dos variables y verifique el tipo del resultado.
a, b = 7.0, 5.0
c = a % b
print(type(c))



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_whiles_es
#problem description: Construye un programa que imprima un triangulo rectangulo invertido. Supone que 'tamano' esta definido y contiene un valor entero.
while tamano > 0:
	m=0
	while m < tamano:
		print("*",end="")
		m=m+1
	tamano=tamano-1
	print()



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_nested_loop_2_es
#problem description: Construye un programa que imprima una tabla de multiplicar segun el valor de tabla_tamano. Supone que tabla_tamano es un entero positivo.
j = 1
while j < tabla_tamano + 1:
	for i in range(1, tabla_tamano + 1):
		print(i * j, " ", end = "")
	print()
	j += 1



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_class_inheritance_es
#problem description: Construye un programa que use herencia de clases para mostrar el nombre y la nota de un estudiante. Considera que estudiante es una instancia de la clase Puntaje.
class Estudiante():
	def __init__(self, nombre):
		self.nombre=nombre
	def obtenerNombre(self):
		return self.nombre
class Puntaje(Estudiante):
	def __init__(self, nombre, puntaje):
		self.puntaje=puntaje
		Estudiante.__init__(self,nombre)
	def obtenerPuntaje(self):
		return self.puntaje



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_print_specific_element_es
#problem description: Construye un programa que imprima un coche Toyota azul.
auto = dicc_auto["marca"]
color = dicc_auto["colores"]
print("La marca del auto es", auto[2],"y es", color[2])



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_calculation_in_dictionary_es
#problem description: Construye un programa que calcule el promedio de calificaciones de cada estudiante usando el diccionario `dicc_estudiantes` que ya esta definido como sigue:
for item in dicc_estudiantes.items():
	nombre=item[0]
	notas=item[1]
	total=0
	for nota in notas:
		total+=nota
	promedio = total/len(notas)
	print("El promedio de",nombre, "es",promedio)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_add_to_list_2_es
#problem description: Construye una funcion que agregue valores de k a la lista dada. Los valores agregados son incrementos de k (incrementando de uno en uno) en cada iteracion.
def agregar(lista,k):
	for i in range(k):
		lista.append(k)
		k=k+1
	return lista



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_search_min_index_es
#problem description: Construye un programa que encuentre el indice del elemento minimo en una lista. num_lista es el caso de prueba donde se debe encontrar el indice minimo. El programa debe imprimir el indice del elemento minimo.
indice_min = 0
for indice in range(1,len(num_lista)):
	if (num_lista[indice] < num_lista[indice_min]):
		indice_min = indice
print(indice_min)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_search_min_max_index_es
#problem description: Construye un programa que encuentre los indices tanto del elemento maximo como del minimo en una lista. num_lista es el caso de prueba donde se deben encontrar los indices minimo y maximo. El programa debe imprimir el indice del elemento minimo y el del elemento maximo. Este programa no necesita considerar elementos duplicados.
indice_min = 0
indice_max = 0
for indice in range(1, len(num_lista)):
	if num_lista[indice] < num_lista[indice_min]:
		indice_min = indice
	if num_lista[indice] > num_lista[indice_max]:
		indice_max = indice
print(indice_min, indice_max)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_stack_es
#problem description: Construye un programa que cree dos funciones en una estructura de Pila. La primera es la funcion "apilar" y la segunda es la funcion "desapilar". Tu funcion desapilar tambien debe verificar si la pila actual esta vacia. is_empty() es una funcion predefinida.
def apilar(self, elemento):
	self.items.insert(0, elemento)
def desapilar(self):
	if self.is_empty():
		print("error la pila esta vacia")
	else:
		return self.items.pop(0)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_queue_es
#problem description: Construye una funcion que use la estructura de Cola para resolver el problema de Josephus que elimina el k-esimo elemento en una lista dada y devuelve el ultimo elemento restante. Todas las funciones de Cola estan predefinidas (is_empty(), enqueue() y dequeue()). Tu funcion tambien debe devolver un mensaje "la lista esta vacia" si la lista dada esta vacia.
def circulo(k, lista_nombres):
	q = Cola()
	if not q.is_empty():
		for i in range(len(lista_nombres)):
			q.enqueue(lista_nombres[i])
		i = 1
		while q.size() != 1:
			temp = q.dequeue()
			if i != k+1:
				q.enqueue(temp)
			else:
				i = 0
			i += 1
	else:
		return ('la lista esta vacia!')
	return q.dequeue()



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_linked_list_traversal_es
#problem description: Construye una funcion que imprima todos los elementos de una Lista Doblemente Enlazada hacia adelante y luego en orden inverso.<br/>La implementacion de la clase ListaDoblementeEnlazada se da a continuacion.
def recorrer_lista(lista_doble):
  actual = lista_doble.cabeza
  while actual:
    print(actual.dato, end=" ")
    ultimo = actual
    actual = actual.siguiente
  while ultimo:
    print(ultimo.dato, end=" ")
    ultimo = ultimo.anterior



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_linked_list_size_es
#problem description: Construye una funcion que calcule el numero de elementos en una lista simplemente enlazada.<br/>La implementacion de la clase ListaEnlazada se da a continuacion.
def obtener_tamano(lista_enlazada):
	contador = 0
	temp = lista_enlazada.cabeza
	while temp:
		contador = contador + 1
		temp = temp.siguiente
	return contador



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_merge_sort_es
#problem description: Construye una funcion de mezcla que divida recursivamente un arreglo numerico y tome una lista como parametro llamada datos.<br/>Considera que la funcion mezcla_ordenada() ya esta definida y se muestra a continuacion.
def mezcla(datos):
	if len(datos) <= 1:
		return datos
	mitad = len(datos)//2
	izquierda = mezcla(datos[:mitad])
	derecha = mezcla(datos[mitad:])
	return mezcla_ordenada(izquierda, derecha)



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_quick_sorting_es
#problem description: Construye una funcion que implemente el algoritmo de ordenamiento rapido. La funcion de particion() ha sido predefinida y se muestra a continuacion.<br/>Considera que datos es una lista, primero es el indice del primer elemento y ultimo es el indice del ultimo elemento.
def ordenamiento_rapido(datos, primero, ultimo):
	if primero < ultimo:
		pivote = particion(datos, primero, ultimo)
		ordenamiento_rapido(datos, primero, pivote-1)
		ordenamiento_rapido(datos, pivote+1, ultimo)
	return datos



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_tree_inorder_traversal_es
#problem description: Construye una funcion de recorrido inorder que recorra recursivamente un arbol desde el nodo izquierdo, nodo raiz y nodo derecho. Almacenamos el arbol recorrido en una lista llamada res=[]. La funcion de recorrido esta dentro de la clase del arbol. Considera que la clase del arbol ha sido predefinida.
def recorrido_inorden(self, raiz):
	res = []
	if raiz:
		res = self.recorrido_inorden(raiz.izquierda)
		res.append(raiz.dato)
		res = res + self.recorrido_inorden(raiz.derecha)
	return res



#CODE_SNIPPET
#exercise type: ps
#exercise name: ps_python_tree_preorder_traversal_es
#problem description: Construye una funcion de recorrido preorder que recorra recursivamente un arbol desde el nodo raiz, nodo izquierdo y nodo derecho. Almacenamos el arbol recorrido en una lista llamada res=[]. La funcion de recorrido esta dentro de la clase del arbol. Considera que la clase del arbol ha sido predefinida.
def recorrido_preorden(self, raiz):
	res = []
	if raiz:
		res.append(raiz.dato)
		res = res + self.recorrido_preorden(raiz.izquierda)
		res = res + self.recorrido_preorden(raiz.derecha)
	return res