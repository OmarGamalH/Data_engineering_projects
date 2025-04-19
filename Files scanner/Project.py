import os
import pandas as pd
import sys 
import math
import sqlite3 as sql

def main():
    database_path = os.path.join(os.getcwd() , "files.db") 
    if os.path.exists(database_path):
        os.remove(database_path)
    connection = sql.connect(database_path)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE  IF NOT EXISTS files (
                ID INTEGER PRIMARY KEY AUTOINCREMENT , 
                NAME TEXT,
                SIZE INTEGER)""")
    connection.commit()

    if len(sys.argv) <= 1 :
        print("The usage of the program is : py Project.py root_name")
        return -1

    path = sys.argv[1]

    if os.path.exists(path):
        result_files = []
        files_size = []
        path = os.path.abspath(path)
        print("""Choose one of the options:
            1. No more than 20 file
            2. Files larger than a specific size in megabytes
            3. search for all files (Default)  
               """)
        
        choice = int(input("Choice(1-3) : "))
        max_files = 20
        if choice == 2:
            specific_size = (int(input("Give the specific size : ")) * math.pow(10 , 6))
            print(specific_size)
        for roots , dirs , files in os.walk(path):
            for file in files:
                    path = os.path.join(roots , file)
                    if os.path.exists(path):
                        file_size = os.path.getsize(path)
                        if choice == 1 and path not in result_files:
                            max_files -= 1
                            if max_files < 0 :
                                break
                        if choice == 2:
                            if not (file_size > specific_size):
                                continue
                        
                        if path not in result_files:
                            print(f"Path {path} was added to the list")
                            result_files.append(path)
                            files_size.append(file_size)
                            cursor.execute("INSERT INTO files (NAME , SIZE) VALUES(? , ?)" , (path , file_size))
                            connection.commit()
                    else:
                        print(f"file {path} doesn't exist")

        files = cursor.execute("SELECT * FROM files ORDER BY SIZE DESC, NAME")
        for file in files:
            print(f"File No.{file[0]} name : {file[1]} , file size : {file[2] * math.pow(10 , -6)} MB")

    else:
        print("Path doesn't exist")
        return
    
if __name__ == "__main__":
    main()




        