#create register, view credits, view last 5 games 
import random
import sqlite3
import itertools
import time
import hmac
import hashlib
import secrets
import subprocess
import webbrowser
from casinoproject.convertfunc import convertselect
from casinoproject.usermanagement import checklogin

connect = sqlite3.connect('casino.db')

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                 username text NOT NULL UNIQUE,
                 password text NOT NULL,
                 credits integer NOT NULL,
                 gameswon integer,
                 gameslost lost integer,
                 salt text NOT NULL,
                 PRIMARY KEY (username)
                 )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS GameType (
                 GameID integer NOT NULL UNIQUE ,
                 GameName text NOT NULL,
                 PRIMARY KEY (GameID)
                 )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Game_History (
                 RecordID integer NOT NULL UNIQUE,
                 username text NOT NULL,
                 GameID integer NOT NULL,
                 P1_Outcome integer NOT NULL,
                 P2_Outcome integer NOT NULL,
                 P3_Outcome integer,
                 P4_Outcome integer,
                 P5_Outcome integer,
                 playernumber text NOT NULL,
                 PRIMARY KEY (RecordID),
                 CONSTRAINT fk_users
                     FOREIGN KEY (username)
                     REFERENCES users(username)
                     ON DELETE CASCADE, 
                 CONSTRAINT fk_GameType
                     FOREIGN KEY (GameID)
                     REFERENCES GameType(GameID)
                 );""")

cursor.execute("""PRAGMA FOREIGNKEYS = ON;""")
connect.commit()
connect.close()



class Card:
    def __init__(self, suit, rank):
        #constrcutor
        self.suit = suit
        self.rank = rank
        self.convertcards()
    def convertcards(self):
        #used to get the int value of the cards
        try:
            self.value = int(self.rank)
        except:
            if self.rank == "Jack":
               self.value = 11
            if self.rank == "Queen":
               self.value = 12
            if self.rank == "King":
               self.value = 13
            if self.rank == "Ace":
               self.value = 1


    def __str__(self):
        #formatting method
        return f"{self.rank} of {self.suit}"

class Deck:
    #makes deck of cards
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.cards)


class slot(self)
    def __init__(self, line, grid, reel, payout):
        self.line = []
        self.grid = grid
        self.reel_one = []
        self.reel_two = []
        self.reel_three = []
        self.payout = payout
    def grid(self):
        self.grid = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]
    def lines(self):
        if self.grid[0,0].symbol == self.grid[0,1].symbol and self.grid[0,0].symbol == self.grid[0,2].symbol:
            self.line.append(True)
        else:
            self.line.append(False)
        if self.grid[1,0].symbol == self.grid[1,1].symbol and self.grid[1,0].symbol == self.grid[1,2].symbol:
            self.line.append(True)
        else:
            self.line.append(False)
        if self.grid[2,0].symbol == self.grid[2,1].symbol and self.grid[2,0].symbol == self.grid[2,2].symbol:
            self.line.append(True)
        else:
            self.line.append(False)
        if self.grid[0,0].symbol == self.grid[1,1].symbol and self.grid[0,0].symbol == self.grid[2,2].symbol:
            self.line.append(True)
        else:
            self.line.append(False)
        if self.grid[2,0].symbol == self.grid[1,1].symbol and self.grid[2,0].symbol == self.grid[0,2].symbol:
            self.line.append(True)
        else:
            self.line.append(False)
    def make_reel(self):
        for i in range(0, 1000):
            self.reel_one.append(self.symbols(random.randint(0, 8)))
            self.reel_two.append(self.symbols(random.randint(0, 8)))
            self.reel_three.append(self.symbols(random.randint(0, 8)))
        
        


class symbol(slot):
    def __init__(self)
        slot(__init__(self, line, grid, reel, payout))
        self.symbol_chance = chance
        self.symbol_name = name
        self.symbol_value = value
        self.symbol_look = look
        self.symbols = ["strawberry, watermelon, orange, grape, seven, wild, cherry, barr, lemon"]
    def assign_chance(self):
        self.lemon_chance = 20
        self.orange_chance = 20
        self.cherry_chance = 16
        self.grape_chance = 16
        self.watermelon_chance = 13
        self.strawberry_chance = 10
        self.barr_chance = 8
        self.seven_chance = 6
        self.wild_chance = 3
    def assign_value(self, bet):
        self.lemon_value = bet
        self.orange_value = bet
        self.cherry_value = bet * 2
        self.grape_value = bet * 2
        self.watermelon_value = bet * 5
        self.strawberry_value = bet * 7
        self.barr_value = bet * 10
        self.seven_value = bet * 15
        self.wild_value = bet * 30
        

def x_of_a_kind(hand, cards):
    same = 1
    current = []
    for i in hand:
        for j in current:
            if i[0] == j[0]:
                same += 1
                current.remove(j)
        current.append()
    if same == cards:
        return True

def sot():
  #returns if player wants to stick or twist
  sotloop = 0
  while sotloop == 0:
    stotw = input("stick or twist?")
    if stotw == "stick":
        return False
    elif stotw == "twist":
        return True
    else:
        print("please enter stick or twist")
      

def convertedcards(type, hand):
    #used to convert string cards into their integer values
    playertotal = 0
    dealertotal = 0
    loop = True
    #make dictionary for dealer probability
    #W3 schools
    if type == "player":
        for i in hand:
                if i.value > 10 and i.value < 14:
                    playertotal += 10
                elif i.value == 1:
                    while loop == True:
                        verify = int(input("would you like your ace to be an 1 or a 11"))
                        print(verify)
                        if verify != 1 and verify != 11:
                            print("enter 1 or 11")
                        else:
                            playertotal += verify
                            loop = False

                else:
                     playertotal += i.value

    elif type == "dealer":
        aces = []
        for i in hand:
            if i.value > 10 and i.value < 14:
                dealertotal += 10
            elif i.value == 1:
                aces.append(i)
                if dealertotal + 11 < 21:
                    dealertotal += 11

                else:
                    dealertotal += 1
            else:
                dealertotal += i.value
            #can change ace from an 11 to a 1
            if (dealertotal > 21 or dealertotal == 16 or dealertotal == 17) and len(aces) > 0:
               dealertotal -= 10
               aces.remove(aces[0])



    if playertotal > 0:
        return playertotal
    else:
        return dealertotal


def prettyprint(array):
  #formatting function for lists
  output = '|'
  for i in array:
    output += f' {i[0]} {i[1]} |'
  return output

def printcards(hand):
    #used to print cards from the class in the correct format
    for i in hand:
        print(i)


def sortcards(deck, rank):
    for card in deck:
        if rank in card.rank:
            return rank
        
def findprobability(dictionary, deck):
    probability = 0
    for i in deck:
        if i.value < 6:
            probability += dictionary.get(i.rank)
    probability = probability / 4
    return probability

        



def blackjack():
    #main blackjack code
    looping = True
    connect = sqlite3.connect('casino.db')
    cursor = connect.cursor()
    total = 0
    dealertotal = 0
    deck = Deck()
    print('welcome to blackjack')
    cursor.execute(f"""SELECT credits FROM users WHERE username = '{username}'""")
    winnercredits = cursor.fetchone()
    connect.commit()
    winnercredits = convertselect(winnercredits, "int")
    while looping:
        try:
            print("current available credits:", winnercredits)
            credits_used = int(input("what do you bet?"))
            if credits_used < 1 or credits_used == '':
                print("enter a int greater than 0")
            elif credits_used > winnercredits:
                print("enter an integer less than your current balance")
            else:
                looping = False
        except:
            print("Enter an int greater than 0")
    overall =  credits_used + winnercredits
    print("dealer matched")
    probabilitydict = {
        sortcards(deck.cards, "Ace"): 4,
        sortcards(deck.cards, "2"): 4,
        sortcards(deck.cards, "3"): 4,
        sortcards(deck.cards, "4"): 4,
        sortcards(deck.cards, "5"): 4,
        sortcards(deck.cards, "6"): 4,
        sortcards(deck.cards, "7"): 4,
        sortcards(deck.cards, "8"): 4,
        sortcards(deck.cards, "9"): 4,
        sortcards(deck.cards, "10"): 4,
        sortcards(deck.cards, "Jack"): 4,
        sortcards(deck.cards, "Queen"): 4,
        sortcards(deck.cards, "King"): 4

    }
    playercards = []
    dealercards = []
    #deal first 2 cards
    for i in range(0, 2):
        playercards.append(deck.cards[i])
        deck.cards.remove(deck.cards[i])
        probabilitydict.update({playercards[i].rank: probabilitydict.get(playercards[i].rank) - 1})

    for i in range(0, 2):
        dealercards.append(deck.cards[i])
        deck.cards.remove(deck.cards[i])
        probabilitydict.update({dealercards[i].rank: probabilitydict.get(dealercards[i].rank) - 1})

    print("dealers face up card is:", dealercards[0])

    print("your cards are:")
    printcards(playercards)
    total = convertedcards("player", playercards)
    dealertotal = convertedcards("dealer", dealercards)
    print("bringing your total to:", total)

    while True:
        if sot() == False:
            probability = findprobability(probabilitydict, deck.cards)
            while dealertotal<17 or dealertotal < 18 and probability > 17:
                probability = findprobability(probabilitydict, deck.cards)
                dealercards.append(deck.cards[0])
                deck.cards.remove(deck.cards[0])
                probabilitydict.update({dealercards[-1].rank: probabilitydict.get(dealercards[-1].rank) - 1})
                dealertotal = convertedcards("dealer", dealercards)
                print(dealertotal)
            if dealertotal > 21:
                print("dealer goes bust with a hand of")
                printcards(dealercards)
                time.sleep(2)
                print("you won", credits_used)
                cursor.execute(f"""UPDATE users SET credits = '{overall}' WHERE username = '{username}'""")
                connect.commit()
                break
            else:
                if dealertotal >= total:
                    print("dealer wins with a hand of")
                    printcards(dealercards)
                    print("you lost", credits_used)
                    cursor.execute(f"""UPDATE users SET credits = '{winnercredits - credits_used}' WHERE username = '{username}'""")
                    connect.commit()
                    break
                else:
                    print("player wins, dealer had a hand of")
                    printcards(dealercards)
                    time.sleep(2)
                    print("you won", credits_used)
                    cursor.execute(f"""UPDATE users SET credits = '{overall}' WHERE username = '{username}'""")
                    connect.commit()
                    break
        else:
            playercards.append(deck.cards[0])
            print("you got dealt", deck.cards[0])
            deck.cards.remove(deck.cards[0])
            probabilitydict.update({playercards[-1].rank: probabilitydict.get(playercards[-1].rank) - 1})
            if playercards[-1].rank == "Ace":
                playercards[-1].value = int(input("would you like your ace to be an 1 or a 11"))
            print("you now have")
            printcards(playercards)
            total = convertedcards("player", playercards)
            if total > 21:
                print("you went bust, dealer had a hand of")
                printcards(dealercards)
                print("you lost", credits_used)
                cursor.execute(f"""UPDATE users SET credits = '{winnercredits - credits_used}' WHERE username = '{username}'""")
                connect.commit()
                break
    connect.commit()
    connect.close()
    #cursor.close()





#create a for loop that iterates through every combination of the 5 cards, each time win checking those 5 cards, then calculating the best score overall
def pokerbots(hand):
  return itertools.permutations(hand, 5)





def Of_A_Kind(hand):
        #used to identify multiple of the same rank in the players hand
        score = 0
        ofkind = 0
        ofkinder = 0
        number = 0
        detect = 0
        seen = set()
        for n in hand:
            if n.value in seen:
                number += 2
                if number == 2:
                    detect = 2
            else:
                seen.add(n.value)
        if number == 2 or detect == 2:
            if number == 2:
                ofkind += 1
            elif number == 4:
                ofkind += 2
            else:
                ofkind = 1
                ofkinder = 1
        elif number == 4 and detect != 2:
            ofkinder = 1
        elif number == 6:
            score = 56

        if ofkind > 0 and ofkinder > 0:
            score = 33
        elif ofkind == 1:
            score = 2
        elif ofkind == 2:
            score = 4
        elif ofkinder == 1:
            score = 7
        return score

def straight_or_flush(hand, stage):
        flush = False
        score = 0
        score2 = 0
        for i in range(0, len(hand)):
            straight = False
            try:
                if hand[i].value + 1 != hand[i+1].value:
                    if hand[i+1].value == 1:
                        if hand[i].value + 1 != 14:
                            if stage == "no":
                                score = i + 1
                                break

                    else:
                        break
                straight = True
            except:
                straight = True
                break


        for i in range(0, len(hand)):
            flush = False
            try:
                if hand[i].suit != hand[i+1].suit:
                    score2 = i + 1
                    break
                flush = True
            except:
                flush = True

        if straight and flush and hand[0].value == 10:
            score = 146
            score2 = 0
        elif straight and flush == True:
            score = 89
            score2 = 0
        elif flush:
            score = 0
            score2 = 20
        elif straight:
            score =  12
            score2 = 0
        if stage == "no":
            return score, score2
        else:
            return score


def pokercalc(hand):
    maxscore = 0
    bestcardsindex = 0
    possiblehands = pokerbots(hand)
    for i, e in enumerate(possiblehands):
        score = 0
        score = Of_A_Kind(e) + straight_or_flush(e, "yes")
        if max(score, maxscore) == score:
            maxscore = score
    possiblehands = list(possiblehands)
    return maxscore


def deal_cards(number_of_players):
  number_of_players = number_of_players + 1
  tempcards = []
  playercards = []
  deck = Deck()
  players = dict()
  for i in range(0, (number_of_players * 2) + 1):
      tempcards.append(deck.cards[i])
      deck.cards.remove(deck.cards[i])
  for i in range(1, number_of_players + 1):
    player_name = f"player_{i}"
    for n in range(0, 2):
        playercards.append(tempcards[n])
        tempcards.remove(tempcards[n])
    players.update({player_name: playercards})
    playercards = []
  return players, deck

def botwage(hand, stage, loop, folded, highestbet, communitycards):
    fullhand = list(hand) + list(communitycards)
    number = random.randint(0, 10)
    if stage == 1:
        score = two_card_dict(hand, loop, folded, highestbet, "no")
        return score
    elif stage == 2:
        score = post_two_card_calc(fullhand, highestbet)
        return score
    elif stage == 3:
        score = post_two_card_calc(fullhand, highestbet)
        return score
    elif stage == 4:
        score = pokercalc(fullhand)
        if score == 0:
            return "fold"
        elif score == 2:
            if random.randint(0, 2) != 0:
                return "fold"
            else:
                if highestbet == 0:
                    return 10
                else:
                    return "call"
        elif score > 2 and score < 8:
            if highestbet == 0:
                return 10
            else:
                return "call"
        elif score > 7 and score < 21:
            if highestbet == 0:
                return 40
            else:
                return highestbet * 2
        elif score > 20 and score < 57:
            if score > 33:
                #if number == 5:
                    #return "all"
                #else:
                if highestbet == 0:
                    return 60
                    return highestbet * 3
            else:
                if highestbet == 0:
                    return 80
                else:
                    return highestbet * 4
        else:
            #if number == 5:
                #return "all"
            #else:
                if highestbet == 0:
                    return 200
                else:
                    return highestbet * 5

def playerwager(wage, loop, highestbet, playernum):
    truth = True
    truth1 = True
    connect = sqlite3.connect('casino.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT credits FROM users WHERE username = '{username}'""")
    overdrawn = cursor.fetchone()
    connect.commit()
    overdrawn = convertselect(overdrawn, "int")
    while truth:
        if wage == 1:
            if loop != "yes":
                r_or_c = input("raise(highestbet * x) or call(highestbet)?:(r or c)")
            else:
                r_or_c = input("raise, call, fold or pass?:(r, c, f or p)")
            if r_or_c == "r":
                while truth == True:
                    try:
                        wager = int(input("raise to?"))
                        truth = False
                    except: 
                        print("enter a valid integer")
                truth = True
                if wager > overdrawn:
                    print("you don't have enough credits for that wager, your available credits are:", overdrawn)
                else:
                    while truth1:
                        if wager < 10:
                                print("enter a integer higher than ten")
                                try:
                                    wager = int(input("raise to:"))
                                except:
                                    print("enter a valid integer")

                        else:
                            if wager % highestbet == 0 and wager != highestbet:
                                return wager
                            else:
                                print("please enter a multiple of", highestbet)
                                try:
                                    wager = int(input("raise to:"))
                                except:
                                    print("enter a valid integer")
    
            elif r_or_c == "c":
                if highestbet > overdrawn:
                    print("you don't have enough credits for that wager, your available credits are:", overdrawn)
                else:
                    print("bet called")
                    return "call"
            elif r_or_c == "f" and loop == "yes":
                return "fold"
            elif r_or_c == "p" and loop == "yes":
                if highestbet == 0:
                    return "pass"
                else:
                    print("a bet has already been made, therefore you cannot pass")
                    time.sleep(1.5)
                    playerwager(1, loop, highestbet, playernum)
            else:
                print("pick a valid option")
        else:
            if highestbet == 0:
                choice = input("please make the first bet(min 10), fold or pass(r, f or p)")
            else:
                choice = input("raise, call, fold or pass?:(r, c, f, p)")
            if choice == "r":
                while truth == True:
                    try:
                        wager = int(input("raise to?"))
                        truth = False
                    except: 
                        print("enter a valid integer")
                truth = True
                if wager > overdrawn:
                    print("you don't have enough credits for that wager, your available credits are:", overdrawn)
                else:                   
                    while truth1 == True:
                        wager = int(input("raise to?"))
                        if highestbet == 0:
                            if wager < 10:
                                print("enter a integer higher than ten")
                            else:
                                return wager
                        elif wager % highestbet == 0 and wager != highestbet:
                            return wager
                        else:
                            print("please enter a multiple of", highestbet)
            elif choice == "c" and loop == "yes":
                if highestbet > overdrawn:
                    print("you don't have enough credits for that wager, your available credits are:", overdrawn)
                else:
                    print("bet called")
                    return "call"
            elif choice == "c" and loop == "no" and playernum != "player_1":
                 if highestbet > overdrawn:
                    print("you don't have enough credits for that wager, your available credits are:", overdrawn)
                 else:
                    print("bet called")
                    return "call"
            elif choice == "f":
                return "fold"
            elif choice == "p":
                print("a bet has already been made, therefore you cannot pass")
                time.sleep(1.5)
                playerwager(2, loop, highestbet, playernum)
            else:
                print("pick a valid option!!!")
    connect.commit()
    connect.close()
    cursor.close()

def two_card_dict(hand, loop, folded, highestbet, flop):
    #calculates whether bot should raise call or fold
    value = 0
    twocard = ""
    twocardreverse  = ""
    twocard = hand[0].rank + hand[1].rank
    twocardreverse = hand[1].rank + hand[0].rank
    if hand[0].suit == hand[1].suit:
        twocard = twocard + "S"
        twocardreverse = twocardreverse + "S"
    two_card_dict = {
        "27": 1,
        "28": 2,
        "38": 3,
        "29": 4,
        "39": 5,
        "49": 6,
        "26": 7,
        "102": 8,
        "37": 9,
        "103": 10,
        "23": 11,
        "104": 12,
        "105": 13,
        "48": 14,
        "Jack2": 15,
        "24": 16,
        "Jack3": 17,
        "Jack4": 18,
        "25": 19,
        "59": 20,
        "Jack5": 21,
        "36": 22,
        "Jack6": 23,
        "47": 24,
        "Queen2": 25,
        "Queen3": 26,
        "Queen4": 27,
        "34": 28,
        "Queen5": 29,
        "106": 30,
        "58": 31,
        "35": 32,
        "Queen6": 33,
        "46": 34,
        "69": 35,
        "King2": 36,
        "King3": 37,
        "King4": 38,
        "Queen7": 39,
        "57": 40,
        "Jack7": 41,
        "King5": 42,
        "45": 43,
        "68": 44,
        "King6": 45,
        "107": 46,
        "56": 47,
        "King7": 48,
        "67": 49,
        "27S": 50,
        "79": 51,
        "28S": 52,
        "Ace2": 53,
        "38": 54,
        "Queen8": 55,
        "78": 56,
        "Ace6": 57,
        "King8": 58,
        "29S": 59,
        "26S": 60,
        "Ace3": 61,
        "Jack8": 62,
        "39S": 63,
        "49S": 64,
        "23S": 65,
        "Ace4": 66,
        "37S": 67,
        "Ace7": 68,
        "Ace5": 69,
        "108": 70,
        "89": 71,
        "102S": 72,
        "24S": 73,
        "103S": 74,
        "104S": 75,
        "48S": 76,
        "105S": 77,
        "25S": 78,
        "Ace8": 79,
        "36S": 80,
        "Jack2S": 81,
        "59S": 82,
        "Jack3S": 83,
        "Jack4S": 84,
        "47S": 85,
        "34S": 86,
        "Queen9": 87,
        "Jack5S": 88,
        "King9": 89,
        "Jack9": 90,
        "Jack6S": 91,
        "58S": 92,
        "35S": 93,
        "Ace9": 94,
        "Queen2S": 95,
        "106S": 96,
        "109": 97,
        "Queen3S": 98,
        "Queen4S": 99,
        "46S": 100,
        "Queen5S": 101,
        "69S": 102,
        "57S": 103,
        "Queen6S": 104,
        "45S": 105,
        "Jack7S": 106,
        "56S": 107,
        "68S": 108,
        "Queen7S": 109,
        "King3S": 110,
        "King2S": 111,
        "King4S": 112,
        "107S": 113,
        "67S": 114,
        "King5S": 115,
        "79S": 116,
        "King6S": 117,
        "33": 118,
        "22": 119,
        "44": 120,
        "Queen10": 121,
        "78S": 122,
        "Jack10": 123,
        "55": 124,
        "King10": 125,
        "King7S": 126,
        "Queen8S": 127,
        "Ace10": 128,
        "Jack8S": 129,
        "89S": 130,
        "Ace2S": 131,
        "108S": 132,
        "King8S": 133,
        "66": 134,
        "QueenJack": 135,
        "Ace6S": 136,
        "Ace3S": 137,
        "Ace4S": 138,
        "KingJack": 139,
        "Ace7S": 140,
        "77": 141,
        "Ace5S": 142,
        "AceJack": 143,
        "Jack9S": 144,
        "Queen9S": 145,
        "Ace8S": 146,
        "109S": 147,
        "King9S": 148,
        "88": 149,
        "KingQueen": 150,
        "Ace9S": 151,
        "AceQueen": 152,
        "99": 153,
        "Jack10S": 154,
        "Queen10S": 155,
        "King10S": 156,
        "QueenJackS": 157,
        "Ace10S": 158,
        "AceKing": 159,
        "1010": 160,
        "KingJackS": 161,
        "AceJackS": 162,
        "KingQueenS": 163,
        "AceQueenS": 164,
        "JackJack": 165,
        "AceKingS": 166,
        "QueenQueen": 167,
        "KingKing": 168,
        "AceAce": 169
    }
    if twocard in two_card_dict or twocardreverse in two_card_dict:
        value = two_card_dict.get(twocard)
        if isinstance(value, int):
            pass
        else:
            value = two_card_dict.get(twocardreverse)
    if flop == "yes":
        return value
    #print(value)

    bluff = random.randint(1, 10)
    if loop != "yes":
        if bluff == 1 and value < 140:
            return highestbet * 2
        elif value <= 40 and folded != "done":
            return "fold"
        elif value <= 40 and folded == "done":
            return "call"
        elif value <= 140:
            return "call"
        elif value <= 169:
            if value > 141 and value < 150:
                return highestbet * 2
            elif value > 149 and value < 160:
                return highestbet * 3
            elif value > 159:
                return highestbet * 4
    else:
        if value < 45 and folded != "done":
            return "fold"
        elif value <= 140 or highestbet > 60:
            return "call"
        elif value <= 169:
            if value > 141 and value < 156:
                return highestbet * 2
            elif value > 155:
                return highestbet * 3


def pokercalc2(hand):
    maxscore = 0
    maxscore2 = 0
    maxscore3 = 0
    possiblehands = pokerbots(hand)
    for i, e in enumerate(possiblehands):
        score = 0
        score2 = 0
        score3 = 0
        score = Of_A_Kind(e)
        if max(score, maxscore) == score:
            maxscore = score
        score2, score3 = straight_or_flush(e, "no")
        if max(score2, maxscore2) == score2:
            maxscore2 = score2
        if max(score3, maxscore3) == score3:
            maxscore3 = score3
    return maxscore, maxscore2, maxscore3




def post_two_card_calc(hand, highestbet):
    #look into more fold options for the 3rd round of betting
    if highestbet > 0:
        betting = 1
    else:
        betting = 0
    placeholder = two_card_dict(hand, "no", "no", highestbet, "yes")
    ofakindscore, straightscore, flushscore = pokercalc2(hand)
    if straightscore == 12 or flushscore == 20:
        if betting == 1:
            return highestbet * 2
        else:
            return 20
    elif straightscore == 89:
        if betting == 1:
            return highestbet * 3
        else:
            return 30
    elif straightscore == 146:
        return highestbet * 4
    elif highestbet == 0 and placeholder >= 100 and (straightscore > 1 and straightscore < 4) and (flushscore > 1 and flushscore < 4):
        return "pass"
    elif ofakindscore == 0 and placeholder <= 125 and straightscore < 3 and flushscore < 3:
        return "fold"
    elif highestbet > 80:
        return "call"
    elif ofakindscore == 0 and placeholder <= 125 and (straightscore > 2 and straightscore < 5) or (flushscore > 2 and flushscore < 5):
        if highestbet < 81:
            if betting == 1:
                return "call"
            elif betting == 0:
                return 10
        else:
            return "fold"
    elif ofakindscore == 0 and placeholder > 125 and straightscore < 4 and flushscore < 4:
        if betting == 1:
            return "call"
        else:
            return 10
    elif ofakindscore == 0 and straightscore == 4 or flushscore == 4:
        if betting == 1:
            return highestbet * 2
        else:
            return 20
    elif ofakindscore == 2:
        if straightscore > 3 or flushscore > 3:
            if betting == 1:
                return highestbet * 2
            else:
                return 20
        else:
            if highestbet > 80:
                return "fold"
            else:
                if betting == 1:
                    return "call"
                else:
                    return 10
    elif (ofakindscore == 7 or ofakindscore == 4):
        if straightscore > 3 or flushscore > 3:
            if betting == 1:
                return highestbet * 3
            else:
                return 30
        else:
            if betting == 1:
                return highestbet * 2
            else:
                return 20
    elif ofakindscore == 4 or ofakindscore == 7:
        if betting == 1:
            return highestbet * 2
        else:
            return 20
    elif ofakindscore == 33:
        if straightscore > 3 or flushscore > 3:
            if betting == 1:
                return highestbet * 4
            else:
                return 40
        else:
            if betting == 1:
                return highestbet * 3
            else:
                return 30
    elif ofakindscore == 56:
        if betting == 1:
            return highestbet * 4
        else:
            return 40




def betting(creditstracker, numplayers, playernum, players, bet, loop, round, communitycards, creditdatabase):
    #main betting round function
    deadplayer = 0
    highestbet = bet
    fold = "not"
    for i in range(1, numplayers + 2):
            if len(players) == 1:
                return "folded"
            #player 1 and 2 already made bets
            if round == 1 and ("player_" + str(i) == "player_1" or "player_" + str(i) == "player_2"):
                pass
            elif "player_" + str(i) == playernum:
                if round == 1:
                    print("your cards are:")
                    for i in players.get(playernum):
                        print(i)
                        time.sleep(1)
                    player_choice = playerwager(1, "no", highestbet, playernum)
                else:
                    print("your cards available are:")
                    for i in players.get(playernum):
                        print(i)
                        time.sleep(1)
                    for i in communitycards:
                        print(i)
                        time.sleep(1)
                    player_choice = playerwager(round, "no", highestbet, playernum)

                if player_choice == "fold":
                    players.pop(playernum)
                    print("folded")
                    return "folded"
                if player_choice == "call":
                     creditstracker.update({playernum: highestbet})
                     print("you wagered", highestbet)
                     time.sleep(1.5)
                elif player_choice == "pass":
                    print(playernum, "passed!")
                elif isinstance(player_choice, int) == True and highestbet == 0:
                    creditstracker.update({playernum: player_choice})
                    print(playernum, "starts the betting at", player_choice)
                    highestbet = player_choice
                    time.sleep(1.5)
                else:
                    creditstracker.update({playernum: player_choice})
                    highestbet = player_choice
                    print(playernum, "raised to", highestbet)
                    raisedcreditstracker = creditstracker.copy()
                    raisedcreditstracker.pop(playernum)
                    time.sleep(1.5)
                    creditstracker, players, highestbet, deadplayer, creditdatabase = raisedbetting(raisedcreditstracker, playernum, players, highestbet, fold, creditstracker, communitycards, round, deadplayer, playernum, creditdatabase)
                    return creditstracker, players, highestbet, deadplayer, creditdatabase

            elif "player_" + str(i) in players:
                botplayer = "player_" + str(i)
                bot_choice = botwage(players.get(botplayer), round, "no", fold, highestbet, communitycards)
                if bot_choice == "fold":
                        players.pop(botplayer)
                        deadplayer += creditstracker.get(botplayer)
                        creditdatabase.append(botplayer)
                        #creditstracker.pop(botplayer)
                        print(botplayer, "folded!")
                        fold = "done"
                        time.sleep(1.5)
                elif bot_choice == "call":
                        creditstracker.update({botplayer: highestbet})
                        print(botplayer, "called, their wager is", highestbet)
                        time.sleep(1.5)
                elif bot_choice == "pass":
                    print(botplayer, "passed")
                elif isinstance(bot_choice, int) == True and highestbet == 0:
                    creditstracker.update({botplayer: bot_choice})
                    print(botplayer, "started the betting at:", bot_choice)
                    highestbet = bot_choice
                    time.sleep(1.5)
                elif bot_choice == "all":
                    pass
                else:
                    creditstracker.update({botplayer: bot_choice})
                    highestbet = bot_choice
                    print(botplayer, "raised to", highestbet)
                    raisedcreditstracker = creditstracker.copy()
                    raisedcreditstracker.pop(botplayer)
                    time.sleep(1.5)
                    try:
                        creditstracker, players, highestbet, deadplayer, creditdatabase = raisedbetting(raisedcreditstracker, playernum, players, highestbet, fold, creditstracker, communitycards, round, deadplayer, botplayer, creditdatabase)
                        return creditstracker, players, highestbet, deadplayer, creditdatabase
                    except:
                        return "folded"
    return creditstracker, players, highestbet, deadplayer, creditdatabase





def raisedbetting(raisedcreditstracker, playernum, players, highestbet, fold, creditstracker, communitycards, round, deadplayer, raisedplayer, creditdatabase):
    #function
    numplayers = len(raisedcreditstracker) + 3
    for i in range(1, numplayers):
            if len(players) == 1:
                return "folded"
            if "player_" + str(i) == playernum and playernum in players and playernum != raisedplayer:
                    if round == 1:
                        print("your cards are:")
                        for i in players.get(playernum): print(i)
                        player_choice = playerwager(1, "yes", highestbet, playernum)
                    else:
                        print("your cards available are:")
                        for i in players.get(playernum):
                            print(i)
                            time.sleep(1)
                        for i in communitycards:
                            print(i)
                            time.sleep(1)
                        player_choice = playerwager(round, "yes", highestbet, playernum)
                    if player_choice == "fold":
                        players.pop(playernum)

                        print("folded1")
                        return "folded"
                    if player_choice == "call":
                         raisedcreditstracker.update({playernum: highestbet})
                         creditstracker.update({playernum: highestbet})
                         time.sleep(1.5)
                    else:
                        creditstracker.update({playernum: player_choice})
                        raisedcreditstracker = creditstracker.copy()
                        raisedcreditstracker.pop(playernum)
                        highestbet = player_choice
                        print(playernum, "raised to", highestbet)
                        time.sleep(1.5)
                        try:
                            creditstracker, players, highestbet, deadplayer, creditdatabase = raisedbetting(raisedcreditstracker, playernum, players, highestbet, fold, creditstracker, communitycards, round, deadplayer, playernum, creditdatabase)
                            return creditstracker, players, highestbet, deadplayer, creditdatabase
                        except:
                            return "folded"
            botplayer = "player_" + str(i)
            if botplayer in players and botplayer != raisedplayer:
                bot_choice = botwage(players.get(botplayer), round, "yes", fold, highestbet, communitycards)
                if bot_choice == "fold":
                        players.pop(botplayer)
                        deadplayer += creditstracker.get(botplayer)
                        creditdatabase.append(botplayer)
                        print(botplayer, "folded!")
                        time.sleep(1.5)
                        fold = "done"
                        time.sleep(1.5)
                elif bot_choice == "call":
                        raisedcreditstracker.update({botplayer: highestbet})
                        creditstracker.update({botplayer: highestbet})
                        print(botplayer, "called!")
                        time.sleep(1.5)
                else:
                    creditstracker.update({botplayer: bot_choice})
                    highestbet = bot_choice
                    print(botplayer, "raised to", highestbet)
                    raisedcreditstracker = creditstracker.copy()
                    raisedcreditstracker.pop(botplayer)
                    time.sleep(1.5)
                    try:
                        raisedcreditstracker, players, highestbet, deadplayer, creditdatabase = raisedbetting(raisedcreditstracker, playernum, players, highestbet, fold, creditstracker, communitycards, round, deadplayer, botplayer, creditdatabase)
                        return creditstracker, players, highestbet, deadplayer, creditdatabase
                    except:
                        print("AD")
                        return "folded"

    return creditstracker, players, highestbet, deadplayer, creditdatabase











def poker():
    connect = sqlite3.connect('casino.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT credits FROM users WHERE username = '{username}'""")
    winnercredits = cursor.fetchone()
    connect.commit()
    winnercredits = convertselect(winnercredits, "int")
    playercards = []
    communitycards = []
    lastscore = []
    creditdatabase = []
    creditpool = 0
    loop = 0
    while loop == 0:
        try:
            numplayers = int(input("how many players would you like to play against?(1- 4)"))
            if numplayers < 1 or numplayers > 4:
                print("enter a valid integer(1 - 4)")
            else:
                loop = 1
        except:
            print("enter a valid integer(1 - 4)")
    players, deck = deal_cards(numplayers)
    playernum = "player_" + str(random.randint(1, numplayers + 1))
    playerlist = []
    print("you are:", playernum)
    #make sure folded players credits are still counted
    creditstracker = {
        "player_1": 0,
        "player_2": 0,
        "player_3": 0,
        "player_4": 0,
        "player_5": 0
    }
    print("player1 wagered 5")
    time.sleep(2)
    print("player2 wagered 10")
    time.sleep(2)
    creditstracker.update({"player_1": 5})
    creditstracker.update({"player_2": 10})
    for i in range(0, 2):
        playercards.append(deck.cards[i])
        deck.cards.remove(deck.cards[i])
    for i in range(0, 3):
        communitycards.append(deck.cards[i])
        deck.cards.remove(deck.cards[i])
    #no need for fold as game would instantly end

    try:
        creditstracker, players, highestbet, deadplayer, creditdatabase  = betting(creditstracker, numplayers, playernum, players, 10, "no", 1, "placeholder", creditdatabase)
    except:
         if len(players) != 1:
            print("good game, better luck next time!")
            print("you lost a total of", creditstracker[playernum])
            cursor.execute(f"""UPDATE users SET (credits, gameslost) = ('{winnercredits - creditstracker.get(playernum)}', gameslost + 1) WHERE username = '{username}'""")
            cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))
            connect.commit()
            return
         else:
             print("all other players folded, you win!")
             time.sleep(2)
             cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{winnercredits + creditpool}', gameswon + 1) WHERE username = '{username}'""")
             cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))
             connect.commit()
             print("you won", creditpool, "congrats!!!")
             return
    for i in range(1, numplayers + 2):
        try:
            if i == 6:
                pass
            else:
                indexplayer = "player_" + str(i)
                if indexplayer not in creditdatabase:
                    creditpool += creditstracker.get(indexplayer)
        except:
            pass
    time.sleep(3)
    print("the first round of betting is over, bringing the total credits pool to:", creditpool)
    connect.commit()
    print("success")
    time.sleep(3)
    input("press enter to proceed to the next round")
    print("The Flop:")
    time.sleep(2)
    for i in communitycards:
        print(i)
        time.sleep(1.5)
    try:
        creditstracker, players, highestbet, deadplayer, creditdatabase  = betting(creditstracker, numplayers, playernum, players, 0, "no", 2, communitycards, creditdatabase)
    except:
        if len(players) != 1:
            print("good game, better luck next time!")
            print("you lost a total of", creditstracker[playernum])
            cursor.execute(f"""UPDATE users SET (credits, gameslost) = ('{winnercredits - creditstracker.get(playernum)}', gameslost + 1) WHERE username = '{username}'""")
            cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))
            connect.commit()
            return
        else:
             print("all other players folded, you win!")
             time.sleep(2)
             cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{winnercredits + creditpool}', gameswon + 1) WHERE username = '{username}'""")
             cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))
             connect.commit()
             print("you won", creditpool, "congrats!!!")
             return
    for i in range(1, numplayers + 2):
        try:
            indexplayer = "player_" + str(i)
            if indexplayer not in creditdatabase:
                creditpool += creditstracker.get(indexplayer)
        except:
            pass
    #creditpool = creditpool + deadplayer
    print("the second round of betting is over, bringing the total credits pool to:", creditpool)
    time.sleep(3)
    input("press enter to proceed to the next round")
    print("The Turn:")
    time.sleep(3)
    communitycards.append(deck.cards[0])
    deck.cards.remove(deck.cards[0])
    for i in communitycards:
        print(i)
        time.sleep(1)
    try:
        creditstracker, players, highestbet, deadplayer, creditdatabase  = betting(creditstracker, numplayers, playernum, players, 0, "no", 3, communitycards, creditdatabase)
    except:
        if len(players) != 1:
            print("good game, better luck next time!")
            print("you lost a total of", creditstracker[playernum])
            cursor.execute(f"""UPDATE users SET (credits, gameslost) = ('{winnercredits - creditstracker.get(playernum)}', gameslost + 1) WHERE username = '{username}'""")
            cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))
            connect.commit()
            return
        else:
            print("all other players folded, you win!")
            time.sleep(2)
            cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{winnercredits + creditpool}', gameswon + 1) WHERE username = '{username}'""")
            cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))
            print("you won", creditpool, "congrats!!!")
            connect.commit()
            return
    for i in range(1, numplayers + 2):
        try:
            indexplayer = "player_" + str(i)
            if indexplayer not in creditdatabase:
                creditpool += creditstracker.get(indexplayer)
        except:
            pass
    #creditpool = creditpool + deadplayer
    print("the third round of betting is over, bringing the total credits pool to:", creditpool)
    time.sleep(3)
    input("press enter to proceed to the next round")
    print("The River")
    communitycards.append(deck.cards[0])
    deck.cards.remove(deck.cards[0])
    for i in communitycards:
        print(i)
        time.sleep(1)
    time.sleep(3)
    print("its time for The Showdown")
    time.sleep(1.5)
    try:
        creditstracker, players, highestbet, deadplayer, creditdatabase = betting(creditstracker, numplayers, playernum, players, 0, "no", 4, communitycards, creditdatabase)
    except:
        if len(players) != 1:
            print("good game, better luck next time!")
            time.sleep(2)
            print("you lost a total of", creditstracker[playernum])
            cursor.execute(f"""UPDATE users SET (credits, gameslost) = ('{winnercredits - creditstracker.get(playernum)}', gameslost + 1) WHERE username = '{username}'""")
            cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))
            connect.commit()
            return
        else:
             print("all other players have folded, you win!")
             time.sleep(2)
             cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{winnercredits + creditpool}', gameswon + 1) WHERE username = '{username}'""")
             cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))
             connect.commit()
             print("you won", creditpool, "congrats!!!")
             return
    for i in range(1, numplayers + 2):
        try:
            indexplayer = "player_" + str(i)
            if indexplayer not in creditdatabase:
                creditpool += creditstracker.get(indexplayer)
        except:
            pass
    #creditpool = creditpool + deadplayer
    print("the final round of betting is over, bringing the total credits pool to:", creditpool)
    time.sleep(3)
    print("and the winner of the poker match is.................")
    winner = 0
    thewinner = []
    highestrank = 0
    rankindex = []
    rankmax = 0
    half = 0
    for i in range(1, 6):
        player = "player_" + str(i)
        if player in players:
            hand = players.get(player) + communitycards
            score = pokercalc(hand)
            lastscore.append(score)
    print(lastscore)
    for i in range(0, len(lastscore)):
        if max(winner, lastscore[i]) == lastscore[i]:
            winner = lastscore[i]
            thewinner = []
            thewinner.append(i+1)
        elif winner == lastscore[i] and winner != 0:
            thewinner.append(i+1)
    if len(thewinner) > 1:
        for i in range(1, 6):
            player = "player_" + str(i)
            if i + 1 in thewinner:
                hand = players.get(player) + communitycards
                for i in range(0, len(hand)):
                    if hand[i].value > hand[i+1].value:
                       highestrank = hand[i]
                if highestrank > rankmax:
                    rankmax = highestrank
                    rankindex = []
                    rankindex.append(i + 1)
                elif highestrank == rankmax:
                    rankindex.append(i + 1)

    overallcreditpool = winnercredits + creditpool
    if len(thewinner) == 1:
        winner = "player_" + str(thewinner[0])
        print(winner,"!")
        if winner == playernum:
            cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{overallcreditpool}', gameswon + 1) WHERE username = '{username}'""")
            connect.commit()
            print("you won", creditpool, "congrats!!!")
        else:
            print("you lost a total of", creditstracker[playernum])
            cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{winnercredits - creditstracker.get(playernum)}', gameslost + 1) WHERE username = '{username}'""")
            connect.commit()
    
    elif len(thewinner) != 1 and len(rankindex) == 1:
        winner = "player_" + str(rankindex[0])
        print(winner,"!")
        if winner == playernum:
            cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{overallcreditpool}', gameswon + 1) WHERE username = '{username}'""")
            connect.commit()
            print("you won", creditpool, "congrats!!!")
        else:
            print("you lost a total of", creditstracker[playernum])
            cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{winnercredits - creditstracker.get(playernum)}', gameslost + 1) WHERE username = '{username}'""")
            connect.commit()

    elif len(thewinner) != 1 and len(rankindex) != 1:
        winnercheck = 0
        winnercheck1 = 1
        print("a tie between:")
        for i in range(0, len(rankindex)):
            winner = "player_" + str(rankindex[i])
            print(winner)
            time.sleep(1)
            print("and")
            time.sleep(1)
            if winner == playernum and winnercheck == 0:
                creditpool = creditpool / len(rankindex)
                overallcreditpool = winnercredits - creditpool
                cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{overallcreditpool}', gameswon + 1) WHERE username = '{username}'""")
                connect.commit()
                print("you won", creditpool / len(rankindex), "congrats!!!")
                winnercheck = 1
        if winnercheck == 0:
            print("you lost a total of", creditstracker[playernum])
            cursor.execute(f"""UPDATE users SET (credits, gameswon) = ('{winnercredits - creditstracker.get(playernum)}', gameslost + 1) WHERE username = '{username}'""")
            connect.commit()

    for i in creditstracker:
        if i != winner:
            creditstracker.update({i: -abs(creditstracker.get(i))})

    cursor.execute("""INSERT INTO Game_History (username, GameID, P1_outcome, P2_outcome, P3_outcome, P4_outcome, P5_outcome, playernumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (username, 2, creditstracker.get("player_1"), creditstracker.get("player_2"), creditstracker.get("player_3"), creditstracker.get("player_4"), creditstracker.get("player_5"), playernum))    
            

    connect.commit()
    connect.close()
   




    print("thankyou all for playing!")







    time.sleep(2)

def slot():



def randomsalt():
    salt = 256*3//4
    return secrets.token_urlsafe(salt)

    

def hash_algo(salt, password):
    salt = bytes(salt, 'utf-8')
    password = bytes(password, 'utf-8')
    digest = hmac.new(salt, password, hashlib.sha256)
    return digest.hexdigest()

connect = sqlite3.connect('casino.db')
cursor = connect.cursor()
username = ""
loop = True
loop1 = True
loop2 = True

while loop == True:
    login_create = input("would you like to create a new account or login? n or l: ")
    if login_create == "n":
        credits = 10000
        while loop1 == True:
            if len(username) == 0:
                username = input("enter a username. User name cannot be longer than 10 characters")   
            if len(username) < 11:
                password = input("enter a password. Password must have at least 1 captial and be at least 8 characters long")
                if len(password) > 7:                    
                    for upper in password:
                        if upper.isupper() == True:
                            loop1 = False
                            break
                    if loop1 == True:
                        
                        print("there is no uppercase letter in the password")
                else:
                    print("password is not at least 8 characters")
            else:
                print("username is longer than 10 characters")
                username = ""

        while loop2:
            try:
                salt = randomsalt()
                password = hash_algo(salt, password)
                cursor.execute("""INSERT INTO users (username, password, credits, gameswon, gameslost, salt) VALUES (?, ?, ?, ?, ?, ?)""",
                        (username, password, credits, 0, 0, salt))                
                connect.commit()
                cursor.close()
                connect.close()
                loop = False
                loop2 = False
            except:
                print("that username already exists please pick another one")
                username = input("enter a username. User name cannot be longer than 10 characters")
                

    elif login_create == "l":
            while loop:
                username = input("enter username:")
                password = input("enter password:")
                success, message, name = checklogin(username, password)
                if success:
                    loop = False
                    print(message,name)
                else:
                    print(message)
                    
    else:
        print("pick a valid option!!!")



def selectgame():
    connect = sqlite3.connect('casino.db')
    cursor = connect.cursor()
    loop = True
    loop1 = True
    while loop == True:
        game = input("would you like to play poker or blackjack view your last five games played or quit the ganme, enter p, b or q. If you would like to view your profile statistics, navigate to the profile hub.")
        if game == "p":
            poker()
            while loop1 == True:
                again = input("play again? y or n")
                if again == "y":
                    loop1 = False
                elif again == "n":
                    print("thankyou for playing")
                    loop = False
                    loop1 = False
                else:
                    print("please enter a valid input")
        elif game == "b":
            blackjack()
            while loop1 == True:
                again = input("play again? y or n")
                if again == "y":
                    loop1 = False
                elif again == "n":
                    print("thankyou for playing")
                    loop = False
                    loop1 = False
                else:
                    print("please enter a valid input")
        elif game == "q":
            print("thankyou for playing!")
            loop = False
            
        elif game=="slot":
            slot()
            while loop1 == True:
                again = input("play again? y or n")
                if again == "y":
                    loop1 = False
                elif again == "n":
                    print("thankyou for playing")
                    loop = False
                    loop1 = False
                else:
                    print("please enter a valid input")
        elif game == "q":
        else:
            print("enter a valid option!!!")

selectgame()