import sqlite3
connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')
INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)
VALUES ('Junga', 'Vijay Sethupathi', 'Sayyesha Saigal', 2018,'Gokul' );
INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)
VALUES ('Visvasam', 'Ajith', 'Nayanthara', 2019,'Siva' );
INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)
VALUES ('Master', 'Vijay Sethupathi', 'Malvika Mohan', 2021,'Loki' );
INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)
VALUES ('Red', 'AK', 'Thrisha', 2001,'Noper' );
cursor.execute('''SELECT * from Movies''')
result = cursor.fetchone();
print(result)
connection.commit()
connection.close()