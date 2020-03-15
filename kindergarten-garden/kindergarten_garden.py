class Garden:
    def __init__(self, diagram, students):
        
        self.diagram = diagram.split('\n') 
        self.students = ['Alice', 'Bob', 'Charlie', 'David',
                         'Eva', 'Fred', 'Ginny', 'Harriet',
                         'Ileana', 'Joseph', 'Kincaid','Larry']
    
    def plants(self,student):
        
            plants = {'G':'Glover','C':'Clover','R':'Radishes','V':'Violets'}
            index = self.students.index(student)*2
            
            plant_stu = self.diagram[0][index]+self.diagram[0][index+1]+self.diagram[1][index]+self.diagram[1][index+1]
            
            final_plants = []
            temp = 0
                        
            for i in plant_stu:
                
                final_plants[temp] = plants[i]
                temp+=1
                
            return final_plants
                
            
            
        
        
        