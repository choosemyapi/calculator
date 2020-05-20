from typing import List, Any


class Stack:
    """A last-in-first-out (LIFO) stack of items.
    Stores data in first-in, last-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.
    """
    # === Private Attributes ===
    # _items:
    # The items stored in the stack. The end of the list represents
    # the top of the stack.
    _items: List

    def __init__(self) -> None:
        """Initialize a new empty stack.
        """
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push('hello')
        >>> s.is_empty()
        False
        """
        return self._items == []

    def top(self):
        return self._items[-1]

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.
        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        return self._items.pop()


def InfixToPostfix(exp: str):
    exp = exp.replace(" ", "")

    S = Stack()
    postfix = ""
    for i in range(len(exp)):
        if is_operand(exp[i]):
            postfix += exp[i]
        elif is_operator(exp[i]):
            while not S.is_empty() and S.top() != "(" and HasHigherPrecedence(S.top(), exp[i]):
                postfix += S.top()
                S.pop()
            S.push(exp[i])
        elif exp[i] == "(":
            S.push(exp[i])
        elif exp[i] == ")":
            while not S.is_empty() and S.top() != "(":
                postfix += S.top()
                S.pop()
        else:
            print("There's an invalid character")
            return
    while not S.is_empty():
        if S.top() == '(':
            S.pop()
            continue
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
    return exp.isalnum()




