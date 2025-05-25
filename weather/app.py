from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = '4f6e5a65b8494bff677740730fd6e484'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    raw_data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        raw_data = response.text  # Show raw JSON to debug

        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed']
            }
        else:
            error = f"City not found or API error. Raw response: {raw_data}"

    return render_template('index.html', weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)
