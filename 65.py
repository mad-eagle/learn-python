class Math:
    def __init__(self , n):
        self.number = n
    
    @staticmethod
    def add(*num):
        value = 0
        for n in num:
            value = value + n

        return value

obj = Math(10)

print(obj.add(1,2,3,4))
print(Math.add(1,2,3,4,5))