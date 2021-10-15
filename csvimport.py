import sqlite3
import csv

conn = sqlite3.connect('imdb-sm.sqlite')
cur = conn.cursor()

csv_data = csv.reader(open('imdb-sm.csv'))
header = next(csv_data)

cur.execute('DROP TABLE IF EXISTS ImdbSm')

#Rank	Title	Genre	Description	Director	Actors	Year	Runtime (Minutes)	Rating	Votes	Revenue (Millions)	Metascore

cur.execute('''CREATE TABLE ImdbSm
    (id INTEGER PRIMARY KEY UNIQUE, rank INTEGER, title TEXT, genre TEXT, description TEXT,
    director TEXT, actors TEXT, year INTEGER, runtime INTEGER,
    rating REAL)''')

print('Importing CSV rows')
for row in csv_data:
    print(row)
    rank = row[0]
    title = row[1]
    genre = row[2]
    description = row[3]
    director = row[4]
    actors = row[5]
    year = row[6]
    runtime = row[7]
    rating = row[8]
    
    cur.execute('''
        INSERT INTO ImdbSm (rank, title, genre, description, director, actors, year, runtime, rating)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (rank, title, genre, description, director, actors, year, runtime, rating))
        
conn.commit()
cur.close()
print('Done')