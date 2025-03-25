import os

def new_file():
    filename = input("Enter file name: ")
       
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    with open(filename, 'w') as file:
        print(f"File {filename} created successfully!")

def write_to_file():
    filename = input("Enter file name: ")
        
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    with open(filename, 'w') as file:
        content = input("Enter data to write: ")
        file.write(content)
        print("Data written successfully!")

def read_from_file():
    filename = input("Enter file name: ")
        
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    with open(filename, 'r') as file:
        content = file.read()
        print("\n--- File Contents ---")
        print(content)

def append_to_file():
    
    filename = input("Enter file name: ")
        
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    with open(filename, 'a') as file:
        content = input("Enter data to append: ")
        file.write("\n" + content)
        print("Data appended successfully!")

def list_files():
    
    print("\n--- Files in Current Directory ---")
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        print(file)

def file_menu():
    while True:
        print("\n--- File Operations (Custom Module) ---")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. List files in directory")
        print("6. Back to Main Menu")
        
        
        choice = int(input("Enter your choice: "))
            
        if choice == 1:
            new_file()
        elif choice == 2:
            write_to_file()
        elif choice == 3:
            read_from_file()
        elif choice == 4:
            append_to_file()
        elif choice == 5:
            list_files()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")
