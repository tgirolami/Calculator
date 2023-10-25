from dealing_with_priorities import dealing_with_priorities as dwp

def find_sub_operations(operation):
    index = -1
    while index != len(operation)-1:
        index+=1
        char  = operation[index]
        if char == "(":
            padding = 1
            last_index = None
            while operation[index+padding] != "(" and index+padding<len(operation)-1:
                padding+=1
                if operation[index+padding] == ")":
                    last_index = index+padding

                
            operation = operation[:index]+find_sub_operations(operation[index+1:last_index])+operation[last_index+1:]
            index-=1

    return dwp(operation)