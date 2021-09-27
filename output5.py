class Employee:
    name=''
    empId=0
    
    def __init__(self,name,empId):
        self.name=self.name+name
        self.empId=self.empId+empId
    def display(self):
        print(self.name)
        print(self.empId)
def main():
    a=Employee('A',1)
    b=Employee('B',2)
    a.display()
    b.display()
main()
