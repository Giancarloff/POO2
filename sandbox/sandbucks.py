
class Foo:
    
    def __init__(self, a, b, c = 0) -> None:
        self.a = a
        self.b = b
        self.c = c
        
def main():
    
    foo = Foo(a=3, b=2)
    print(foo.c)

main()
   
   
   
    