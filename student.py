import xml.etree.ElementTree as ET

tree = ET.parse('Students.xml')
root = tree.getroot()

choice = 0

while choice < 5:
    print("1.Add Student\n2.Delete Student\n3.View Student\n4.View All Students\n5.Exit")
    choice = int(input())
    if choice == 1:
        name = input("Enter name of student: ")
        rollno = input("Enter rollno of student: ")
        classs = input("Enter class of student: ")
        div = input("Enter div of student: ")
        n = int(input("Enter your number of courses: "))
        courses = []
        for i in range(n):
            course = input("Enter course name: ")
            courses.append(course)
        new_student = ET.Element('Student')
        name1 = ET.SubElement(new_student, 'name')
        name1.text = name
        rollno1 = ET.SubElement(new_student, 'rollno')
        rollno1.text = rollno
        class1 = ET.SubElement(new_student, 'class')
        class1.text = classs
        div1 = ET.SubElement(new_student, 'div')
        div1.text = div
        courses1 = ET.SubElement(new_student, 'courses')
        for i in range(n):
            course = ET.SubElement(courses1, 'course')
            course.text = courses[i]
        root.append(new_student)
        tree.write('Students.xml')
        print("Record Added Successfully\n")
    
    elif choice == 2:
        rollno = input("Enter rollno of student to delete student: ")
        student = root.find("Student[rollno='{}']".format(rollno))
        root.remove(student)
        tree.write('Students.xml')
        print('Record Deleted Successfully\n')
    
    elif choice == 3:
        rollno = input("Enter rollno of student: ")
        student = root.find("Student[rollno='{}']".format(rollno))
        print("Name: ", student.find('name').text)
        print("Roll NO:", student.find('rollno').text)
        print('Class :', student.find('class').text)
        print("Div: ", student.find('div').text)
        courses = student.find('courses')
        courses = courses.findall('course')
        courses_names = [course.text for course in courses]
        print("Courses: ", courses_names)

    elif choice == 4:
        for student in root.findall('Student'):
            print("\nName: ", student.find('name').text)
            print("Roll NO:", student.find('rollno').text)
            print('Class :', student.find('class').text)
            print("Div: ", student.find('div').text)
            courses = student.find('courses')
            courses = courses.findall('course')
            courses_names = [course.text for course in courses]
            print("Courses: ", courses_names)

        
        

