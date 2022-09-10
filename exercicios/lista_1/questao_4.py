class Serie():
    
    class Fibonacci():
            
        def get(self, x):
            
            if (x == 0):
                return 0;
        
            if (x == 1):
                return 1;
            
            return self.get(x-1) + self.get(x-2);
            
        def upto(self, x):
            
            tr = list();
            for i in list(range(x)):
                tr.append(self.get(i));
            
            return tr;
            
    class Fatorial():
        
        def get(self, x):
            
            if (x == 1 or x == 0):
                return 1;
                
            return x*self.get(x-1);
        
        def upto(self, x):
            
            tr = list();
            for i in list(range(x)):
                tr.append(self.get(i));
                
            return tr;
        
    class Fibonarial():
        
        def get(self, x):
            
            p = Serie().Fibonacci().get(x);
            return Serie().Fatorial().get(p);
            
        def upto(self, x):
            
            tr = list();
            for i in list(range(x)):
                tr.append(self.get(i));
                
            return tr;
            
    class Primo():
        
        def check(self, num):
            
            if (num == 1 or num == 0):
                return False;
            
            isPrime = True;
            root = int(num**(1/2));
            for i in list(range(2, root+1)):
                if (num % i == 0):
                    isPrime = False;
                    
            return isPrime;
            
        def upto(self, x):
            
            i, j = 0, 0;
            tr = list();
            
            while j <= x:
                if (self.check(i)):
                    tr.append(i);
                    j += 1;
                i += 1;
            
            return tr;
        
        def get(self, x):
            
            l = self.upto(x);
            return l[len(l)-1];
            
        
        
s = Serie();
print(s.Fatorial().get(10));
print(s.Fatorial().upto(10));
print(s.Fibonacci().get(8));
print(s.Fibonacci().upto(10));
print(s.Fibonarial().upto(10));
print(s.Primo().get(10));
print(s.Primo().upto(10));