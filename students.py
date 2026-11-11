stds = []
avarage_grade = 0
count = int(input("how many students? ")) #گرفتن تعداد دانش آموزان از کاربر

# گرفتن اطلاعات هر دانش اموز از کاربر
for i in range(count): 
  std = []
  std.append(input(f"student {i + 1} first name: "))
  std.append(input(f"student {i + 1} last name: "))
  std.append(int(input(f"student {i + 1} id: ")))
  std.append(float(input(f"student {i + 1} grade: ")))
  print("=========================================================")
  stds.append(std) # اضافه کردن لیست مربوط به دانش اموز به لیست کل دانش آموزان

# محاسبه میانگین نمرات دانش آموزان 
for s in stds:
  avarage_grade += s[3]
avarage_grade /= len(stds)

print(f"class avarage grade is {avarage_grade}")
print("=========================================================")

# تشخیص بهترین و بدترین دانش آموز با مقایسه نمره ها
best_std = stds[0]
worst_std = stds[0]
best_grade = stds[0][3]
worst_grade = stds[0][3]

for s in stds:
  if best_grade < s[3]:
    best_std = s
    best_grade = s[3]

  if worst_grade > s[3]:
    worst_std = s
    worst_grade = s[3]

print(f"best grade is {best_grade} from {best_std[0]} {best_std[1]} with Id {best_std[2]}")
print(f"worst grade is {worst_grade} from {worst_std[0]} {worst_std[1]} with Id {worst_std[2]}")
print("=========================================================")

# نمایش و تغییر نمره دانش آموز مورد نظر
intended_std = int(input("Enter an student Id for changing grade: "))
print(f"intended student grade is {stds[intended_std - 1][3]}")

grade_change = input("do you want to change it?(Y / any key): ")
if grade_change == 'Y' or grade_change == 'y':
  stds[intended_std - 1][3] = float(input("new grade: "))
  print("_done_")
print("=========================================================")

# نمایش اطلاعات کل دانش آموزان
print("* all students: ")
for s in stds:
  print(f"  {s[0]} | {s[1]} | {s[2]} | {s[3]}")
   