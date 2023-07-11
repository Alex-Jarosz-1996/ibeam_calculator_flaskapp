# Import the necessary modules
from flask import Flask, render_template, request
from ibeam_calc import ibeam

# Create an instance of Flask
app: Flask = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def home() -> str: 
    if request.method == 'POST':
        # Get the form data
        sigma = float(request.form['sigma'])
        force_applied = float(request.form['force_applied'])
        beam_thick = float(request.form['beam_thick'])
        num_distances = int(request.form['num_distances'])
        distances = [float(request.form[f'distance{i}']) \
                     for i in range(1, num_distances+1)]
        
        # using the ibeam() function to create the height, width
        # relationships
        ibeam_dict = ibeam(sigma, 
                           force_applied, 
                           beam_thick, 
                           distances)

        # Render the same template again
        return render_template('distance.html', 
                               sigma=sigma,
                               force_applied=force_applied,
                               beam_thick=beam_thick,
                               results=ibeam_dict)
        
    else:
        # rendering form template
        return render_template('base.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
