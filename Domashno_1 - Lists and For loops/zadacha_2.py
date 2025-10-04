grades = [95, 82, 67, 54, 100, 73, 88, 42]
excellent = []
good = []
pass_grades = []
fail_grades = []

for grade in grades:
  if grade >= 90:
    excellent.append(grade)
  elif grade >= 70: 
    good.append(grade)
  elif grade >= 50: 
    pass_grades.append(grade)
  else:  
    fail_grades.append(grade)

print("Excellent grades:")
for num in excellent:
  print(num)

print("Good grades:")
for num in good:
  print(num)

print("Pass grades:")
for num in pass_grades:
  print(num)

print("Fail grades:")
for num in fail_grades:
  print(num)