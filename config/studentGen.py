import csv
from random import sample

numStudents = 100
numSubjectPer = 9

subjects = [
    "Mathematics",
    "English Language",
    "English Literature",
    "Biology",
    "Chemistry",
    "Physics",
    "Modern Language",
    "Religious Studies",
    "Physical Education",
    "Computer Science",
    "History",
    "Geography",
    "French",
    "German",
    "Spanish",
    "Drama & Theatre Studies",
    "Music",
    "Electronics",
]

with open('students.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    for student in range(numStudents):
        studentID = [f'student{student}']
        studentSubjects = sample(subjects, numSubjectPer)
        writer.writerow(studentID + studentSubjects)
