

# Task 1: File Creation and Writing
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text, including a mix of strings and numbers
        file.write("Hello, this is the first line.\n")
        file.write("The second line contains a number: 1234.\n")
        file.write("The third line is a final message.\n")
    print("File 'my_file.txt' created and initial content written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error while writing to the file: {e}")

# Task 2: File Reading and Display
try:
    # Open the file in read mode ('r') and display its contents
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("\nContents of 'my_file.txt' after initial writing:\n")
    print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error while reading the file: {e}")

# Task 3: File Appending
try:
    # Open the file in append mode ('a') and add three more lines
    with open("my_file.txt", "a") as file:
        file.write("Fourth line: appending more text.\n")
        file.write("Fifth line: adding another number: 5678.\n")
        file.write("Sixth line: final line after appending.\n")
    print("\nAdditional lines appended to 'my_file.txt'.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error while appending to the file: {e}")

# Task 4: Error Handling - Reading and displaying the updated content
try:
    # Open the file again in read mode to check the final content
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
    print("\nContents of 'my_file.txt' after appending:\n")
    print(updated_content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error while reading the file: {e}")

finally:
    print("\nFile handling operations completed.")
