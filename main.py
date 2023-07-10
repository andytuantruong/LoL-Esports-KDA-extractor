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
    
    extracted_data.append((champion, outcome, kda, game_time, match_date, match_details))

for champion, outcome, kda, game_time, match_date, match_details in extracted_data:
    print(f"Champion: {champion}")
    print(f"Outcome: {outcome}")
    print(f"KDA: {kda}")
    print(f"Game Time: {game_time}")
    print(f"Match Date: {match_date}")
