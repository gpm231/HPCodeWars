total_games = int(input())

front_team = str(input())

m=(front_team.split())
winner=(m[0])

wins=(int(m[1]))

second_team = str(input())

n=(second_team.split())
losses=(int(n[2]))

z=(total_games-wins-losses)+1
magic_number=str(z)

print(winner+ " must win " + magic_number + " matches")