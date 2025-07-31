from pathlib import Path  # It is a modern alternative to older modules like os.path
import os

"""this fn return all file and folder"""


def read_all_file_and_folder():
    path = Path('')  # Create a Path object
    items = list(path.rglob('*'))  # return all dir by a list
    print("All file and folder is: ")
    for i, items in enumerate(items):
        print(f"{i + 1} : {items}")


# -- Create File:
def create_file():
    try:
        read_all_file_and_folder()  # call for show all file
        file_name = input("Enter your new file name: ")
        p = Path(file_name)  # name converted by a path

        if not p.exists():
            with open(p, "w") as fs:
                data = input("Write content here: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY...")
        else:
            print("This file is already exist")

    except Exception as err:
        print(f"Error is: {err}")



# -- Read File:
def read_file():
    try:
        read_all_file_and_folder()
        name = input("Which file do you want to read? ")
        p = Path(name)
        if (p.exists() and p.is_file()):
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READED SUCCESSFULLY...")
        else:
            print("Not found!")

    except Exception as err:
        print(f"Error is: {err}")



# -- Update file:
def update_file():
    try:
        read_all_file_and_folder()

        name = input("Which file do you want to update? ")
        p = Path(name)
        if (p.exists() and p.is_file()):
            print("Press '1' for rename your file.")
            print("Press '2' for overwrite on file.")
            print("Press '3' for appending content.")

            res = int(input("Tell your response: "))

            match res:
                case 1:
                    name2 = input("write your new file name: ")
                    p2 = Path(name2)
                    p.rename(p2)
                case 2:
                    with open(p, 'w') as fs:
                        data = input("Write content for overwrite: ")
                        fs.write(data)
                case 3:
                    with open(p, 'a') as fs:
                        data = input("Write content for append: ")
                        fs.write(data)
                case _:
                    print("Invalid option")

    except Exception as err:
        print(f"Error is: {err}")            




# -- Delete file:
def delete_file():
    try:
        read_all_file_and_folder()
        name = input("Which file do you want to delete? ")
        p = Path(name)
        if(p.exists() and p.is_file()):
            os.remove(p)
            print("FILE REMOVE SUCCESSFULLY...")
        else:
            print("Not found!")  

    except Exception as err:
        print(f"Error is {err}")          




# show option to user
print("Press '1' for Create a file.")
print("Press '2' for Read a file.")
print("Press '3' for Update a file.")
print("Press '4' for Delete a file.")

option = int(input("Choose a option: "))

match option:
    case 1: create_file()
    case 2: read_file()
    case 3: update_file()
    case 4: delete_file()
    case _: print("Invalid option!")
