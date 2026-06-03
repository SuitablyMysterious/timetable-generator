"""
timetable-generator
    Copyright (C) 2026  HippoProgrammer, NHPlayzz

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse, csv
from alive_progress import alive_bar

subjectsPer = 9

parser = argparse.ArgumentParser(
    prog = 'timetable-generator',
    description = 'generates timetables'
)

parser.add_argument('students')
parser.add_argument('teachers')
args = parser.parse_args()

with open(args.students, 'r') as studentFile:
    reader = csv.reader(studentFile)
    students = []
    for line in reader:
        students.append(line)

with open(args.teachers, 'r') as teacherFile:
    reader = csv.reader(teacherFile)
    teachers = []
    for line in reader:
        teachers.append(line)

def similarityScore(student1: list, student2: list) -> int:
    subjects1 = set(student1[1:])
    subjects2 = set(student2[1:])
    return len(subjects1.intersection(subjects2))

scores = dict()

for i in range(subjectsPer+1):
    scores[i] = []

with alive_bar(len(students)^2) as bar:
    for student1 in students:
        for student2 in students:
            if student1[0] != student2[0]:
                score = similarityScore(student1, student2)
                canAppend = True
                for item in scores[score]:
                    if len(set(item).intersection(tuple([student1[0], student2[0]]))) == 2:
                        canAppend = False
                if canAppend:
                    scores[score].append(tuple([student1[0], student2[0]]))
                bar()
print(scores)

