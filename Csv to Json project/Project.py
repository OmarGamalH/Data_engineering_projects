import csv
import json
import glob
import files as f
import os


def main():
    files = f.get_csv_files(os.getcwd())
    if len(files) >= 1:
        file_content = []
        for file in files:
            try:
                with open(file , "r" , encoding= "utf-8") as F: 
                    csv_file = csv.DictReader(F)
                    csv_file = list(csv_file)
                    required_keys = ["region" , "variety" , "rating"]
                    for row in csv_file:
                        d = {}
                        for key in required_keys:
                            d[key] = row[key]
                        file_content.append(d)
                    print(f"file : {file} was read successfully")
            except:
                print(f"file : {file} wasn't read successfully")

        result_path = os.path.join(os.getcwd() , "result.json")
        with open(result_path , "w") as file:
            json.dump(file_content , file)
            print(f"The Output file : {result_path}")

    else:
        print("Wrong Path used or no files in the path provided")



if __name__ == "__main__":
    main()














        