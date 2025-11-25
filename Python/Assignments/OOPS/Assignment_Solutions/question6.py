from abc import ABC, abstractmethod

class Employee(ABC):
    company_name = "Microsoft"

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        # 20% bonus
        return self.salary + self.salary * 20 / 100


class FullTime(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        # 30% bonus
        return self.salary + self.salary * 30 / 100


class ContractType(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        # 40% bonus
        return self.salary + self.salary * 40 / 100



intern = Intern("Arvind", 20_000)
print("Intern Salary:", intern.calculate_salary())

full = FullTime("Ritik", 50_000)
print("FullTime Salary:", full.calculate_salary())

contract = ContractType("Sagar", 30_000)
print("Contract Salary:", contract.calculate_salary())
