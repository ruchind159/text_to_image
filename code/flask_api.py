from flask import Flask
from flask import send_file
import os
from gen_image import *

app = Flask(__name__)

current_dir=os.getcwd()
#loading model
bird_model=loading_model('bird')
coco_model=loading_model('coco')


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<dataset_name>/<sentence>")              #this is same as the grammar check function in main file
def generate_image(dataset_name,sentence):
	if dataset_name=='bird':
		generate_image_sent(sentence,bird_model)
	else:
		generate_image_sent(sentence,coco_model)

	filename=os.path.join(current_dir,'output/my_img_g2.png')
	return send_file(filename, mimetype='image/gif')

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)