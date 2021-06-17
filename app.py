from flask import Flask, request, render_template, jsonify, redirect

from physics.coordinateSystem import SphericalCoordinatesFromPoint
from physics.approximate import convertToMultipleOfPi
import physics.quantities as quantities
import physics.dimensions as dimensions
from search.showSimilarWord import similarQuantity
import time
import os
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

@app.route('/dimension')
def dimension():
	data = quantities.quantity
	return render_template('dimension.html', suggestion = data, toggle = 1)

@app.route('/dimension/table', methods=['GET', 'POST'])
def dimensionTable():
	if request.method == "POST":
		headings = ("Quantity", "Dimensions")
		data = request.form.get('quantity')
		data = data.lower()
		showAll = request.form.get("showAll")
		if showAll == "yes" and data == "":
			row = []
			for data in quantities.quantity:
				row.append([data, dimensions.dimensions[data]])
			return render_template('table.html', headings=headings, row=row, suggestion=quantities.quantity, toggle = 0)
		elif showAll == "no"  and data=="":
			return redirect('/dimension')
		else:
			try:
				data = data.strip(" ")
				row = [[data, dimensions.dimensions[data]]]

				return render_template('table.html', headings=headings, row=row, suggestion=quantities.quantity,toggle = 1)
			except:
				quantity = similarQuantity(data)
				return render_template('didYouMean.html', quantity=quantity, suggestion=quantities.quantity, toggle=1)
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