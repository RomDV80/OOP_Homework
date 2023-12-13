class Student:
    """Класс Студенты"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = float()

    def __str__(self):
        """Метод подсчета средней оценки за домашние задания студентов"""
        grade_count = 0
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        for val in self.grades:
            grade_count += len(self.grades[val])
        self.average = round(sum(map(sum, self.grades.values())) / grade_count, 1)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n' 
                f'Средняя оценка за домашние задания: {self.average}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}\n')

    def rate_hw(self, lecturer, course, grade):
        """Метод выставления оценок лекторам от студентов за лекции"""
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # def comparison(self, other):
    #     """Метод сравнения"""
    #     if not isinstance(other, Student):
    #         print('Сравнение не может быть выполнено')
    #         return
    #     if self.average > other.average:
    #         return f'Победитель: {self.name} {self.surname}\n'
    #     if self.average < other.average:
    #         return f'Победитель: {other.name} {other.surname}\n'
    #     if self.average == other.average:
    #         return f'Победила дружба\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение не может быть выполнено')
            return
        return self.average < other.average

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение не может быть выполнено')
            return
        return self.average > other.average

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Сравнение не может быть выполнено')
            return
        return self.average == other.average


class Mentor:
    """Класс Менторы"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс Лекторы. Унаследован от класса Менторы"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.grades = {}
        self.average = float()

    def __str__(self):
        """Метод подсчета средней оценки Лекторам за лекции от студентов"""
        grade_count = 0
        courses_attached = ', '.join(self.courses_attached)
        for val in self.grades:
            grade_count += len(self.grades[val])
        self.average = round(sum(map(sum, self.grades.values())) / grade_count, 1)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average}\n'
                f'Ведет лекции по предмету: {courses_attached}\n')

    # def comparison(self, other):
    #     """Метод сравнения"""
    #     if not isinstance(other, Lecturer):
    #         print('Сравнение не может быть выполнено')
    #         return
    #     if self.average > other.average:
    #         return f'Победитель: {self.name} {self.surname}\n'
    #     if self.average < other.average:
    #         return f'Победитель: {other.name} {other.surname}\n'
    #     if self.average == other.average:
    #         return f'Победила дружба\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение не может быть выполнено')
            return
        return self.average < other.average

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение не может быть выполнено')
            return
        return self.average > other.average

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение не может быть выполнено')
            return
        return self.average == other.average


class Reviewer(Mentor):
    """Класс Проверяющие. Унаследован от класса Менторы"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        courses_attached = ', '.join(self.courses_attached)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Проверяет ДЗ по предмету: {courses_attached}\n')

    def rate_hw(self, student, course, grade):
        """Метод выставления оценок за домашние задания студентов"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Из квиза (экземпляры класса)
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# Из квиза оценки
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Из квиза (экземпляры класса)
best_lecturer = Lecturer('Ruoy', 'Eman')
best_lecturer.courses_attached += ['Python']

cool_student = Student('Some', 'Buddy', 'your_gender')
cool_student.courses_in_progress += ['Python']

# Из квиза оценки
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)

# Проверяющие (экземпляры класса)
reviewer_1 = Reviewer('Иван', 'Иванов')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Михаил', "Мишин")
reviewer_2.courses_attached += ['Git']

# Лекторы (экземпляры класса)
lecturer_1 = Lecturer('Сергей', 'Сергеев')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Александр', 'Александров')
lecturer_2.courses_attached += ['Git']

lecturer_3 = Lecturer('Семен', 'Семенов')
lecturer_3.courses_attached += ['Git']


# Студенты (экземпляры класса)
student_1 = Student('Клементий', 'Афанасьев', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Глафира', 'Петрова', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Тимур', 'Гайдар', 'your_gender')
student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['Git']
student_3.finished_courses += ['Введение в программирование']

# Оценки Лекторов за лекции от Студентов
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 5)

student_1.rate_hw(lecturer_2, 'Git', 10)
student_1.rate_hw(lecturer_2, 'Git', 10)
student_1.rate_hw(lecturer_2, 'Git', 10)

student_2.rate_hw(lecturer_1, 'Python', 10)
student_2.rate_hw(lecturer_1, 'Python', 10)
student_2.rate_hw(lecturer_1, 'Python', 10)

student_2.rate_hw(lecturer_2, 'Git', 10)
student_2.rate_hw(lecturer_2, 'Git', 10)
student_2.rate_hw(lecturer_2, 'Git', 10)

student_1.rate_hw(lecturer_3, 'Git', 10)
student_1.rate_hw(lecturer_3, 'Git', 10)
student_1.rate_hw(lecturer_3, 'Git', 10)

student_2.rate_hw(lecturer_3, 'Git', 10)
student_2.rate_hw(lecturer_3, 'Git', 5)
student_2.rate_hw(lecturer_3, 'Git', 10)

# Оценки Студентов за ДЗ от Проверяющих
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)

reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)

reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Git', 10)

reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Python', 10)

reviewer_2.rate_hw(student_3, 'Git', 10)
reviewer_2.rate_hw(student_3, 'Git', 10)
reviewer_2.rate_hw(student_3, 'Git', 10)


print(best_student.grades)
print(best_lecturer.grades)
print(f'Проверяющие:\n\n{reviewer_1}\n{reviewer_2}')
print(f'Лекторы:\n\n{lecturer_1}\n{lecturer_2}\n{lecturer_3}')
print(f'Студенты:\n\n{student_1}\n{student_2}')
# print(f'Сравнение по средней оценке Лекторов от Студентов: '
#       f'{lecturer_1.name} {lecturer_1.surname}'
#       f' ({lecturer_1.average} Баллов) '
#       f'VS {lecturer_2.name} {lecturer_2.surname}'
#       f' ({lecturer_2.average} Баллов)\n'
#       f'{lecturer_1.comparison(lecturer_2)}')
# print(f'Сравнение по средней оценке за ДЗ Студентов: {student_1.name} {student_1.surname}'
#       f' ({student_1.average} Баллов)'
#       f' VS {student_2.name} {student_2.surname}'
#       f' ({student_2.average} Баллов)\n'
#       f'{student_1.comparison(student_2)}\n')
print(f'Сравнение по средней оценке Лекторов от студентов: {lecturer_1.name} {lecturer_1.surname}'
      f' {lecturer_1.average} '
      f'< {lecturer_2.name} {lecturer_2.surname} {lecturer_2.average} = {lecturer_1 < lecturer_2}')
print(f'Сравнение по средней оценке за ДЗ студентов: {student_1.name} {student_1.surname} {student_1.average}'
      f' < {student_2.name} {student_2.surname} {student_2.average} = {student_1 < student_2}\n')

list_students = [student_1, student_2]
list_lecturers = [lecturer_1, lecturer_2, lecturer_3]


def all_students_rating(list_students, course_name):
    """Функция подсчета средней оценки всех Студентов по конкретному курсу"""
    average_students_all = []
    if list_students:
        for student in list_students:
            for key, value in student.grades.items():
                if key == course_name:
                    average_students_all += value
    return round(sum(average_students_all) / len(average_students_all), 1)


print(f'Средняя оценка Студентов по предмету {"Python"}: '
      f'{all_students_rating(list_students, 'Python')} Баллов')
print(f'Средняя оценка Студентов по предмету {"Git"}: '
      f'{all_students_rating(list_students, 'Git')} Баллов\n')


def all_lecturers_rating(list_lecturers, course_name):
    """Функция подсчета средней оценки всех Лекторов по конкретному курсу"""
    average_lecturers_all = []
    if list_students:
        for lecturer in list_lecturers:
            for key, value in lecturer.grades.items():
                if key == course_name:
                    average_lecturers_all += value
    return round(sum(average_lecturers_all) / len(average_lecturers_all), 1)


print(f'Средняя оценка Лекторов по предмету {"Python"}: '
      f'{all_lecturers_rating(list_lecturers, 'Python')} Баллов')
print(f'Средняя оценка Лекторов по предмету {"Git"}: '
      f'{all_lecturers_rating(list_lecturers, 'Git')} Баллов')

