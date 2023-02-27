import unittest
from the_employee_class import Employee

class TestEmployeeClass(unittest.TestCase):
    """"""
    def setUp(self) -> None:
        """"""
        self.u_1 = Employee("Anurag","Pareek",100)

    def test_default(self):
        """"""
        need = self.u_1.give_raise()
        self.assertEqual(need,600)

    def test_custom(self):
        """"""
        need = self.u_1.give_raise(500)
        self.assertEqual(need,600)

unittest.main()
