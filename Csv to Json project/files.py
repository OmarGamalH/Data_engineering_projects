import os 
import glob as gb


def get_csv_files(path):
    extention = "*.csv"
    # search for all files in the the path
    if os.path.exists(path):
        csv_path = path + "/" + extention
        files = gb.glob(csv_path)
        return files
    else:
        return []
    

