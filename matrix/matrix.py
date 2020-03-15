class Matrix:
    def __init__(self, matrix_string):
         
        self.matrix_string = matrix_string.split('\n')
        self.matrix = [i.split(' ') for i in matrix_string]
        
    def row(self, index):
        
        return [int(i) for i in self.matrix[index-1]]

    def column(self, index):
        
        return [int(i[index-1]) for i in self.matrix]
        
