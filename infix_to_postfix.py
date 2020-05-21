from typing import List, Any


class Stack:

    _items: List

    def __init__(self) -> None:
        self._items = []

    def is_empty(self) -> bool:
        return self._items == []

    def top(self):
        return self._items[-1]

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        return self._items.pop()


def InfixToPostfix(exp: str):
    exp = exp.replace(" ", "")

    S = Stack()
    postfix = ""
    j = 0
    for i in range(len(exp)):
        if is_operand(exp[i]):
            if i + 1 <= len(exp) - 1 and is_operand(exp[i+1]):
                continue
            else:
                j = i
                while j - 1 >= 0 and is_operand(exp[j - 1]):
                    if is_operand(exp[j]):
                        j -= 1
                    else:
                        break
            postfix += exp[j:i + 1] + " "
        elif is_operator(exp[i]):
            while not S.is_empty() and S.top() != "(" and HasHigherPrecedence(S.top(), exp[i]):
                if is_operator(S.top()):
                    postfix += S.top() + " "
                else:
                    postfix += S.top()
                S.pop()
            S.push(exp[i])
        elif exp[i] == "(":
            S.push(exp[i])
        elif exp[i] == ")":
            while not S.is_empty() and S.top() != "(":
                if is_operator(S.top()):
                    postfix += S.top() + " "
                else:
                    postfix += S.top()
                S.pop()
        else:
            print("There's an invalid character")
            return

    while not S.is_empty():
        if S.top() == '(':
            S.pop()
            continue
        if is_operator(S.top()):
            postfix += S.top() + " "
        else:
            postfix += S.top()
        S.pop()

    return postfix


def HasHigherPrecedence(op1: str, op2: str):
    op1_weight = get_operator_weight(op1)
    op2_weight = get_operator_weight(op2)
    return op1_weight > op2_weight

def get_operator_weight(op: str) -> int:
    weight = -1
    if op == '+' or op == '-':
        weight = 1
    elif op == '*' or op == '/':
        weight = 2
    return weight

def is_operator(exp: str):
    return exp == '+' or exp == '-' or exp == '/' or exp == '*'

def is_operand(exp: str):
    return exp.isdigit()




