from flask import Flask, request, redirect, url_for
import requests
import json
 
app = Flask(__name__)
 
app.config['DEBUG'] = True
 
@app.route('/')
def index():
    return '<h1>IP API with Python Flask</h1>'
 
@app.route('/result/<string:accKey>/<string:ip>/<string:continent_name>/<string:region_name>/<string:zip_code>/<string:capital>')
def result(accKey, ip, continent_name, region_name, zip_code, capital):
   return '<h3>Continent Name: {};  <br> Region Name: {}; <br>  Zip Code: {}; <br> Capital Name: {}; <br> Your Access Key: {};<br>IP:{} </h3>'.format(continent_name, region_name, zip_code, capital, accKey, ip)
 
@app.route('/ipapi', methods=['GET', 'POST'])
def ipapi():
    if request.method == 'GET':
        return '''<h1>Please fill with IP Address</h1>
                    <form method="POST" action="/ipapi">
                    <input type="text" name="accKey">
                    <input type="text" name="ip">
                    <input type="submit" value="Request">
                </form>'''
    else:
        accKey = request.form['accKey']
        ip     = request.form['ip']
 
        req = requests.get('http://ipapi.co'+ ip + '?access_key=' + accKey)
        response = req.json()
 
        continent_name = response['continent_name']
        region_name    = response['region_name']
        zip_code       = response['zip']
        capital        = response["location"]["capital"]        
 
        return redirect(url_for('result', accKey=accKey, ip=ip, continent_name=continent_name,
                                 region_name=region_name, zip_code=zip_code, capital=capital))
 
if __name__ == '__main__':
    app.run(debug = True)