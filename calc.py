currentOperand=0
res=0
isOperation=False
currentOperator=''
operations = {'+','-','/','*','**'}

while curOperator !='=':
    currentOperand = float(input("Введите число:"))
    currentOperator = input("Введите операцию:")
    if currentOperator in operations:
        res = currentOperand
        currentOperand = float(input("Введите число:"))
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

    else:
        print("Введите операцию + - / * **")