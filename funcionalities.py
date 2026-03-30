def register_student (student_list, id, name, age,  course, state = bool):

    for student in student_list:
        if student["name"].lower() == name.lower():
            return False
        
    student_info = {
        "id"  : (id),
        "name" : name,
        "age" : age,
        "course" : course,
        "state" : state
    }

    student_list.append(student_info)

    return True

def show_list (student_list):
    
    list = []
    for student in student_list:

        line = f'''
            ID: {student["id"]}
            Name: {student['name']}
            Age: {student["age"]}
            Course: {student["course"]}
            State: ({student["state"]}
        '''

        list.append(line)

    return list

def search_student (student_list, name):
        
        for student in student_list:
            if student["name"].lower() == name.lower():
                return student
            
        return None

def update_info (student_list, name, new_course = None, new_state = None):

    for student in student_list:
        if student["name"].lower() == name.lower():
            if new_course is not None:
                student["course"] = new_course
            if new_state is not None:
                student["state"] = new_state
            
            return True
        
    return False

def remove_student (student_list, name):

    for i, student in enumerate(student_list):
        if student["name"].lower() == name.lower():
            del student_list[i]
            return True
        
    return False