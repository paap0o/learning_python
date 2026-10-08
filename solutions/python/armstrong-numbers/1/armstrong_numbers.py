def is_armstrong_number(number):
    number_of_digits = len(str(number))

    total = 0 

    for digit in str(number):
        total = total + int (digit)** number_of_digits

    return total == number

    
