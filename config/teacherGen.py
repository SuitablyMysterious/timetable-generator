import csv
from random import choice

numTeachers = 10

subjects = [
    ["Mathematics",0,0,0],
    ["English Language",
    "English Literature",0,0],
    ["Biology",0,0,0],
    ["Chemistry",0,0,0],
    ["Physics",0,0,0],
    ["Religious Studies",0,0,0],
    ["Physical Education",0,0,0],
    ["Computer Science",0,0,0],
    ["History",0,0,0],
    ["Geography",0,0,0],
    ["Modern Language",
    "French",
    "German",
    "Spanish"],
    ["Drama & Theatre Studies",0,0,0],
    ["Music",0,0,0],
    ["Electronics",0,0,0],
]

with open('teachers.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    for teacher in range(numTeachers):
        teacherID = [f'teacher{teacher}']
        teacherSubjects = choice(subjects)
        writer.writerow(teacherID + teacherSubjects)
        