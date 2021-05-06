from canvasapi import Canvas


def names(userlist):
    newlist = []
    for i in range(0, len(userlist), 2):
        newlist.append(userlist[i])
    return newlist


def id(userlist):
    newlist = []
    for i in range(1, len(userlist), 2):
        newlist.append(userlist[i])
    return newlist


API_URL = "https://academy.instructure.com/"
API_KEY = "3287~BpA0p1uUspZgzMGhvkfvZ6u9AiK1KlpSBY06f6mIamilUdqM2IsQd9gERk0xwv3a"
canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(3910)

userlist = ["NAME", "ID"]
user = canvas.get_user("1686")
courselist = [f"{user}"]

for user in course.get_users():
    # print(f"{user.name} : {user.id}")
    userlist.append(user.name)
    userlist.append(user.id)

for course in user.get_courses:
    courselist.append(course)

print(courselist)
