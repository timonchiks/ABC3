#----------------------------------------------
import random
from enum import Enum
import string

class typization(Enum):
    nothing = 0
    strict = 1
    dynamic = 2


class Functional:
    def __init__(self):
        self.popularity = 0.0
        self.year = 0
        self.typization = typization(0).name
        self.lazy = False
        self.name = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум четыре непрочитанных значения в массиве
        if i > len(strArray) - 5:
            return 0
        self.popularity = float(strArray[i + 2])
        self.year = int(strArray[i + 1])
        self.typization = typization(int(strArray[i + 4])).name
        self.lazy = bool(strArray[i + 3])
        self.name = strArray[i]
        print(strArray[i])
        i += 5
        return i

    def Random(self):
        self.year = random.randint(1900, 2022)
        self.lazy = bool(random.randint(0,1))
        self.popularity = random.randint(0,10000)/100.0
        self.name = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1,50)))
        self.typization = typization(random.randint(0,2)).name

    def Print(self):
        print("Objective:", self.name, " popularity = ", self.popularity, " year = ", self.year, " typization = ",  self.typization, " lazy count = ",  self.lazy, " Function = ", self.Function())
        pass

    def Write(self, ostream):
        ostream.write("Objective:{} popularity = {}  year = {}, typization = {}, lazy count = {}, Function = {}".format(self.name, self.popularity, self.year, self.typization, self.lazy, self.Function()))
        pass

    def Function(self):
        return float(self.year / len(self.name))
        pass
