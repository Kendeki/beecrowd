from sys import stdin

input()
cases = list(stdin.readlines())

for i in range(0, len(cases), 3):
    print(f"Instancia {int(i/3 + 1)}")
    team1, team2 = 0, 0
    mTeam1, mTeam2 = -1, -1

    for j in range(len(cases[i])):
        if cases[i][j] == cases[i + 1][j]: team1 += 1
        if cases[i][j] == cases[i + 2][j]: team2 += 1
        if cases[i][j] == cases[i + 1][j] and not cases[i][j] == cases[i + 2][j]: mTeam1 = 1
        if cases[i][j] == cases[i + 2][j] and not cases[i][j] == cases[i + 1][j]: mTeam2 = 1
    
    if team1 > team2 or mTeam1:
        print("time 1\n")
    elif team2 > team1 or not mistake:
        print("time 2\n")
    
    else:
        print("empate\n")