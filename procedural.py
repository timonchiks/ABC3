# ----------------------------------------------
import random
import string


class Procedural:
    def __init__(self):
        self.popularity = 0.0
        self.year = 0
        self.abstract = False
        self.name = ""

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум четыре непрочитанных значения в массиве
        if i > len(strArray) - 4:
            return 0
        self.popularity = float(strArray[i + 2])
        self.year = int(strArray[i + 1])
        self.abstract = bool(strArray[i + 3])
        self.name = strArray[i]
        i += 4
        return i

    def Random(self):
        self.year = random.randint(1900, 2022)
        self.abstract = bool(random.randint(0, 1))
        self.popularity = random.randint(0, 10000) / 100.0
        self.name = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 50)))

    def Print(self):
        print("Procedural:", self.name, " popularity = ", self.popularity, " year = ", self.year, "abstract_type = ", self.abstract,
              ", Function = ", self.Function())
        pass

    def Write(self, ostream):
        ostream.write("Procedural:{} popularity = {}  year = {}  abstract_type = {}, Perimeter = {}".format \
                          (self.name, self.popularity, self.year, self.abstract, self.Function()))
        pass

    def Function(self):
        return float(self.year / len(self.name))
        pass
