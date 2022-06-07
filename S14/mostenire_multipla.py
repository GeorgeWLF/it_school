class A:

    def __init__(self) -> None:
        self.x = 10


class B(A):

    def __init__(self) -> None:
        self.y = 20


class C(A):
    
    def __init__(self) -> None:
        super(A, self).__init__()
        super(B, self).__init__()

class D(C, B):
    def __init__(self):
        
c = C()

print(dir(c))