class Complex():
    def input(self,a,b):
        self.p=a
        self.q=b
    def add(self,s):
        C4 = Comples()
        print(self.p)
        print(self.q)
        print(s.p)
        print(s.q)
        C4.p=self.p+s.p
        C4.q=self.q+s.q
        return C4
    def show(self):
        print(self.p,"+",self.q,"i")


C1=Complex()
C1.input(2,4)
C1.show()

C2=Complex()
C2.input(4,6)
C2.show()

C3=Complex()
C3=C1.add(C2)
C3.show()
