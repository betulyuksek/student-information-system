students = [
    {
        "name": "Resul",
        "surname": "Yüksek",
        "no": "190701",
        "grades": {"midterm_grade":76, "final_grade":85}
    },
    {
        "name": "Sıla",
        "surname": "Cömert",
        "no": "190702",
        "grades": {"midterm_grade":65, "final_grade":78} 
    },
    {
        "name": "Seda",
        "surname": "Dağlar",
        "no": "190703",
        "grades": {"midterm_grade":78, "final_grade":64} 
    },
    {
        "name": "Halil",
        "surname": "Çelik",
        "no": "190704",
        "grades": {"midterm_grade":47, "final_grade":54} 
    },
    {
        "name": "Eda",
        "surname": "Çevik",
        "no": "190705",
        "grades": {"midterm_grade":74, "final_grade":82} 
    },
    {
        "name": "Buse",
        "surname": "Yılmaz",
        "no": "190706",
        "grades": {"midterm_grade":76, "final_grade":89} 
    },
    {
        "name": "Efe",
        "surname": "Gökalp",
        "no": "190707",
        "grades": {"midterm_grade":80, "final_grade":80} 
    },
    {
        "name": "Asya",
        "surname": "Erdal",
        "no": "190708",
        "grades": {"midterm_grade":53, "final_grade":45} 
    },
    {
        "name": "Ahmet",
        "surname": "Erol",
        "no": "190709",
        "grades": {"midterm_grade":45, "final_grade":40} 
    },
    {
        "name": "Deniz",
        "surname": "Çınar",
        "no": "190710",
        "grades": {"midterm_grade":64, "final_grade":50} 
    },
    {
        "name": "Umay",
        "surname": "Mira",
        "no": "190711",
        "grades": {"midterm_grade":87, "final_grade":65} 
    },
    {
        "name": "Elvin",
        "surname": "Açıkgöz",
        "no": "190712",
        "grades": {"midterm_grade":66, "final_grade":75} 
    },
    {
        "name": "Mehmet",
        "surname": "Ilgaz",
        "no": "190713",
        "grades": {"midterm_grade":65, "final_grade":70} 
    },   
    {
        "name": "Mustafa",
        "surname": "Demir",
        "no": "190714",
        "grades": {"midterm_grade":82, "final_grade":75} 
    },   
    {
        "name": "Esra",
        "surname": "Aslan",
        "no": "190715",
        "grades": {"midterm_grade":90, "final_grade":85} 
    },
    {
        "name": "Osman",
        "surname": "Ay",
        "no": "190716",
        "grades": {"midterm_grade":36, "final_grade":45} 
    },
    {
        "name": "Eslem",
        "surname": "Kurt",
        "no": "190717",
        "grades": {"midterm_grade":75, "final_grade":65} 
    },
    {
        "name": "Sena",
        "surname": "Avcı",
        "no": "190718",
        "grades": {"midterm_grade":54, "final_grade":45} 
    },
    {
        "name": "Tolga",
        "surname": "Zengin",
        "no": "190719",
        "grades": {"midterm_grade":85, "final_grade":70} 
    },
    {
        "name": "Büşra",
        "surname": "Uslu",
        "no": "190720",
        "grades": {"midterm_grade":75, "final_grade":65} 
    }
]


def calculate(student):
        average = (student["grades"]["midterm_grade"] * 0.4) + (student["grades"]["final_grade"] * 0.6 )
        return average


def add_student():
    n_st_name = input("Student name: ")
    n_st_surname = input("Student surname: ")
    n_st_no = input("Student number: ")
    for student in students:
        if n_st_no == student["no"]:
            print("The student has already been added.")
            return
    else:
        midterm_valid = False
        while not midterm_valid:
            n_st_m_grade = (input("Midterm grade: "))
            if n_st_m_grade.isdigit():
                n_st_m_grade = int(n_st_m_grade)
                if n_st_m_grade >= 0 and n_st_m_grade <= 100:
                    print("Valid grade.")
                    midterm_valid = True
                else:
                    print("The grade must be between 0 and 100.")
            else:
                print("Please enter a numeric value.")

        final_valid = False
        while not final_valid:
            n_st_f_grade = (input("Final grade:"))
            if n_st_f_grade.isdigit():
                n_st_f_grade = int(n_st_f_grade)
                if n_st_f_grade >= 0 and n_st_f_grade <= 100:
                    print("Valid grade.")
                    final_valid = True
                else:
                    print("The grade must be between 0 and 100.")
            else:
                print("Please enter a numeric value.")


        if midterm_valid and final_valid:
            st_data = {
              "name": n_st_name, 
              "surname": n_st_surname, 
              "no": n_st_no, 
              "grades": {
                  "midterm_grade": n_st_m_grade, 
                  "final_grade": n_st_f_grade
                   }
               }
            students.append(st_data)
            print(f"{st_data['name']} {st_data['surname']} was added.")
        else:
            print("Student could not be added because of invalid grades.")
        
        
def student_list():
    for student in students:
        print(student["no"], student["name"], student["surname"])


def calculate_grade_average():
    for student in students:
        average = calculate(student)
        print(f"{student['name']} {student['surname']} - Grade average: {average:.2f}") 


def find_student():
    st_no = input("Enter the student number: ")
    for student in students:
        if st_no == student["no"]:
            print(f"Student Number: {student['no']}\nName : {student['name']} {student['surname']}\nGrade Average: {calculate(student)}")
            break
    else:
        print("Student not found.")


def del_student():
    who_del = input("Enter the number of the student you want to delete: ")
    for student in students:
        if who_del == student["no"]:
            students.remove(student)
            print("Student deleted.")
            break
    else:
        print("Student not found.")

def average_class():
    total = 0
    for student in students:
        average = calculate(student)
        total += average

    if len(students) == 0:
        return 0
    else:
        c_average = total / len(students)
        return c_average


def find_successful_students():
    successful_student = []
    for student in students:
        average = calculate(student)
        if average >= 50:
            successful_student.append(f"{student['no']} - {student['name']} {student['surname']} - Average: {average:.2f}")
    for s_st in successful_student:
        print(s_st)


def update():
    st_no = input("Enter the student number: ")
    for student in students:
        if st_no == student["no"]:
            your_c = input("Which grade do you want to update?")
            if your_c == "midterm grade":
                n_m_grade = (input("New grade: "))
                if n_m_grade.isdigit():
                    n_m_grade = int(n_m_grade)

                    if n_m_grade >= 0 and n_m_grade <= 100:
                        student["grades"]["midterm_grade"] = n_m_grade
                        print("Grade updated successfully")
                    else:
                        print("The grade must be between 0 and 100.")
                else:
                    print("Please enter a numeric value.")

            elif your_c == "final grade":
                n_f_grade = (input("New grade: "))

                if n_f_grade.isdigit():
                    n_f_grade = int(n_f_grade)

                    if n_f_grade >= 0 and n_f_grade <= 100:
                        student["grades"]["final_grade"] = n_f_grade
                        print("Grade updated successfully")
                    else:
                        print("The grade must be between 0 and 100.")
                else:
                    print("Please enter a numeric value.")
            else:
                print("You have entered an invalid grade type.")
            break
            
    else:
        print("Student not found.")


while True:
    print()
    print("STUDENT INFORMATION SYSTEM")
    print("=============================")
    print("1- Add a Student")
    print("2- Student Listing")
    print("3- Calculate Student Grade Averages")
    print("4- Find a Student")
    print("5- Delete a Student")
    print("6- Calculate Class Average")
    print("7- List Successful Students")
    print("8- Updating Grade")
    print("0- Log Out")

    your_choice = input("Select the option you would like to choose: ")

    if your_choice == "1":

        add_student()

    elif your_choice == "2":
        student_list()

    elif your_choice == "3":
        calculate_grade_average()

    elif your_choice == "4":
        find_student()

    elif your_choice == "5":
        del_student()

    elif your_choice == "6":
        print(average_class())

    elif your_choice == "7":
        find_successful_students()

    elif your_choice == "8":
        update()

    elif your_choice == "0":
        print("Logged out of the system")
        break

    else:
        print("Invalid selection.")
