total_games = int(input())

front_team = str(input())

m=(front_team.split())
wins=(int(m[1]))

second_team = str(input())

n=(second_team.split())
losses=(int(n[2]))

magic_number=(total_games-wins-losses)+1
print(magic_number)