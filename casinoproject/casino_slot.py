import random
class slot:
    def __init__(self, bet):
        self.table = {
            "orange": 0,
            "grape":0,
            "seven":0,
            "wild":0,
            "cherry":0,
            "barr":0,
            "lemon":0
        }

        self.symbol_value = {
            "lemon": bet * 4,
            "orange" : bet * 4,
            "cherry" : bet* 8,
            "grape" : bet* 8,
            "barr" : bet*15,
            "seven" : bet*20,
            "wild" : bet*30
        }
        self.symbol_chance = {
            "lemon": 87,
            "orange" : 62,
            "cherry" : 44,
            "grape" : 30,
            "barr" : 18,
            "seven" : 8,
            "wild" : 0
        }
        self.grid = self.grid()
        self.line = self.lines()
        self.pay = self.payout()

    def grid(self):
        grid = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]
        total_chance = 0
        counter = 0
        reel_1 = []
        reel_2 = []
        reel_3 = []
        for x in range(0, 3):
            counter += 1
            for i in range(0, 1000):
                odds = random.randint(1,115)
                for n in self.symbol_chance.keys():
                    if odds>self.symbol_chance.get(n):
                        if n == ["lemon", "orange", "cherry", "grape", "watermelon", "strawberry", "barr", "seven"]:
                            n = "wild"
                        if counter == 1:
                            reel_1.append(n)
                        elif counter == 2:
                            reel_2.append(n)
                        elif counter == 3:
                            reel_3.append(n)
                        break
        for i in grid:
            i[0] = random.choice(reel_1)
            i[1] = random.choice(reel_2)
            i[2] = random.choice(reel_3)
        return grid


    def lines(self):
        line = [[" ", " "],
                [" ", " "],
                [" ", " "],
                [" ", " "],
                [" ", " "]]
        count = -1
        for i in self.grid:
            print(i[0], i[1], i[2])
            count+=1
            if (i[0] == i[1] and i[0] == i[2]):
                line[count][0] = True
                line[count][1] = i[0]
            else:
                line[count][0] = False
        print()

        if self.grid[0][0] == self.grid[1][1] and self.grid[0][0] == self.grid[2][2]:
            line[3][0] = True
            line[3][1] = self.grid[0][0]
        else:
            line[3][0] = False

        if self.grid[2][0] == self.grid[1][1] and self.grid[2][0] == self.grid[0][2]:
            line[4][0] = True
            line[4][1] = self.grid[2][0]
        else:
            line[4][0] = False
        return line
    def payout(self):
        pay = 0
        for i in self.line:
            if i[0]:
                self.table[i[1]] += 1
                pay +=self.symbol_value.get(i[1])
        return pay
        return self.table
        
tracker = {
            "orange": 0,
            "grape":0,
            "seven":0,
            "wild":0,
            "cherry":0,
            "barr":0,
            "lemon":0
        }
overall = []
for i in range(0, 10):
    total = 0
    for i in range(0, 10000):
        total -= 11
        test = slot(1)
        total += test.pay
        for i in test.table.keys():
            tracker[i] += test.table[i]
    overall.append(total)
total = 0
for i in overall:
    total+=i
average = total / 100
print("rtp:", average,"%")
print(overall)

    
print(total)
print(tracker)
    


# for i in range(0, 1000):
#     test = slot(10)
#     for i in test.grid:
#         print(i)
#     print(test.line)
#     print(test.pay)