class supervisor(company):
    def __init__(self,Name,email,telephone,Age,pay,employis = None):
        super().__init__(Name,email,telephone,Age,pay)
        if employis == None:
            self.employis = []
        else:
            self.employis = employis

    def add_employees(self,emp):
         if emp not in self.employis:
             self.employis.append(emp)

    def remove_employees(self,emp):
         if emp in self.employis:
             self.employis.remove(emp)

    def print_employees(self):
         for x in self.employis:
             print(x.Name)

emplo_1 = company('Shedy Musa Katama','sheddy@gmail.com','+254713363819','27 years',60000)
emplo_2 = company('Halima Said Kizingitini','halima@gmail.com','+254720820798','22 years',40000)

supervisor_1 = supervisor('Said Umuru Jillo','umurjillo@gmail.com','+254740169448','25 years',50000,[emplo_1])
supervisor_1.remove_employees(emplo_2)
print(supervisor_1.print_employees())
