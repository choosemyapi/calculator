from __future__ import annotations
from typing import Any, List, Optional, Tuple, Union
import infix_to_postfix


class BinaryExprTree:
    _root: Optional[Any]
    _left: Optional[BinaryExprTree]
    _right: Optional[BinaryExprTree]

    def __init__(self, root: Optional[Any]) -> None:

        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinaryExprTree(None)
            self._right = BinaryExprTree(None)

    def is_empty(self) -> bool:

        return self._root is None

    def __str__(self) -> str:
        return self._str_indented()

    def _str_indented(self, depth: int = 0) -> str:

        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + str(self._root) + '\n'
            s += self._left._str_indented(depth + 1)
            s += self._right._str_indented(depth + 1)
            return s

    def evaluate(self):

        if not self.is_empty():
            if not infix_to_postfix.is_operator(self._root):
                return float(self._root)
            else:
                A = self._left.evaluate()
                B = self._right.evaluate()
                if self._root == "+":
                    return A + B
                elif self._root == "-":
                    return A - B
                elif self._root == "*":
                    return A * B
                elif self._root == "/":
                    return A / B


def build_tree(postfix: str):
    S = infix_to_postfix.Stack()

    for i in range(len(postfix)):
        if infix_to_postfix.is_operand(postfix[i]):
            if i + 1 <= len(postfix) - 1 and postfix[i + 1] != " ":
                continue
            else:
                j = i
                while j - 1 >= 0 and infix_to_postfix.is_operand(postfix[j - 1]):
                    j -= 1
                node = BinaryExprTree(postfix[j:i + 1])
                S.push(node)
        elif infix_to_postfix.is_operator(postfix[i]):
            tree = BinaryExprTree(postfix[i])
            right = S.pop()
            left = S.pop()

            tree._left = left
            tree._right = right

            S.push(tree)

        i += 1

    expr_tree = S.pop()
    return expr_tree


if __name__ == "__main__":
    print("Welcome to the Calculator. Enter 'N' to stop.")
    expr = input("Enter the expression you want to evaluate (floats only, + - * / supported): ")
    while expr.lower() != "n":
        postfix = infix_to_postfix.InfixToPostfix(expr)
        # print(postfix)
        binExprTree = build_tree(postfix)
        # print(binExprTree)
        print(binExprTree.evaluate())
        expr = input("Enter the expression you want to evaluate (floats only, + - * / supported): ")
    print("You've cancelled the operation. Restart to enter again.")