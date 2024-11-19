import os

def create_user_file(filename="user_input.txt"):
    # Check if the file already exists; if not, create it
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("This is a sample text file.\nFeel free to modify its contents.")
        print(f"User file '{filename}' has been created.")
    else:
        print(f"File '{filename}' already exists.")

def read_and_write_file():
    # Create a sample file before starting
    create_user_file()

    # Ask the user for the input filename
    input_filename = input("Enter the filename to read from: ")
    
    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content by converting it to uppercase
        modified_content = content.upper()  # Example modification
        
        # Ask for the output filename
        output_filename = input("Enter the filename to write the modified content to: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Content has been successfully written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print("Error: The file could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()
