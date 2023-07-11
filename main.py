data = """
LeBlanc LeBlanc	Victory	4/0/6	ItemsItemsItemsItemsItemsItems	29:14	2023-07-08	OMG vs TT	LPL Summer 2023
Jayce Jayce	Victory	8/2/8	ItemsItemsItemsItemsItemsItems	29:32	2023-07-08	OMG vs TT	LPL Summer 2023
Tristana Tristana	Victory	13/0/6	ItemsItemsItemsItemsItemsItems	27:28	2023-07-06	TT vs IG	LPL Summer 2023
Tristana Tristana	Victory	8/1/5	ItemsItemsItemsItemsItemsItems	30:25	2023-07-06	TT vs IG	LPL Summer 2023
Neeko Neeko	Victory	4/2/14	ItemsItemsItemsItemsItemsItems	40:36	2023-07-04	EDG vs TT	LPL Summer 2023
Azir Azir	Victory	11/1/10	ItemsItemsItemsItemsItemsItems	35:58	2023-07-04	EDG vs TT	LPL Summer 2023
Azir Azir	Defeat	10/5/8	ItemsItemsItemsItemsItemsItems	41:14	2023-07-04	EDG vs TT	LPL Summer 2023
"""

lines = data.strip().split('\n')
extracted_data = []

total_kills = 0
num_matches = len(lines)

for line in lines:
    line = line.strip()
    elements = line.split('\t')

    champion = elements[0]
    outcome = elements[1]
    kda = elements[2]
    game_time = elements[4]
    match_date = elements[5]
    match_details = elements[6]
    
    #used to separate kills, deaths, and assists
    kda_values = kda.split('/') #delimiter between '/'
    kills = int(kda_values[0])
    deaths = int(kda_values[1])
    assists = int(kda_values[2])

    total_kills += kills
    extracted_data.append((champion, outcome, kda, kills, deaths, assists, game_time, match_date, match_details))

average_kills = round(total_kills / num_matches, 3)

"""
for champion, outcome, kda, kills, deaths, assists, game_time, match_date, match_details in extracted_data:
    print(f"Champion: {champion}")
    print(f"Outcome: {outcome}")
    print(f"KDA: {kda}")
    print(f"Kills: {kills}")
    print(f"Deaths: {deaths}")
    print(f"Assists: {assists}")
    print(f"Game Time: {game_time}")
    print(f"Match Date: {match_date}")
"""

print(f"Total Kills: {total_kills}")
print(f"Number of Matches: {num_matches}")
print(f"Average Kills per Match: {average_kills}")