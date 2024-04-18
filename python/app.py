import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
# Define the upload route
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files['file']
        # Load the file into a DataFrame
        data = pd.read_csv(uploaded_file)
        # Pass the data to the next function
        return render_template('analyze.html', data=data.to_html())
    else:
        return render_template('upload.html')

# Define the analyze route
@app.route('/analyze')
def analyze():
    # Get the data from the query string
    data = request.args.get('data')
    # Load the data into a DataFrame
    df = pd.read_html(data)[0]
    # Analyze the data
    summary = df.describe()
    # Convert the summary to HTML
    summary_html = summary.to_html()
    # Display the summary
    return render_template('summary.html', summary=summary_html)

if __name__ == '__main__':
    app.run(debug=True)
