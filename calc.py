from _ast import ExceptHandler

currentOperand=0
res=0
isOperation=False
currentOperator=''
operations = {'+','-','/','*','**'}
try:
    currentOperand = float(input("Введите число:"))
except Exception:
    print('Введите числовое значение')
while currentOperator !='=':
    currentOperator = input("Введите операцию:")
    if currentOperator in operations and currentOperator != '=':
        res = currentOperand
        try:
            currentOperand = float(input("Введите число:"))
        except Exception:
            print('Введите числовое значение')
        if currentOperator == '+':
            res=res+currentOperand
        elif currentOperator == '-':
            res = res - currentOperand
        elif currentOperator == '*':
            res = res * currentOperand
        elif currentOperator == '**':
            res = res ** currentOperand
        elif currentOperator == '/':
            if currentOperand == 0:
                print('На 0 делить нельзя')
            else:
                res = res / currentOperand
    elif currentOperator == '=':
        break
    else:
        print("Введите операцию + - / * **")
print(res)
