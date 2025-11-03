from flask import Flask, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    # Últimos 7 días
    end_date = datetime.now() - timedelta(days=1)  # evitar futuro
    start_date = end_date - timedelta(days=6)  # 7 días total

    url = f"https://api.frankfurter.app/{start_date.strftime('%Y-%m-%d')}..{end_date.strftime('%Y-%m-%d')}?from=USD&to=COP"
    
    response = requests.get(url)
    data = response.json()

    # Si la API falla, usar datos de ejemplo
    if 'rates' not in data:
        dates = [(end_date - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)][::-1]
        rates = [5100, 5110, 5120, 5115, 5105, 5095, 5100]
    else:
        dates = sorted(data['rates'].keys())
        rates = [data['rates'][date]['COP'] for date in dates]

    return render_template('index.html', dates=dates, rates=rates)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
