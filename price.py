class price1:
    def __init__(self,rs,ps):
        self.rs=rs
        self.ps=ps

    def __add__(self, other):
        temp_rs=0
        ps1=self.ps+other.ps
        if ps1>=100:
            temp_rs=ps1//100
            temp_ps=ps1%100
            ps1=temp_ps
        rs1=self.rs+other.rs+temp_rs
        p3=price1(rs1,ps1)
        return p3

    def print(self):
        print("Rs={}    Ps={}".format(self.rs,self.ps))

p1=price1(10,50)
p2=price1(40,30)
p3=p1+p2
p3.print()
