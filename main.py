
from funcionalities import *

# A main function is defined.
def main ():

    # the main list where student information is stored
    student_list = []
    
    # print the main UI of system
    print('''
             ================================
              WELCOME TO STUDENTS MANAGEMENT
                         SYSTEM
             ================================
          ''')
    
    init_sys = input("Do you want to start the system? (Y/N): ").lower()
    print("=" * 55)

    # This is where the main program loop runs.
    try:
        while init_sys == "y":

            # print the menu option UI
            print('''
                           - MENU -
                    1. Register new student
                    2. Consult student list
                    3. Search student
                    4. Update student Info
                    5. Remove student Info
                    6. Exit
                ---------------------------
                ''')
            
            ACTIVE = True
            option = int(input("Choose an option (1 - 6): "))

            if option < 1 or option > 7:
                print("ERROR: Choose a valid option (1 -6)!")

            # A MATCH/CASE control structure is defined to manage the user's choice.
            match option:
                
                # In the first case, the logic of the "register_student()" function is built.
                case 1:

                    i = 1

                    while ACTIVE:
                        print(f'''
                            - REGISTER STUDENT -
                                register # {i}
                        =============================
                        ''')

                        id = int(input("Introduce the ID's student (Number sequence): "))
                        name = input("Introduce the student's name: ")
                        age = int(input("Introduce the student's age: "))
                        course = input("What is the student's program or course?: ")
                        state = bool(int(input("What is the student's status?(Write 1 -> active and 0 -> inactive): ")))

                        i += 1

                        register_student(student_list, id, name, age, course, state)

                        print("-" * 50)
                        ask = input("Do you want to register more students? (y/n): ").lower()
                        print("-" * 50)

                        if ask != "y":
                            break
                                     
                # In the second case, the logic is built that will be responsible for displaying a list of the students' information.
                # Here not implemented a function.
                case 2:
                    print(f'''
                             - STUDENT'S LIST -
                        =============================
                        ''')
                    
                    if not student_list:
                        print("There are no registered students.!...")
                    else:
                        for i, student in enumerate(student_list):

                            print(f'''
                                STUDENT # {i + 1}
                            ===================
                                ID: {student['id']}
                                Name: {student['name']}
                                Age: {student['age']}
                                Course: {student['course']}
                                State: {student['state']}
                            -------------------------------
                                ''')

                # In the third case, the logic is built that will be responsible for requesting a name and searching for the information of said student.      
                case 3:
                    print(f'''
                             - SEARCH STUDENT -
                        =============================
                        ''')
                    
                    name = input("Enter the student's name or ID to search: ")
                    print("=" * 50)

                    found = search_student(student_list, name)

                    if found:
                        print(f'''
                              - STUDENT FOUND -
                              =================
                                ID: {student['id']}
                                Name: {student['name']}
                                Age: {student['age']}
                                Course: {student['course']}
                                State: {student['state']}
                              ---------------------
                           ''')
                    else:
                        print("The student not Found...")
                
                # In the fourth case, the logic was built that will be responsible for 
                # updating the student's information, such as their Program/course and their status (active(True) and inactive(False))
                case 4:
                    print(f'''
                          - UPDATE STUDENT'S INFO -
                        =============================
                        ''')
                    
                    name = input("Enter the student's name to update: ")
                    print("=" * 50)

                    new_course = input("Enter the new program to update: ")
                    new_state = bool(int(input("Enter the new status to update (1 (active) or 0 (inactive)): ")))

                    updated = update_info(student_list, name, new_course, new_state)

                    if updated:
                        print("The student's info is updated successfully!")
                    else:
                        print("The student not found and his info!")

                # In the fifth case, the logic is simply based on being able to delete the complete information of any student from the main list.
                case 5:
                    print(f'''
                          - REMOVE STUDENT'S INFO -
                        =============================
                        ''')
                    
                    name = input("Enter the student's name to remove: ")
                    print("=" * 50)

                    removed = remove_student(student_list, name)

                    if removed:
                        print("The student's info is removed succesfully!")
                    else:
                        print("The student's info don't exist!")

                # In the sixth case, the entire system shuts down and displays a thank you message.
                case 6:
                    print('''
                           ===============================
                            - THANKS FOR USE OUR SYSTEM -
                           ===============================
                          ''')
                    
                    break
    except ValueError:
        print("Enter valid information into the program...")

# The main function is called to be executed.
if __name__ == "__main__":
    main()