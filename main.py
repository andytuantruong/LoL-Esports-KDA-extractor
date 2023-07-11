from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
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
        
        kda_values = kda.split('/')
        kills = int(kda_values[0])
        deaths = int(kda_values[1])
        assists = int(kda_values[2])

        total_kills += kills
        extracted_data.append((champion, outcome, kda, kills, deaths, assists, game_time, match_date, match_details))

    average_kills = round(total_kills / num_matches, 3)
    kills_in_two_maps = average_kills * 2

    return render_template('index.html', extracted_data=extracted_data, total_kills=total_kills, num_matches=num_matches, average_kills=average_kills, kills_in_two_maps=kills_in_two_maps)

if __name__ == '__main__':
    app.run()