data = """
Varus Varus	Defeat	0/2/3	ItemsItemsItemsItemsItemsItems	25:43	2023-07-07	WBG vs Ultra Prime	LPL Summer 2023
Aphelios Aphelios	Defeat	0/3/1	ItemsItemsItemsItems	21:29	2023-07-07	WBG vs Ultra Prime	LPL Summer 2023
"""

lines = data.strip().split('\n')
extracted_data = []

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
