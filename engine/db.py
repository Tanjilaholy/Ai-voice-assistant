import csv
import sqlite3

con = sqlite3.connect("lexi.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'android studio', 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)


#query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
#cursor.execute(query)
#con.commit()

 #testing module
#app_name = "android studio"
#cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#results = cursor.fetchall()
#print(results[0][0])


# Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 1]  # Adjust 1 to the correct index for 'mobile_no'

# # # Read CSV and insert selected columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#      csvreader = csv.reader(csvfile)
#      for row in csvreader:
#          if len(row) > max(desired_columns_indices):
#              selected_data = [row[i] for i in desired_columns_indices]
#              cursor.execute('''INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?)''', tuple(selected_data))
#          else:
#              print(f"Skipped row due to missing columns: {row}")

# #Commit and close
# con.commit()
# con.close()

# query = 'Holi'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])