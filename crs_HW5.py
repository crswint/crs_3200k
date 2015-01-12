## #1 all parts, #2 all except i

import sqlite3 as dbapi

# 1) a) Create a new database called census.db

con = dbapi.connect('U:/Shared/GIS/StuData/crswin5726/Python/census.db')

# b) Make a db table called Density, that will hold the name of the
# province or territory (text), the population (integer) and the land
# area (real)

cur = con.cursor()

cur.execute('CREATE TABLE Density(Territory TEXT, Population INTEGER, Area REAL')

# c) Insert the data from Table 27, 2001 Canadian Census Data
#  cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')

cur.execute('INSERT INTO Density VALUES("Newfoundland and Labrador", 512930, 370501.69)')
cur.execute('INSERT INTO Density VALUES("Prince Edward Island", 135294, 5684.39)')
cur.execute('INSERT INTO Density VALUES("Nova Scotia", 908007, 52917.43)')
cur.execute('INSERT INTO Density VALUES("New Brunswick", 729498, 71355.67)')
cur.execute('INSERT INTO Density VALUES("Quebec", 7237479, 1357743.08)')
cur.execute('INSERT INTO Density VALUES("Ontario", 11410046, 907655.59)')
cur.execute('INSERT INTO Density VALUES("Manitoba", 1119583, 551937.8)')
cur.execute('INSERT INTO Density VALUES("Saskatchewan", 978933, 586561.35)')
cur.execute('INSERT INTO Density VALUES("Alberta", 2974807, 639987.12)')
cur.execute('INSERT INTO Density VALUES("British Columbia", 3907738, 926492.48)')
cur.execute('INSERT INTO Density VALUES("Yukon Territory", 28674, 474706.97)')
cur.execute('INSERT INTO Density VALUES("Northwest Territories", 37360, 1141108.37)')
cur.execute('INSERT INTO Density VALUES("Nunavut", 26745, 1925460.18)')

con.commit()

# d) Display the contents of the table.

cur.execute('SELECT * FROM Density')
print cur.fetchall()

# e) Display the populations

cur.execute('SELECT Population FROM Density')
print cur.fetchall()

# f) Display the provinces that have populations of less than 1 million

cur.execute('SELECT Territory FROM Density WHERE Population < 1000000')
print cur.fetchall()

# g) Display the provinces that have populations less than 1 million or greater than 5 million.

cur.execute('SELECT Territory FROM Density WHERE Population < 1000000 OR Population > 5000000')
print cur.fetchall()

# h) Display the provinces that do not have populations less than 1 million or greater than 5 million

cur.execute('SELECT Territory FROM Density WHERE Population > 1000000 OR Population < 5000000')
print cur.fetchall()

# i) Display the populations of provinces that have a land area greater than 200,000 sq Kilometers

cur.execute('SELECT Population FROM Density WHERE Area > 200000')
print cur.fetchall()

# j) Display the provinces along with their population densities (population divided by land area)
#  below is the correct format for SQL statements (to allow for more fluid transition)
cur.execute("""SELECT Territory, Population/Area FROM Density;""")
print cur.fetchall()

#2

cur.execute('CREATE TABLE Capitals(Territory TEXT, Capital TEXT, Population INTEGER')

cur.execute('INSERT INTO Capitals VALUES("Newfoundland and Labrador", "St.Johns", 172918)')
cur.execute('INSERT INTO Capitals VALUES("Prince Edward Island", "Charlottetown", 58358)')
cur.execute('INSERT INTO Capitals VALUES("Nova Scotia", "Halifax", 359183)')
cur.execute('INSERT INTO Capitals VALUES("New Brunswick", "Fredericton", 81346)')
cur.execute('INSERT INTO Capitals VALUES("Quebec", "Quebec", 682757)')
cur.execute('INSERT INTO Capitals VALUES("Ontario", "Toronto", 4682897)')
cur.execute('INSERT INTO Capitals VALUES("Manitoba", "Winnipeg", 671274)')
cur.execute('INSERT INTO Capitals VALUES("Saskatchewan", "Regina", 192800)')
cur.execute('INSERT INTO Capitals VALUES("Alberta", "Edmonton", 937845)')
cur.execute('INSERT INTO Capitals VALUES("British Columbia", "Victoria", 311902)')
cur.execute('INSERT INTO Capitals VALUES("Yukon Territory", "Whitehorse", 21405)')
cur.execute('INSERT INTO Capitals VALUES("Northwest Territories", "Yellowknife", 16541)')
cur.execute('INSERT INTO Capitals VALUES("Nunavut", "Iqaluit", 5236)')

con.commit()

# 2) a)

cur.execute('SELECT * FROM Capitals')

# b)

cur.execute('''
SELECT Density.Population, Capitals.Population
FROM Density INNER JOIN Capitals
WHERE (Density.Territory = Capitals.Territory)''')

# c

cur.execute('''
SELECT Density.Area
FROM Density INNER JOIN Capitals
WHERE (Density.Territory = Capitals.Territory)
AND (Capitals.Population > 100000)''')

# d)

cur.execute('''
SELECT Density.Territory
FROM Density INNER JOIN Capitals
WHERE (Density.Territory = Capitals.Territory)
AND (Density.Population/Density.Area < 2)
AND (Capitals.Population > 500000)''')

# e)

cur.execute('SELECT SUM (Area) FROM Density')

# f)

cur.execute('SELECT AVG (Population) FROM Capitals')

# g)

cur.execute('SELECT MIN (Population) FROM Capitals')

# h)

cur.execute('SELECT MAX (Population) FROM Density')
