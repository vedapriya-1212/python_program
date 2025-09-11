class emp:
    name="teju"
    salary=89000
    def display(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\n")
class manager(emp):
    dept="technical"
    def display(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.dept}\n")
obj=manager()
obj.display()
