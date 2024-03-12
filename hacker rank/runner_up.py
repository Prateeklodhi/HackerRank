if __name__ == '__main__':
    list_of_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_of_students.append([name, score])
    
    list_of_students.sort(key=lambda item: item[1], reverse=True)
    min_marks = list_of_students[0][1]
    for student in list_of_students:
        if min_marks > student[1]:
            second_min = min_marks
            min_marks = student[1]
    runner_up_students = sorted([student for student in list_of_students if second_min==student[1]])
    for student in runner_up_students:
        print(student[0])
   
    