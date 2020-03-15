class School:
    def __init__(self ,shool_roster = {}):
        
        self.shool_roster = shool_roster

    def add_student(self, name, grade):
        
        self.school_roster[name] = grade

    def roster(self):
        
        return sorted(list(self.school_roster.keys()))

    def grade(self, grade_number):
        
        return sorted([i for i in self.shool_roster
                       if self.shool_roster.get(i) == grade_number])
