# -------------------------------------------------------------------
# sort() method   = used with lists
# sort() function = used with iterables

# Students LIST of tupples
students_list = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]

# Students Tupple of tupples => As iterable
students_iter = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
age = lambda ages:ages[2]
# students.sort(key=age)                     # sorts current list

sorted_stlist_grade = sorted(students_iter,key=grade) # sorts and creates a new list
sorted_stlist_age = sorted(students_iter,key=age)

sorted_stiter_grade = sorted(students_iter,key=grade) # sorts and creates a new list
sorted_stiter_age = sorted(students_iter,key=age)

for i in sorted_stlist_grade:
    print(i)

print("###################################")

for i in sorted_stiter_age:
    print(i)
# -------------------------------------------------------------------