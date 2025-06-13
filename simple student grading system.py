#Student grading system
#Change the value of the variable 'grade' to test different conditions

def grade_input():
    try:
        student_grade = int(input("Enter student grade: "))
        return student_grade
    except ValueError:
            print("An error occurred, please enter a valid number.")
            return grade_input() # Ask again if input is invalid

def grade_logic(student_grade): 
    #Determine and print the grade based on the students score
    if 81 <= student_grade <=100:
        print("You got an A")
    elif 61 <= student_grade <=80:
        print("You got a B")
    elif 40 <= student_grade <=60:
        print("You got a C")
    elif 20 <= student_grade <=39:
        print("You got a D")
    elif 0 <= student_grade <=19:
        print("You got an F")
    else:
        print("Invalid grade entered. Please enter a grade between 0 and 100.")
        
grade = grade_input() #Get the student grade from user input
grade_logic(grade) #Print the letter grade assigned to it