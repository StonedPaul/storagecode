from canvasapi import Canvas

API_URL = "https://academy.instructure.com/"
API_KEY = "3287~BpA0p1uUspZgzMGhvkfvZ6u9AiK1KlpSBY06f6mIamilUdqM2IsQd9gERk0xwv3a"
canvas = Canvas(API_URL, API_KEY)

#1711 user
#3486 course code for DSA

user = canvas.get_user(1711)
count = 0
courses = user.get_courses(enrollment_state='active')
file = open('textfile.txt', 'w+')
file.write(f"Currently looking at student: {user.name}")

for course in courses:
    file.write(f"------------------------------{course}------------------------------")
    assignments = user.get_assignments(course)
    for assignment in assignments:
        count+=1
        file.write(f"{assignment}\n")

file.write(f"{count} assignments for the school year 2020-21")