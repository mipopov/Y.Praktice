n = int(input())
visited_optional_courses = []

i = 0
while i < n:
    inputCourse = str(input())
    if inputCourse in visited_optional_courses:
        i += 1
    else:
        visited_optional_courses.append(inputCourse)
        i += 1

for i in visited_optional_courses:
    print(i)