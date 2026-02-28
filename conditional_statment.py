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



