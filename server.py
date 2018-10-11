from flask import Flask, render_template, request
import process

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/setTitle")
def setTitle():
    addr = request.args.get('addr')
    info = process.getInfo(addr)
    return render_template("customize.html", addr=addr, name=info['name'], artist=info['artist'], title=info['title'])

@app.route("/startProcess")
def startProcess():
    fileInfo = {
        "name":request.args.get('name'),
        "title":request.args.get('title'),
        "artist":request.args.get('artist'),
        "changeVol":request.args.get('changeVol'),
        "addToiTunes":True if request.args.get('addToiTunes') == 'on' else False
    }
    if process.wholeProcess(request.args.get('addr'), fileInfo):
        return render_template("output.html", success=True)
    return render_template("output.html", success=False)

app.run(debug=True, host='0.0.0.0', port=80)