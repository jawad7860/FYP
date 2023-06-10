PATH_TO_REPO = r'C:\Users\hassa\Music\utae-paps-main'
PATH_TO_DATA = r'C:\Users\hassa\Music\PASTIS'
PATH_TO_UTAE_WEIGHTS = r"C:\Users\hassa\Music\UATE_zenodo"
#PATH_TO_UTAEPaPs_WEIGHTS = r"D:\fyp\UTAE+PAPs_PanopticSeg_weights\UTAE_PAPs"
device = 'cpu' # or "cpu"

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


import time
from PIL import Image
from flask import Flask, render_template, request, url_for
import json


import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib

from matplotlib import patches
import numpy as np




# Colormap (same as in the paper)
cm = matplotlib.cm.get_cmap('tab20')
def_colors = cm.colors
cus_colors = ['k'] + [def_colors[i] for i in range(1,19)]+['w']
cmap = ListedColormap(colors = cus_colors, name='agri',N=20)

label_names = [
"Background",
"Meadow",
"Soft winter wheat",
"Corn",
"Winter barley",
"Winter rapeseed",
"Spring barley",
"Sunflower",
"Grapevine",
"Beet",
 "Winter triticale",
 "Winter durum wheat",
 "Fruits,  vegetables, flowers",
 "Potatoes",
 "Leguminous fodder",
 "Soybeans",
 "Orchard",
 "Mixed cereal",
 "Sorghum",
 "Void label"]



app = Flask(__name__)  # create the Flask app


# In[7]:

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")


NAME = str()

@app.route("/deepfarm",methods=['GET', 'POST'])
def deepfarm():

    if request.method == 'GET':
        return render_template("deepfarm.html", msg='')

    image = request.files['file']    
    NAME = image.filename
    file = open("img.txt",'w')
    file.write(NAME) 
    file.close()
    return render_template("deepfarm.html",msg=image.filename)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)







@app.route('/upload',methods=['GET','POST'])
def upload():
    #demo=random.randint(2000, 5000)

    file = open("img.txt","r")
    name=file.read()
    
    file.close()

    Pred = 'p'+name

    Label ='l'+name

    
    
    return render_template("complete2.html", image_output=name,image_output1=Label,image_output2=Pred)
if __name__ == '__main__':
    # Change the port number to the desired value
    app.run(port=5002)

