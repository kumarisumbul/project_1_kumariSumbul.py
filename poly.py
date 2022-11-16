'''class Sum:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def do_sum(self,num1,num2):
        print('The sum is ')
        print(num1 + num2)

    def do_sum1(self,num1,num2,num3):
        print('the sub is ')
        print(num1 + num2 +num3)


s = Sum(1, 2)
s.do_sum(3, 4)
s.do_sum1(3,4,5)'''

from multipledispatch import dispatch


@dispatch(int,int,int)
def do_sum(num1,num2,num3):
    print('the sum is')
    print(num1+num2+num3)

@dispatch(int,int)
def do_sum(num1,num2):
    print('the sum is')
    print(num1+num2)

do_sum(2,3)