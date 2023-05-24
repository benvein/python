from typing import *
from student import Student
from studentIO import *
from services import *

students: List[Student] = importStudents()

#1 - Írjuk ki minden diák adatát a képernyőre!
print("az osztaly tanuloi: ")
for student in students:
    print(student)

#2 - Hány diák jár az osztályba?
countOfClass: int = len(students)
print(f"\n\naz osztalynak {countOfClass} tanuloja van\n\n")

#3 - Mennyi az osztály átlaga?
classAverage: float = calculateAverage(students)
print(f"\n\nAz osztaly atlaga {classAverage:1.2f}\n\n")

#4 - Keressük a legtöbb pontot elért érettségizőt és írjuk ki az adatait a képernyőre.
bestStudent: Student = getBestStudent(students)
print(f"\n\nlegjobb tanulo: {bestStudent}\n\n")

#5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
aboveAverage: List[Student] = studentsAboveAverage(students, classAverage)
writeStudentsInFile(aboveAverage, "atlagfelett.txt")

#6 - Van e kitünő tanulónk?
exists: bool = isAnyExcellentStudent(students)
if (exists):
	print("\n\nvan kituno tanulo\n\n")
else:
	print("\n\nnincs kituno tanulo\n\n")


""" 7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
    Értékhatárok:
	- elégtelen, ha: 0.00 - 1.99
	- elégséges, ha: 2.00 - 2.99
	- jó, ha: 3.00 - 3.99
	- jeles, ha: 4.00 - 4.99
	- kitünő, ha: 5.00 """