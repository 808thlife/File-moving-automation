import os 
from datetime import date

SORTING_DIRECTORY = os.path.join("/Users", "ismail", "downloads")

date = date.today()

def get_files(folder, file_type):
    """
    GETTINGS FILES WITH SOME X "extension". RETURNING ARRAY
    """

    files = []

    folder = os.listdir(folder)

    for file in folder:
        file_name, file_extension = os.path.splitext(file)
        if file_extension == "."+file_type:  
            files.append(file)
    return files

def move_files(folder, files):

    if not len(files) == 0:
        try:
            new_directory = os.mkdir(f"{folder}/music-{date}")
        except FileExistsError:
            new_directory = os.path.join(folder, f"music-{date}")
    
        for file in files:
            os.rename(f"{folder}/{file}", f"{new_directory}/{file}")

    return None

def main(folder, file_type):

    files = get_files(folder, "mp3")

    if not move_files(folder, files) == None:
        move_files(folder, files)

    return "Invalid Action"

if __name__ == "__main__":
    main(SORTING_DIRECTORY, "mp3")