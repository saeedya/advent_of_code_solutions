import hashlib
  
# initializing string
str2hash = "yzbqklnj"
check = "000000"
  
# encoding GeeksforGeeks using encode()
# then sending to md5()

  
class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

a = iter(InfIter())

while True:
    n = next(a)
    s = str2hash + str(n)
    result = hashlib.md5(s.encode()).hexdigest()
    if not result[0:6] == check:
        str2hash = "yzbqklnj"
        continue
    else:
        print(n)
        break