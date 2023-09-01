class EMP:
    def __init__(self,name,id,sal,dept):
        self.name=name
        self.id=id
        self.sal=sal
        self.dept=dept
    def __str__(self):
        return "name:"+self.name+"\nID:"+self.id+"\nSal:"+str(self.sal)
    def update_sal(self,dept,sal):
        if(dept==self.dept):
            self.sal=sal

E=[]
for i in range(3):
    name= input("Enter name : ")
    id = input("Enter ID : ")
    dept = input("Enter Dept : ")
    sal= int(input("Enter Salary : "))
    E.append(EMP(name,id,sal,dept))
dept=input("enter depart")
sal=int(input("enter new salary"))
for e in E:
    e.update_sal(dept,sal)
    print(e)