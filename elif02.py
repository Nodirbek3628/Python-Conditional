templete = "{operand01}{operator}{operand02} = {result}"

operand01 = float(input("1-sonnni kiriting: "))
operand02 = float(input("2-sonni kiriting: "))
operator = input("Ishorani kiriting:: ")

if operator == "+":
    result = operand01 + operand02 
    print(templete.format(operand01 = operand01,
                          operand02 = operand02,
                          operator = operator,
                          result = result
                          ))
if operator == "-":
    result = operand01 - operand02 
    print(templete.format(operand01 = operand01,
                          operand02 = operand02,
                          operator = operator,
                          result = result
                          ))
if operator == "*":
    result = operand01 * operand02 
    print(templete.format(operand01 = operand01,
                          operand02 = operand02,
                          operator = operator,
                          result = result
                          ))
if operator == "/":
    if operand02 != 0:
        result = operand01 / operand02 
        print(templete.format(operand01 = operand01,
                          operand02 = operand02,
                          operator = operator,
                          result = result
                          ))

