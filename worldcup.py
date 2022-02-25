
spain = {"name":"Spain","wins":0 , "loses":0 , "draws":0 ,"goal difference":0 , "points":0}
iran = {"name":"Iran","wins":0 , "loses":0 , "draws":0 ,"goal difference":0 , "points":0}
portugal = {"name":"Portugal","wins":0 , "loses":0 , "draws":0 ,"goal difference":0 , "points":0}
morocco = {"name":"Morocco","wins":0 , "loses":0 , "draws":0 ,"goal difference":0 , "points":0}

teams = [iran, spain, portugal, morocco]

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

def compare_points(team):
    return team.get("points")

def compare_wins (team):
    return team.get("wins")

def compare_name (team):
    return ord("z") - ord(team.get("name")[0])

def print_team(team):
    print("{}  wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}".format(team.get("name"), team.get("wins"), team.get("loses"), team.get("draws"), team.get("goal difference"), team.get("points")))

for i in range(3):
    for j in range(3-i):
        a,b = list(map(int, input().split("-")))
        if a == b:
            team_tie_update(teams[i])
            team_tie_update(teams[j+i+1])
        if a > b:
            team_win_update(teams[i])
            team_goal_diff_update(teams[i],a-b)
            team_lose_update(teams[j+i+1])
            team_goal_diff_update(teams[j+i+1],b-a)
        if a < b:
            team_win_update(teams[j+i+1])
            team_goal_diff_update(teams[j+i+1],b-a)
            team_lose_update(teams[i])
            team_goal_diff_update(teams[i],a-b)

teams.sort(key=lambda x: (compare_points(x), compare_wins(x), compare_name(x)), reverse=True)

for team in teams:
    print_team(team)



