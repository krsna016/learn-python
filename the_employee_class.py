""""""
class Employee():
    """"""

    def __init__(self,first_name,last_name,annual_salary) -> str:
        """"""
        self.f_name = first_name
        self.l_name = last_name
        self.a_salary = annual_salary

    def give_raise(self,increment = 500):
        """"""
        self.a_salary += increment
        return self.a_salary
