import unittest

from playground.Stack import myStack


class MyTestCase(unittest.TestCase):

    def test_stack_can_add_element(self):
        stack = myStack()
        stack.add_to_stack("semicolon.africa")
        stack.add_to_stack("google.com")

        self.assertEqual(len(stack.myStack), 2)

        def test_stack_removes_last_in_element(self):
            sl = myStack()
            sl.add_to_stack("semicolon.africa")
            sl.add_to_stack("google.com")
            sl.add_to_stack("reuters.ng")
            sl.add_to_stack("x.com")
            self.assertEqual(sl.stack[-1],"reuters.ng")





if __name__ == '__main__':
    unittest.main()
