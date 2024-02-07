from flask import Flask, render_template, url_for, request, redirect
from models import db, Tree
from datetime import date
app = Flask(__name__)

"""
This function handles requests to the home page and returns the index.html template.
"""

@app.route("/")
def home_page():
   return render_template("/index.html")

@app.route("/treelist.html")
def tree_list():
    render_template("/TreeList.html")

@app.route("/form_page.html")
def form_page():
    return render_template("/form_page.html")


@app.route('/tree_table.html')
def tableshow():
    # We need to pass trees as a variable, called from the db, to the HTML/Jinja template.
    trees = Tree.select()
    return render_template('/tree_table2.html', trees = trees)

@app.route('/submit_form', methods=['POST', 'GET'])

def submit_form():
    if request.method == "POST":
        data = request.form

        species_name = data['species_name']
        diameter = float(data['diameter'])
        post_date = Tree.postdate
        activity = data["activity"]


    # Validate and sanitize data if needed (e.g., check for empty fields or invalid input)

        # Create a new Tree instance
        tree = Tree.create(species=species_name, diameter=diameter, post_date = post_date, activity=activity)

    # Redirect to a success page or display a confirmation message
        return render_template("/thankyou.html")  # Example redirect

# Database connection and table creation.
db.connect()
db.drop_tables([Tree])
db.create_tables([Tree])
print(f"{Tree._meta.fields} coming from the app.py script.")
print(db.get_columns("Tree"))

# View functions and other app logic, including:
# test = Tree.create(species="Oak", diameter=10.0, postdate=postdate)  # Within a suitable context

if __name__ == '__main__':

    app.run(debug=True)