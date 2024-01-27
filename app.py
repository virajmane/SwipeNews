from flask import Flask, render_template, request, jsonify
from newsscrapper import start

app = Flask(__name__)

@app.route('/')
def index():
    state_data = start()
    #return state_data
    return render_template('index.html', state_data = state_data)


@app.route('/record_preference', methods=['POST'])
def record_preference():
    direction = request.form.get('direction')
    news_id = request.form.get('newsId')
    # Handle the user's preference and update the database
    # Implement this based on your server-side logic

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
