class Math:
    n=0.0
    sap=0
    def table(self):
        print("Table")
        for i in range(1,11):
            a=i*self.n
            print(a)

    def factorial(self):
        if self.n == 0 or self.n == 1:
            print(1)
        else:
            c = 1
            for i in range(2, self.n + 1):
                c = c * i
            print("Factorial of the number: ",c)
    def square(self):
        print("Square: ",self.n**2)
    def cube(self):
        print("Cube: ",self.n**3)
    def tablesap(self):
        c=self.sap
        for i in range(1,11):
            a=i*self.n
            c+=1
            print(a,",","(",c,")")
math=Math()
math.n=4
math.sap=100
math.table()
math.factorial()
math.square()
math.cube()
math.tablesap()