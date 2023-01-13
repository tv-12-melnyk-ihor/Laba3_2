from abc import ABC, abstractmethod


class ICourse(ABC):

    def __init__(self, name, topics):
        self.name = name
        self.teachers = []
        self.topics = topics

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ICourse):

    def __init__(self, name, topics):
        ICourse.__init__(self, name, topics)

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ICourse):

    def __init__(self, name, topics):
        ICourse.__init__(self, name, topics)

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class LocalCourse(ILocalCourse):

    def __add__(self, other):
        self.teachers.append(other)

    def __str__(self):
        teachers_names = []
        for teacher in self.teachers:
            teachers_names.append(teacher.name)
        return f'Local course name: {self.name}' \
               f'\nCourse teachers: {teachers_names}' \
               f'\nCourse topics: {self.topics}'


class OffsiteCourse(IOffsiteCourse):

    def __add__(self, other):
        self.teachers.append(other)

    def __str__(self):
        teachers_names = []
        for teacher in self.teachers:
            teachers_names.append(teacher.name)
        return f'Offsite course name: {self.name}' \
               f'\nCourse teachers: {teachers_names}' \
               f'\nCourse topics: {self.topics}'


class ITeacher(ABC):

    def __init__(self, name):
        self.name = name
        self.courses = []

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Teacher(ITeacher):

    def __add__(self, other):
        self.courses.append(other)

    def __str__(self):
        courses_names = []
        for course in self.courses:
            courses_names.append(course.name)
        return f'Teacher name: {self.name}' \
               f'\nThey teach such courses as {courses_names}'


class ICourseFactory(ABC):

    @abstractmethod
    def create_teacher(self) -> ITeacher:
        pass

    @abstractmethod
    def create_local_course(self) -> ILocalCourse:
        pass

    @abstractmethod
    def create_offsite_course(self) -> IOffsiteCourse:
        pass

    @abstractmethod
    def course_plus_teacher(self, t, c):
        pass


class CourseFactory(ICourseFactory):

    def __init__(self):
        self.teachers = []
        self.courses = []

    def create_teacher(self, name) -> ITeacher:
        t = Teacher(name)
        self.teachers.append(t)
        return t

    def create_local_course(self, name, topics) -> ILocalCourse:
        lc = LocalCourse(name, topics)
        self.courses.append(lc)
        return lc

    def create_offsite_course(self, name, topics) -> IOffsiteCourse:
        oc = OffsiteCourse(name, topics)
        self.courses.append(oc)
        return oc

    def course_plus_teacher(self, c, t):
        c + t
        t + c


if __name__ == '__main__':
    factory = CourseFactory()
    print()
    t1 = factory.create_teacher("Степанчук Галина Вікторівна")
    t2 = factory.create_teacher("Ковальчук Віталій Михайлович")
    t3 = factory.create_teacher("Шевченко Дмитро Олександрович")
    t4 = factory.create_teacher("Романенко Олена Григорівна")
    t5 = factory.create_teacher("Сіплюсплюсенко Антон Володимирович")

    lc1 = factory.create_local_course("Основи Програмування", ["Лекція 1", "Лекціяs 2", "Лекція 3", "Лекція 4"])
    lc2 = factory.create_local_course("Структури даних", ["Лекція 1", "Лекціяs 2", "Лекція 3", "Лекція 4", "Лекція 5"])
    lc3 = factory.create_local_course("Компоненти програмної інженерії", ["Лекція 1", "Лекціяs 2", "Лекція 3"])
    oc1 = factory.create_offsite_course("Математичний аналіз", ["Лекція 1", "Лекціяs 2", "Лекція 3", "Лекція 4"])

    factory.course_plus_teacher(lc1, t5)
    factory.course_plus_teacher(lc2, t1)
    factory.course_plus_teacher(lc2, t2)
    factory.course_plus_teacher(lc3, t2)
    factory.course_plus_teacher(lc3, t3)
    factory.course_plus_teacher(oc1, t4)

    for t in factory.teachers:
        print(t, "\n")

    for c in factory.courses:
        print(c, "\n")