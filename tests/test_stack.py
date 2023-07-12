"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertFalse(stack.empty())

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.empty())
        self.assertIsNone(stack.pop())

