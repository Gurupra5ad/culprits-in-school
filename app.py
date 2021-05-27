from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify, json
from flask_mongoengine import MongoEngine


app = Flask(__name__)

DB_URI = "mongodb+srv://guruprasad:SCaxg0y8vQTCVXrh@cluster0.sne4s.mongodb.net/culprits?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI

database_name = "culprits"
db = MongoEngine()
db.init_app(app)

class Complaints(db.Document):
    name = db.StringField()
    insti = db.StringField()
    insti_name = db.StringField()
    desig = db.StringField()
    descp = db.StringField()
    evidence = db.StringField()


    def to_json(self):
        return {
            "name":self.name,
            "insti":self.insti,
            "insti_name":self.insti_name,
            "desig":self.desig,
            "descp":self.descp,
            "evidence":self.evidence
        }

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        name=request.form['name']
        insti = request.form['insti']
        insti_name = request.form['insti_name']
        desig = request.form['desig']
        descp = request.form['descp']
        evidence = request.form['evidence']
        
        complaint = Complaints(name=name, insti=insti, desig =desig, descp=descp, insti_name = insti_name, evidence = evidence )
        complaint.save()
        
        return redirect('/success', code=302)
    
    return render_template('home.html')

@app.route("/complaints")
def complaints():
    complaints=[]
    for complaint in Complaints.objects:
        complaints.append(complaint)
    
    return render_template("complaint.html", complaints=complaints, n=len(complaints))

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
