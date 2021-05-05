import os, os.path
import time
import keyboard
import time

real_path = os.path.realpath(__file__)
print(real_path)

key1 = 'f4'
key2 = 'f6'
key3 = 'esc'
key4 = 'f8'
key5 = 'f9'
key6 = 'f7'
key7 = 'Del'

def folder_init():
    """Receives folder name input from user"""
    folder_names = []
    done = False
    print("Press {} when creating each folder name".format(key6))
    print(f"e.g. {key6} + folder_name + 'enter', {key6} + folder_name + 'enter'...")
    print(f"Press {key1} for help")
    
    while done is False:
        done = False

        if keyboard.is_pressed(key2):
            keyboard.release(key2)
            if folder_names:
                clear_all(folder_names)
            elif not folder_names:
                print("No folders have been created!")
                
        elif keyboard.is_pressed(key5):
            if folder_names:
                print(folder_names)
                time.sleep(1)
            elif not folder_names:
                print("No folders have been created yet!")
                
        elif keyboard.is_pressed(key3):
            print("Closing program....")
            time.sleep(3)
            done = True
            exit(code=0)
            
        elif keyboard.is_pressed(key4):
            print(f"Creating folders in {real_path}")
            folder_create(folder_names)
            
        elif keyboard.is_pressed(key1):
            help_menu()

        elif keyboard.is_pressed(key6):
            print("Enter the folder names you wish to create.")
            folder = input("")
            folder_names.append(folder)

        elif keyboard.is_pressed(key7):
            folder_exists(folder_names)
    
def folder_years(folder_names, year=None, count=0):
    while count < len(folder_names):
        if extras:
            folder_names[count] = folder_names[count] + " " + year
            count += 1

def clear_all(_list_):
    """Clears a list of folders entered by the user"""
    for item in _list_:
        _list_.remove(item)
    
        
def folder_create(folder_names, *extras):
    folders_copy = folder_names[:]
    """Creates the folders"""
    while folders_copy:
        print(folders_copy)
        time.sleep(1)
        folder = folders_copy.pop(0)
        print(f"finding {folder}....")
        time.sleep(1)
        print(f"Creating {folder} folder...")
        os.path.join(real_path)
        os.mkdir(folder)
        time.sleep(1)

        #Checks if the folders exist
        boolean = os.path.isdir(folder)
        if boolean == True:
            print(f"{folder} directory created.")
        else:
            print(f"Failed to find {folder} directory in {real_path}.")

def folder_exists(folder_names):
    """Checks if folders exists before deletion or handling"""
    for scan in range(len(folder_names)):
        for folder in folder_names:
            boolean = os.path.isdir(folder)
            if boolean == True:
                print(f"{folder} detected")
            else:
                print(f"{folder} not found")
    del_all_folders(folder_names)

def del_all_folders(folders):
    try:
        for num in range(len(folders)):
            for folder in folders:
                os.rmdir(folder)
    except FileNotFoundError:
        print("File not found, or has already been deleted")

def help_menu():
    print(f"\nPress {key2} to clear.")
    print(f"Press {key5} to show folders added.")
    print(f"Press {key3} to end the program.")
    print(f"Press {key4} when you have entered all your folder names.")
    print(f"Press {key7} to remove all created folders in {real_path}")


folder_init()
