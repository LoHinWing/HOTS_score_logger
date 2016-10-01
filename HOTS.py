import time

target= open("Herolist.txt", "r")

roster = eval(target.read())


def game():
    hero_called = raw_input("Input hero name (or \"list\" for a list of heroes):")

    if hero_called == "list":
        print "List of Heroes:"
        for names in sorted(roster.iterkeys()):
            print "\t", names
        game()
    elif hero_called in roster:
        print "===" + hero_called + "==="
        print "Your current score = ", roster[hero_called]
        print "Update your stats! (input 0 for all if you don't want to update)"
        kills = raw_input("Kills: ")
        assists = raw_input("Assists: ")
        deaths = raw_input("Deaths: ")
        old_score = roster[hero_called]
        new_score = int(kills) * int(assists) - int(deaths) * 10
        roster[hero_called] = new_score + old_score
        print "Score updated! New score: ", roster[hero_called]
        target2 = open("Herolist.txt", "w")
        target2.write(str(roster))
        target2.close()
        time.sleep(5)
    elif hero_called == "quit":
        print "Bye!"
        time.sleep(5)
    else:
        print "No such command/hero! Try again/Type \"quit\""
        game()

game()
