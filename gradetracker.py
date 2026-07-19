
students_grades = []

while True:
    print ("Press '1' to Add student and grade\n",
           "Press '2' to Display student, their grades and average\n",
           "Press 'q' to quit " )
    u_input = input(">")
    
    if u_input.lower() == "q":
        break

    else:
        if u_input == '1':
            while True:
                student = input("Enter student name/press 'q' to quit: ")
                if student.lower() == 'q':
                    break
                else:
                    grade = float(input("Enter the students grades: "))
                    students_grades.append([student,grade])
        
        if u_input == '2':
            if not students_grades:
                print("No students added yet")
                continue
            else:
                for stu_grade in students_grades:
                    print(f"{stu_grade[0]} - {stu_grade[1]}")
                
                average = 0
                count = 0
                for ave in students_grades:
                    count += ave[1]
                average = count / len(students_grades)

                print(f"the class average is:{average: .2f}")




    
    
    