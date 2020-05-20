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
        """Return whether this BST is empty.
        """

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



def build_tree(postfix: str):

    S = infix_to_postfix.Stack()

    for expr in postfix:
       if infix_to_postfix.is_operand(expr):
           node = BinaryExprTree(expr)
           S.push(node)
       else:
           tree = BinaryExprTree(expr)
           right = S.pop()
           left = S.pop()

           tree._left = left
           tree._right = right

           S.push(tree)

    expr_tree = S.pop()
    return expr_tree