spain = {"wins":0 , "loses":0 , "draws":0 ,"goal difference":0 , "points":0}
iran = {"wins":0 , "loses":0 , "draws":0 ,"goal difference":0 , "points":0}
protugal = {"wins":0 , "loses":0 , "draws":0 ,"goal difference":0 , "points":0}
morroco = {"wins":0 , "loses":0 , "draws":0 ,"goal difference":0 , "points":0}
teams = [iran, spain, protugal, morroco]
def team_win_update(team):
    team.update({"wins":team.get("wins")+1})
    team.update({"points":team.get("points")+3})

def team_lose_update(team):
    team.update({"loses":team.get("loses")+1})

def team_tie_update(team):
    team.update({"draws": team.get("draws")+1})
    team.update({"points": team.get("points")+1})

def team_goal_diff_update(team, goals):
    team.update({"goal difference": team.get("goal difference")+goals})

for i in range(4):
    for j in range(3-i)
    a,b = list(map(int, input().split("-")))
    goal_diff = a-b
    if a == b:
        

