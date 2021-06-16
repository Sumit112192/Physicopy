from flask import Flask, request, render_template, jsonify, redirect

from physics.coordinateSystem import SphericalCoordinatesFromPoint
from physics.approximate import convertToMultipleOfPi
import physics.quantities as quantities
import physics.dimensions as dimensions
from search.showSimilarWord import similarQuantity
import time
app = Flask(__name__)



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
	data = quantities.quantity
	return render_template('dimension.html', data = data)

@app.route('/dimension/table', methods=['GET', 'POST'])
def dimensionTable():
	if request.method == "POST":
		data = request.form.get('quantity')
		headings = ("Quantity","dimensions")
		data = [[data, dimensions.dimensions[data]]]
		print(data)
		return render_template('table.html',headings = headings,data=data)
	return redirect('/dimension')



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