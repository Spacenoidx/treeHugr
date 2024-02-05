from flask import Flask, render_template, url_for, request, redirect
from models import Tree

app = Flask(__name__)

@app.route("/")
def home_page():
   return render_template("/index.html")

@app.route("/treelist.html")
def tree_list():
    render_template("/TreeList.html")

@app.route("/form_page.html")
def form_page():
    return render_template("/form_page.html")

@app.route('/submit_form', methods=['POST', 'GET'])

def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()

        species_name = request.form['species_name']
        diameter = float(request.form['diameter'])

    # Validate and sanitize data if needed (e.g., check for empty fields or invalid input)

        # Create a new Tree instance
        tree = Tree.create(species=species_name, diameter=diameter)

    # Redirect to a success page or display a confirmation message
        return "nice!"  # Example redirect

