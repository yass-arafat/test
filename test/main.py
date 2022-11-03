def main():
   
   num1 = OddEvenNumbers(1,20)
   
   num1.displayEvenNumbers()
   num1.displayOddNumbers()
   OddEvenNumbers.test_class_method()
   

def oddeven():
    for i in range(1,20):
        if (i%2 == 0):
            print('%d is even number'%(i))
        else:
            print(i,' is odd number')

def oddevendig(n,m):
    even= []
    odd= []
    for i in range(n,m):
        if (i%2):
           even.append(i)
        else:
           odd.append(i)
    
    return {
        "odd": odd,
        "even": even
    }

class OddEvenNumbers:
    odds=[]
    evens=[]
    def __init__(self,m,n):
       for i in range(m,n):
        if(i%2):
             OddEvenNumbers.odds.append(i)
        else:
            OddEvenNumbers.evens.append(i)
       self.odd = OddEvenNumbers.odds
       self.even = OddEvenNumbers.evens
    def displayOddNumbers(self):
        print("Odd Numbers :" ,self.odd)

    def displayEvenNumbers(self):
        print("Even Numbers : " ,self.even)

    @classmethod
    def test_class_method(cls):
        
        print(cls.evens)


if __name__ == "__main__":
    main()



