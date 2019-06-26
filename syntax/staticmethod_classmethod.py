
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def go_to_school(self):
        print('{0} going to school'.format(self.name))

    @classmethod
    def go_to_school_class(cls):
        print('{0} going to school'.format(cls))

    @staticmethod
    def go_to_school_static():
        print('Student go to school')


ana = Student('Ana', 'Harvard')
ana.go_to_school()
ana.go_to_school_class()
ana.go_to_school_static()