# app.py
from flask import Flask, jsonify,request
from api_data import get_news  # Import the function from api_data.py
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/news/')
def index():
    # Fetch the news data
    tickers = request.args.get('tickers')  # Get the tickers query parameter
    start = request.args.get('start')
    end = request.args.get('end')

    if tickers:
        ticker_list = tickers.split(',')  # Split the tickers by commas
        #print(ticker_list)  # ['TSLA', 'MSFT', 'AAPL']
        articles = get_news(ticker_list,start,end)
        
        return jsonify(articles)
    else:
        return "Failed to fetch news data", 500

if __name__ == "__main__":
    app.run(debug=True)
