# Grade Calculator Application. i Created a dictionary to store all students and their marks

students = {
 
}

def add_student(student_name):
    
   # This is a Function to add a new student with their marks .Parameter: student_name - the name of the student to add
  
    # Ask the user how many marks they want to enter for this student
    num_marks = int(input(f"How many marks do you want to add for {student_name}? "))
    
    # Create an empty list to store all the marks for this student
    marks_list = []
    
    # Loop to get each mark from the user
    for i in range(1, num_marks + 1):
        # Ask user to enter each mark, one by one
        mark = float(input(f"Please enter mark {i}: "))
        # Add the mark to our list
        marks_list.append(mark)
    
    # Add the student and their marks to the students dictionary
    students[student_name] = marks_list
    
    # Confirm that the student was added successfully
    print("New user successfully added")

def calculate_marks(student_name):

   # Function is  to calculate the average of a student's marksParameter: student_name the name of the student .this brings the average of all the student's marks
    
    # Check if the student exists in our dictionary
    if student_name in students:
        # Get the list of marks for this student
        marks = students[student_name]
        
        # Calculate the sum of all marks
        total = sum(marks)
        
        # Calculate the average by dividing total by number of marks
        average = total / len(marks)
        
        # Return the average
        return average
    else:
        # If student doesn't exist, return None
        return None

def print_menu(): # def function used to show the menu and brings back what the user chose
    
   
    print("\nWelcome to Grade Calculator")  # Print the welcome message and menu options
    print("1. Add new student")
    print("2. List all the added students")
    print("3. Calculate student average")
    print("0. Close application")
    
    # Get the user's choice and return it
    choice = input("What would you like to do? ")
    return choice

def main():  #main function
    
    
    while True: # Starts an infinite loop for continuous user input
        # Call the print_menu function to show options and get user choice
        user_choice = print_menu()
        
        # Checks what the user selected and acts
        if user_choice == "1":
            # which is Option 1: Add new student
            # 2.Ask for student name
            student_name = input("Please enter the name of the new student: ")
            # Call the add_student function with the student's name
            add_student(student_name)
            
        elif user_choice == "2":  
            # Option 2: List all students 
            print("\nAll Students:")
            # Loop through all student names in the dictionary
            for name in students:
                # Print each student name
                print(name)
                
        elif user_choice == "3":
            # Option 3: Calculate student average
            # Ask for student name
            student_name = input("Enter the student name: ")
            # Call the calculate_marks function
            average = calculate_marks(student_name)
            
            # Check if the function returned a valid average
            if average is not None:
                # Print the student's average
                print(f"{student_name} has an average of {average}%")
            else:
                # if the Student not found it will print
                print(f"Student {student_name} not found.")
                
        elif user_choice == "0":
            # Option 0: Close application
            print("Bye, Bye")
            # Break out of the loop to end the program
            break
            
        else:
            # Any other input is invalid1
            print("Invalid selection")

# Run the main application
# This checks if this file is being run directly (not imported) like clicking on desktop. if it was another name and not main its imported
if __name__ == "__main__":
    # Start the main function
    main() # if we had just this the program would akway run