class Student:
    def __init__(self, s_id, s_name):
        self.id = s_id
        self.name = s_name
        self.cources = {}
        self.grades = {}
        self.cource_codes = []
    def enroll(self,c_code,c_name):
        self.cources[c_code] = c_name
        self.cource_codes.append(c_code)

    def rec_grades(self,c_code,grade):
        self.grades[c_code] = grade

    def gen_trans(self):
        print(f"Transcript of {self.name} (ID: {self.id}) \n")
        for i in self.cource_codes:
            print(f"{self.cources.get(i)} -  {self.grades.get(i)}")


class Cource:
    def __init__(self, cource_code, cource_name):
        self.c_code = cource_code
        self.c_name = cource_name


class Grade:

    def __init__(self,cource_code,grade):
        self.c_code=cource_code
        self.grade=grade


student1 = Student("1001","JH")
student1.enroll("MAT123","Mathematics")
student1.enroll("PHY123","Physics")
student1.enroll("CHY123","Chemistry")
student1.rec_grades("MAT123","A")
student1.rec_grades("PHY123","B")
student1.rec_grades("CHY123","B+")
student1.gen_trans()