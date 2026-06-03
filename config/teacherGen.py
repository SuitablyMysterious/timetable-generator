import csv, time
from random import choice

numTeachers = 1000000

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

start = time.perf_counter()

with open('teachers.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    for teacher in range(numTeachers):
        teacherID = [f'teacher{teacher}']
        teacherSubjects = choice(subjects)
        writer.writerow(teacherID + teacherSubjects)

elapsed = time.perf_counter() - start
print(f"Took {elapsed:.3f}s")
        