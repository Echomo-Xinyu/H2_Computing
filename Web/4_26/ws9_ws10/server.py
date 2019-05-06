from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
# from flask import *

app = Flask(__name__)


@app.route("/")  ## decorate function
def root():
    handle = open("products.txt")
    products_list = []
    for line in handle:
        result = line.strip().split(",")
        products_list.append(result)
    handle.close()
    return render_template("products.html", products=products_list)


@app.route("/product", methods=["GET", "POST"])
def display_add_product():
    return render_template("product_frm.html")


@app.route("/add", methods=["POST"])
def add_product():
    image_file_name = ""
    file_handler = open("products.txt", "a")
    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name = image_file.filename
        image_file.save("static/images" + image_file_name)
    file_handler.write("\n" + request.form["name"] + ", " +
                       request.form["description"] + ", " +
                       request.form["price"] + ", " + image_file_name)
    file_handler.close()
    return redirect("/")


app.run()
