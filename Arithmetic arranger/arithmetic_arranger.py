#This is the 1 st task from freecodecamp.org in Scientific Computing with Python section. 
#Developed by @warencome

#Import libraries
import sys


#Define function
def arithmetic_arranger(tasks):

    #Creating containers for calculation rows
    a_problem = []
    b_problem = []
    line_problem = []
    result_problem = []

    #Creating a loop
    for problem in tasks:

        #Number of problems check
        if len(tasks) > 5:
            print("Error: Too many problems.")
            break

        #Creating problem identifier
        task = problem

        #Searching for calculation sign
        if task.find("+") >= 0:
            sign = task.index("+")
        elif task.find("-") >= 0:
            sign = task.index("-")
        else:
            print("Error: Operator must be '+' or '-'.")
            sys.exit()

        sign_type = task[sign]

        #Searching for problem elements
        numbers = task.split(" " + sign_type + " ")

        #Checking problem elements correctness
        if numbers[0].isdigit() == 1 and numbers[1].isdigit() == 1:
            #Assigment of problem elements
            a = int(numbers[0])
            b = int(numbers[1])
        else:
            print("Error: Numbers must only contain digits.")
            sys.exit()

        #Checking the length of problem elements
        if len(str(a)) > 4 or len(str(b)) > 4:
            print("Error: Numbers cannot be more than four digits.")
            sys.exit()

        #Identifying sign
        if sign_type == "+":
            result = a + b
        else:
            result = a - b

        #Length of the longer number
        length = ( len( str( max(a, b) ) ) )

        #Formatting output of every problem
        a_problem.append((length + 2 - len( str(a) ) ) * " " + str(a) + "    ")
        b_problem.append((sign_type + ( length + 1 - len( str(b) ) ) * " " ) + str(b) + "    ")
        line_problem.append((length + 2 ) * "-" + "    ")
        result_problem.append((length + 2 - len( str(result) ) ) * " " + str(result) + "    ")


    #Adding formated problem rows to the list
    output_a = "".join(x for x in a_problem)
    output_b = "".join(x for x in b_problem)
    output_line = "".join(x for x in line_problem)
    output_result = "".join(x for x in result_problem)


    #Printing all output list to the console
    print(output_a + "\n" + output_b + "\n" + output_line + "\n" + output_result)


