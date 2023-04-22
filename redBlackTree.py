
from queue import Queue


class RedBlackTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.color = red
            self.left_child = None
            self.right_child = None

        def __str__(self):
            return f"Node{{value={self.value}, color={self.color}, left_child={self.left_child}, right_child={self.right_child}}}"

    class Color:
        RED = 0
        BLACK = 1

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root:
            result = self.__add_node(self.root, value)
            self.root = self.__rebalance(self.root)
            self.root.color = Color.BLACK
            return result
        else:
            self.root = self.Node(value)
            return True

    def __rebalance(self, node):
        result = node
        need_rebalance = True
        while need_rebalance:
            need_rebalance = False
            if result.right_child and result.right_child.color == Color.RED and (not result.left_child or result.left_child.color == Color.BLACK):
                need_rebalance = True
                result = self.__right_swap(result)
            if result.left_child and result.left_child.color == Color.RED and result.left_child.left_child and result.left_child.left_child.color == Color.RED:
                need_rebalance = True
                result = self.__left_swap(result)
            if result.left_child and result.left_child.color == Color.RED and result.right_child and result.right_child.color == Color.RED:
                need_rebalance = True
                self.__color_swap(result)
        return result

    def __add_node(self, node, value):
        if node.value == value:
            return False
        elif node.value > value:
            if node.left_child:
                result = self.__add_node(node.left_child, value)
                node.left_child = self.__rebalance(node.left_child)
                return result
            else:
                node.left_child = self.Node(value)
                return True
        else:
            if node.right_child:
                result = self.__add_node(node.right_child, value)
                node.right_child = self.__rebalance(node.right_child)
                return result
            else:
                node.right_child = self.Node(value)
                return True

    def __left_swap(self, node):
        left_child = node.left_child
        between_child = left_child.right_child
        left_child.right_child = node
        node.left_child = between_child
        left_child.color, node.color = node.color, Color.RED
        return left_child

    def __right_swap(self, node):
        right_child = node.right_child
        between_child = right_child.left_child
        right_child.left_child = node
        node.right_child = between_child
        right_child.color, node.color = node.color, Color.RED
        return right_child

    def __color_swap(self, node):
        node.left_child.color = node.right_child.color = Color.BLACK
        node.color = Color.RED

    def __print_in_order(self, node):
        if node:
            self.__print_in_order(node.left_child)
            print(node.value, end=" ")
            self.__print_in_order(node.right_child)

    def print_in_order(self):
        self.__print_in_order(self.root)

    

    root = Node(10)
