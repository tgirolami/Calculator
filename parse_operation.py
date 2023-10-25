def transform_number(operation:"list[str]",output:list,negative=False):
    to_transform = []
    if negative:
        to_transform.append("-")
    padding = 0
    while padding<=len(operation)-1 and (operation[padding].isnumeric() or operation[padding]=="."):
        to_transform.append(operation[padding])
        padding+=1

    output.append(float("".join(to_transform)))
    return (padding-1 if negative == False else padding)
    

def parse_operation(operation:"list[str]"):
    operation_signs = ["+","-","/","*","^","(",")"]
    output = []
    skip = 0
    for index,char in enumerate(operation):
        if skip > 0:
            skip-=1
            continue
        if char == "-" and (operation[index-1] in operation_signs or index==0):
            skip = transform_number(operation[index+1:],output,negative=True)
        elif char.isnumeric():
            skip = transform_number(operation[index:],output)
        else:
            output.append(char)
    return output