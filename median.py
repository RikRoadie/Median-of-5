import stdio
import sys

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
n3 = int(sys.argv[3])
n4 = int(sys.argv[4])
n5 = int(sys.argv[5])
durchlauf = 0

while durchlauf < 3:

    if n1 > n2:
        merkzahl = n1
        n1 = n2
        n2 = merkzahl

    if n2 > n3:
        merkzahl = n2
        n2 = n3
        n3 = merkzahl

    if n3 > n4:
        merkzahl = n3
        n3 = n4
        n4 = merkzahl

    if n4 > n5:
        merkzahl = n4
        n4 = n5
        n5 = merkzahl

    maxi = n5
    n5 = 0
    durchlauf = durchlauf + 1
    
stdio.write("Die mittlere Zahl (Median) ist ")
stdio.writeln(maxi)
