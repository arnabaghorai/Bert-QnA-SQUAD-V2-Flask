from flask import request
from flask import jsonify
from flask import Flask
from Code.Inference import main


app=Flask(__name__)


@app.route("/predict" , methods = ['POST' , 'GET'])
def predict() :
	message = request.get_json(force = True)
	ques = message["quest"]

	a = main(paragraph = "para.txt" , questions = [ques])

	response = {
		"reply" : a[0]
	}

	return jsonify(response)
if __name__ == "__main__":
	app.run()
