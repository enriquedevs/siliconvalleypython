
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def go_to_school(self):
        return '{0} goes to school {1}'.format(self.name, self.school)


class WorkingStudent(Student):
    def __init__(self, name, school, company):
        super().__init__(name, school)
        self.company = company

    def go_to_work(self):
        return self.go_to_school() + ' and works in {0}'.format(self.company)


roger = WorkingStudent('Roger', 'Oxford', 'Google')
print(roger.go_to_school())
print(roger.go_to_work())