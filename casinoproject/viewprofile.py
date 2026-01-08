import sqlite3
def viewprofile(username):
    connect = sqlite3.connect('C:/Users/samue/OneDrive/Desktop/casino venv/casino.db')
    cursor = connect.cursor()
    try:
        cursor.execute(f"""SELECT credits, gameswon, gameslost FROM users WHERE username = '{username}'""")
        viewprof = cursor.fetchall()
        me = []
        for i in viewprof:
            for n in i:
                me.append(n)
        credits = me[0]
        gameswon = me[1]
        gameslost = me[2]
        connect.commit()
        connect.close()
        return True, credits, gameswon, gameslost
    except:
        return False, 0, 1, 0
print(viewprofile('samuel'))




    # playeroutcomes = []
    # cursor.execute(f"""SELECT P1_Outcome, P2_Outcome, P3_Outcome, P4_Outcome, P5_Outcome FROM Game_History WHERE username = '{username}' ORDER BY RecordID DESC LIMIT 5 """)
    # [*playeroutcomes] = cursor.fetchall()
    # cursor.execute(f"""SELECT playernumber FROM Game_History WHERE username = '{username}'""")
    # connect.commit()
    # playernum = cursor.fetchone()   
    # playernum = str(playernum)
    # index = 0
    # game = 0
    # for i in playeroutcomes:
    #     index = 0
    #     game+=1
    #     for n in i:
    #         index += 1
    #         if str(index) in playernum:
    #             print("you:",n)
    #         else:
    #             print("player" + str(index),":",n)