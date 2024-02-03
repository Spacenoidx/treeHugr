from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def home_page():
    return "Sample!"

@app.route("/treelist.html")
def tree_list():
    return TreeList

@app.route("/formpage.html")
def form_page:
    render_template("")

@app.route('/submit-tree', methods=['POST'])

def submit_tree():
    species = request.form['species']
    diameter = float(request.form['diameter'])

    # Validate and sanitize data if needed (e.g., check for empty fields or invalid input)

    # Create a new Tree instance
    tree = Tree.create(species=species, diameter=diameter)

    # Redirect to a success page or display a confirmation message
    return redirect('/treelist.html')  # Example redirect

test = Tree.create(species = "Oak", diameter = "10.0")