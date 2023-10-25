def function_for_indices(index,operation):
    result = single_operation(operation[index-1],operation[index],operation[index+1])
    operation.pop(index-1)
    operation.pop(index-1)
    operation[index-1] = result
    return operation

def single_operation(factor_1,operation_to_do,factor_2):
    if operation_to_do == "^":
        return factor_1**factor_2
    elif operation_to_do == "*":
        return factor_1*factor_2
    elif operation_to_do == "/":
        return factor_1/factor_2
    elif operation_to_do == "+":
        return factor_1+factor_2
    else:
        return factor_1-factor_2

def dealing_with_priorities(operation):
    priority_one = ["^"]
    priority_two = ["*","/"]
    priority_three = ["+","-"]
    index = -1
    while index != len(operation)-1:
        index+=1
        char = operation[index]
        if char in priority_one:
            operation = function_for_indices(index,operation)
            index-=1

    index = -1
    while index != len(operation)-1:
        index+=1
        char = operation[index]
        if char in priority_two:
            operation = function_for_indices(index,operation)
            index-=1


    index = -1
    while index != len(operation)-1:
        index+=1
        char = operation[index]
        if char in priority_three:
            operation = function_for_indices(index,operation)
            index-=1



    return operation