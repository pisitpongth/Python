class Student:
    name = ""
    study_year = 0
    score = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_study_year(self, study_year):
        self.study_year = study_year

    def get_study_year(self):
        return self.study_year

    def get_score(self):
        return self.score

    def add_point(self, point):
        self.score += point
        print(self.get_name(), " got ", point, " points")

    def get_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "F"
