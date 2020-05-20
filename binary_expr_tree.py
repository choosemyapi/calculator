from __future__ import annotations
from typing import Any, List, Optional, Tuple, Union
import infix_to_postfix


class BinaryExprTree:
    # === Private Attributes ===
    # The item stored at the root of the tree, or None if the tree is empty.
    _root: Optional[Any]
    # The left subtree, or None if the tree is empty.
    _left: Optional[BinaryExprTree]
    # The right subtree, or None if the tree is empty.
    _right: Optional[BinaryExprTree]

    def __init__(self, root: Optional[Any]) -> None:

        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinaryExprTree(None)  # self._left is an empty BST
            self._right = BinaryExprTree(None)  # self._right is an empty BST

    def is_empty(self) -> bool:

        return self._root is None

    def __str__(self) -> str:
        return self._str_indented()

    def _str_indented(self, depth: int = 0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + str(self._root) + '\n'
            s += self._left._str_indented(depth + 1)
            s += self._right._str_indented(depth + 1)
            return s

    def calculate(self):

        if not self.is_empty():
            if self._root.isdigit():
                return float(self._root)
            else:
                A = self._left.calculate()
                B = self._right.calculate()
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
            j = i
            while j + 1 <= len(postfix) - 1:
                if infix_to_postfix.is_operand(postfix[j]):
                    j += 1
                else:
                    break
            node = BinaryExprTree(postfix[i:j + 1])
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
    postfix = infix_to_postfix.InfixToPostfix("10*5+3")
    tree = build_tree(postfix)
    print(tree.calculate())
