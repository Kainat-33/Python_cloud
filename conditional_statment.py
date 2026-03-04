#conditional statment
#condation
# conditional operators
# > = greater then
# < = less then
# == is equal
# != not equal
# >= greater then or equal
# <= less then or equal

print(12 > 5)
print(4<3)
print(4 == 4)
print(2!=2)
print(15 >= 5)

value = 34
val = 20
print(value <= val)


# if single
# if-else two block
#if-elif-else multiblock
 

# Write a program to show mark and 
# say congragulation if marks are above 60.
marks = float(input("enter your masks:"))


if marks > 60:
  print("congragulation you're passed", marks)
  percentage = marks/100*100
  print("your percentage is:" , percentage, "%" ) 


# Write a program to show mark and 
# say  failed if marks are below 45.
marks = float(input("enter your masks:"))
if marks < 45:
  print("opps sorry you are failed", marks)
  percentage = marks/100*100
  print("your percentage is:" , percentage, "%" ) 

print("program end") 



#if
#ifelse
#ifelif(repeat acording to your choice)else



#check the number is positive, negitive or zero
number = int(input("enter your number"))

if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negitive")
else:
    print("number is zero")


# print day according to its number lets say monday number is 1 and so on.
day_number = int(input("enter your number"))
if day_number == 1:
    print("the day is Monday")
elif day_number == 2:
        print("the day is tuesday")
elif day_number == 3:
      print("the day is wednesday")

elif day_number == 4:
      print("the day is thursday")

elif day_number == 5:
      print("the day is friday")

elif day_number == 6:
      print("the day is saturday")

elif day_number == 7:
      print("the day is sunday")                                
else:
      print("Sorry invalid choice within 1-7") 
                            
