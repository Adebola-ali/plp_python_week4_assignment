def read_and_write_file():
    # prompt user for the file name
    input_filename = input('Enter filename to read from: ')

    try:
        # Attempt to open and read the file
        with open(input_filename,'r') as file:
            content = file.read()

        # Modify the content
        modified_content = content.upper()

        # Ask for output filename
        output_filename = input('Enter the filename to write the modified content to: ')

        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            content = file.write(modified_content)

        print(f'{output_filename} content has been successfully written to {output_filename}')

    except FileNotFoundError:
        print(f"Error: The file'{input_filename}' does not exist")
    except IOError:
        print("Error: The file could not be read or written.")           
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# call the function
read_and_write_file()  