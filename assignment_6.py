


# que 2

def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is undefined"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
    
print (calculator(5, 3, 'add'))



# que 4

def rat_pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)
rat_pattern(5)