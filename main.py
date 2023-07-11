from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    lines = data.strip().split('\n')
    
    #initial variables
    extracted_data = []
    total_kills = 0
    num_matches = len(lines)

    num_victories = 0
    total_victory_kills = 0
    average_victory_kills = 0

    num_losses = 0
    total_loss_kills = 0
    average_loss_kills = 0

    for line in lines:
        line = line.strip()
        elements = line.split('\t')

        champion = elements[0]
        outcome = elements[1]
        kda = elements[2]
        game_time = elements[4]
        match_date = elements[5]
        match_details = elements[6]
        
        kda_values = kda.split('/')
        kills = int(kda_values[0])
        deaths = int(kda_values[1])
        assists = int(kda_values[2])

        total_kills += kills
        extracted_data.append((champion, outcome, kda, kills, deaths, assists, game_time, match_date, match_details))

        #tracks amount of victories in the dataset 
        if outcome == "Victory":
            num_victories += 1
            total_victory_kills += kills
        else:
            num_losses += 1
            total_loss_kills += kills

    average_kills = round(total_kills / num_matches, 3)
    average_victory_kills = round(total_victory_kills / num_victories, 3)
    average_loss_kills = round(total_loss_kills / num_losses, 3)
    kills_in_two_maps = average_kills * 2

    return render_template('index.html', extracted_data=extracted_data, total_kills=total_kills, num_matches=num_matches, 
                           average_kills=average_kills, kills_in_two_maps=kills_in_two_maps, num_victories=num_victories,
                           num_losses=num_losses, average_victory_kills=average_victory_kills, average_loss_kills=average_loss_kills)
if __name__ == '__main__':
    app.run()