from flask import render_template, Flask, redirect,jsonify,request,send_from_directory

app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('home.html')

@app.route('/home')
def beranda1():
    return redirect('/')   

@app.errorhandler(404)
def NotFound(error):
    return render_template('error.html')

@app.route('/images/<path:namaFile>')
def myImg(namaFile):
    return send_from_directory('storage', namaFile)    


if __name__ == "__main__":
    app.run(debug=True, port=5000) 