#next things to try: get top line of data and automatically set up table columns and headers, and apply those to variables; make a new database for each big tsv and make them relational

import sqlite3
import csv

conn = sqlite3.connect('imdb-sm-tsv.sqlite')
cur = conn.cursor()

tsvfile = input('Which TSV do you want to import? ')
if ( len(tsvfile) < 1 ) : tsvfile = "imdb-sm.tsv"
        
cur.execute('DROP TABLE IF EXISTS ImdbSm')

#Rank	Title	Genre	Description	Director	Actors	Year	Runtime (Minutes)	Rating	Votes	Revenue (Millions)	Metascore

cur.execute('''CREATE TABLE ImdbSm
    (id INTEGER PRIMARY KEY UNIQUE, rank INTEGER, title TEXT, genre TEXT, description TEXT,
    director TEXT, actors TEXT, year INTEGER, runtime INTEGER,
    rating REAL)''')

print('Importing CSV rows')
with open(tsvfile) as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for row in tsv_file:
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