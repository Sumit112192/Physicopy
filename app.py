from flask import Flask, request, render_template
from physics.coordinateSystem import SphericalCoordinatesFromPoint
from physics.approximate import convertToMultipleOfPi
app = Flask(__name__)

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
