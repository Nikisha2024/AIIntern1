import os

def save_file(file):
    file_location = f"data/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return file_location
