from _ast import ExceptHandler

currentOperand=0
res=0
currentOperator=''
operations = {'+','-','/','*','**'}
try:
    res = float(input("Введите число:"))
except Exception:
    print('Введите числовое значение')
while currentOperator !='=':
    operWithNum= input("Введите операцию:").split()
    currentOperator=operWithNum[0]
    #print("curOperator", currentOperator)

    if currentOperator in operations and currentOperator != '=':
        #currentOperand = res
        try:
            currentOperand = float(operWithNum[1])#float(input("Введите число:"))
            #print("curOperand", currentOperand)
        except Exception:
            print('Введите числовое значение')
        if currentOperator == '+':
            res = res+currentOperand
            #print(res)
        elif currentOperator == '-':
            res = res - currentOperand
            #print(res)
        elif currentOperator == '*':
            res = res * currentOperand
            #print(res)
        elif currentOperator == '**':
            res = res ** currentOperand
            #print(res)
        elif currentOperator == '/':
            if currentOperand == 0:
                print('На 0 делить нельзя')
            else:
                res = res / currentOperand
                #print(res)
    elif currentOperator == '=':
        break
    else:
        print("Введите операцию + - / * **")
print(res)
