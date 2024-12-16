from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        prompt = handle_query(query)
        response = generate_response(prompt)  # Assuming you have a `generate_response` function
        return render_template('index.html', query=query, response=response)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)