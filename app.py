from flask import Flask,g,render_template,redirect,url_for,jsonify,request,flash
import barcode
from barcode.writer import ImageWriter
from PIL import Image
from skimage.io import imread
from skimage.util import img_as_ubyte
import os
import time

PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def input():
    return render_template("index.html")

@app.route("/edit-11/",methods=['GET','POST'])
def edit():
    if request.method=='POST':
        barcodeName=request.form.get('barcodeName')
        print("barcodeName:",barcodeName)
        Code_128="code128"
        ean=barcode.get(Code_128,barcodeName,writer=ImageWriter())
        f=ean.save(os.path.join(app.config['UPLOAD_FOLDER'],barcodeName))
        #sk_image=imread(f)
        #shapes_dim=sk_image.shape
        #sk_image=sk_image.flatten()
        #sk_image = sk_image.transpose(1,0,2).reshape(shapes_dim[1],-1) #convert to 2D array
        #image=img_as_ubyte(sk_image)
        return render_template("edit-11.html", user_image = os.path.join(os.getcwd()+"\\"+app.config['UPLOAD_FOLDER'],barcodeName+".png"))
    
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    #http://localhost:5000/
    host = os.environ.get('IP', 'localhost')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
