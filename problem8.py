team_names=str(input())
names=team_names.split()

score_set1=str(input())
scores1=score_set1.split()

score_set2=str(input())
scores2=score_set2.split()

#score_set3=str(input())
#scores3=score_set3.split()

sets_team1 = 0
sets_team2 = 0

score1_team1 = int(scores1[0])
score1_team2 = int(scores1[2])

score2_team1 = int(scores2[0])
score2_team2 = int(scores2[2])

if score1_team1 > score1_team2:
    sets_team1=sets_team1 + 1

else:
    sets_team2=sets_team2 + 1

if score2_team1 > score2_team2:
    sets_team1=sets_team1 + 1

else:
    sets_team2=sets_team2 + 1

if sets_team1==sets_team2:
    score_set3=str(input())
    scores3=score_set3.split()
    score3_team1 = int(scores3[0])
    score3_team2 = int(scores3[2])

    if score3_team1 > score3_team2:
        sets_team1=sets_team1 + 1
        print(names[0] + " won the match " + str(sets_team1) + " - " + str(sets_team2) + ".")

    else:
        sets_team2=sets_team2 + 1
        print(names[2] + " won the match " + str(sets_team2) + " - " + str(sets_team1) + ".")

else:
    if sets_team1 > sets_team2:
        print(names[0] + " won the match " + str(sets_team1) + " - " + str(sets_team2) + ".")

    else:
        print(names[2] + " won the match " + str(sets_team2) + " - " + str(sets_team1) + ".")





