# Import the necessary modules
from flask import Flask, render_template, request

# Create an instance of Flask
app: Flask = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def home() -> str: 
    if request.method == 'POST':
        # Get the form data
        sigma = request.form['sigma']
        force_applied = request.form['force_applied']
        beam_thick = request.form['beam_thick']

        # Process the form data (you can add your own logic here)

        # Render the same template again
        return render_template('index.html')
        
    else:
        return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
