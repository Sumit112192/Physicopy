from flask import Flask, request, render_template, jsonify

from physics.coordinateSystem import SphericalCoordinatesFromPoint
from physics.approximate import convertToMultipleOfPi
import physics.quantities as quantities
from search.showSimilarWord import similarQuantity
import time
app = Flask(__name__)


headings = ("Quantity","dimensions")
data = (
    ("length","1,0,0,0,0,0,0"),
    ("mass","0,1,0,0,0,0,0"),
    ("time","0,0,1,0,0,0,0")
)
@app.route('/')
@app.route('/home')
def index():
	return render_template('home.html')
@app.route('/changeincoordinate')
def changeInCoordinate():
	return render_template('changeInCoordinate.html')

@app.route('/cartesianchange')
def cartesianChange():
	return render_template('cartesianChange.html')

@app.route('/dimension')
def dimension():

	return render_template('dimension.html')

@app.route('/dimension/table')
def table():
    return render_template('table.html',headings = headings,data=data)
@app.route("/search/<string:box>")
def process(box):
	query = request.args.get('query')
	words = similarQuantity(query)
	while(len(words)==0):
		time.sleep(1)
		query = request.args.get('query')
		words = similarQuantity(query)
	print(words)
	suggestions = []
	for word in words:
		suggestions.append({'value':word , 'data':word})
	print(suggestions)
	return jsonify({"suggestions":suggestions})
@app.route('/sphericalchanged', methods=['GET', 'POST'])
def sphericalChanged():
	if request.method == "POST":
		# getting input with name = fname in HTML form
		x = request.form.get("x")
		# getting input with name = lname in HTML form 
		y = request.form.get("y")
		z = request.form.get("z")
		to = request.form.get("to")
		point = SphericalCoordinatesFromPoint((float(x), float(y), float(z)))
		r = point.getR()
		theta = point.getTheta()
		phi = point.getPhi()
		#theta = convertToMultipleOfPi(point.getTheta())
		#phi = convertToMultipleOfPi(point.getPhi())

		return render_template("sphericalChanged.html",x=x, y=y, z=z, r=r, theta=theta, phi=phi, to=to)
	return render_template("cartesianChange.html")
if __name__ == "__main__":
	app.run(debug=True)
