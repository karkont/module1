grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud = list(students)
stud.sort()
a1, b1, c1, d1, e1 = grades[0:]
a2, b2, c2, d2, e2 = sum(a1), sum(b1), sum(c1), sum(d1), sum(e1)
a3, b3, c3, d3, e3 = len(a1), len(b1), len(c1), len(d1), len(e1)
a, b, c, d, e = a2/a3, b2/b3, c2/c3, d2/d3, e2/e3
avg = {stud[0]: a, stud[1]: b, stud[2]: c, stud[3]: d, stud[4]: e}
print('Student AVG: ', avg)
