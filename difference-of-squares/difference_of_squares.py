def square_of_sum(number):
    square=0
    for i in range(number+1):
        square+=i
    square**=2
    return square

def sum_of_squares(number):
    sum_square=0
    for i in range(number+1):
        sum_square+=i**2
    return sum_square


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
