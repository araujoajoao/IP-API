from flask import Flask, request, redirect, url_for
import requests
import json
import io
 
app = Flask(__name__)
 
app.config['DEBUG'] = True

@app.route('/history')
def content(): 
    with io.open('ipapi.json', "r", encoding="utf-8") as history:
        return history.read()

@app.route('/result/<string:accKey>/<string:ip>/<string:continent_name>/<string:region_name>/<string:zip_code>/<string:capital>')
def result(accKey, ip, continent_name, region_name, zip_code, capital): return '<h3>Continent Name: {};  <br> Region Name: {}; <br>  Zip Code: {}; <br> Capital Name: {}; <br> Your Access Key: {};<br>IP:{} </h3>'.format(continent_name, region_name, zip_code, capital, accKey, ip)

@app.route('/', methods=['GET', 'POST'])
def ipapi():
    if request.method == 'GET':
        return '''<h1>Please fill out with Access Key and IP address</h1>
                    <form method="POST" action="/">
                    <input type="text" name="accKey">
                    <input type="text" name="ip">
                    <input type="submit" value="Request">
                </form>'''
    else:
        accKey = request.form['accKey']
        ip     = request.form['ip']
 
        req = requests.get('http://api.ipapi.com/' + ip + '?access_key=4b441b7d00ae432f6864810c14136db6')
        response = req.json()
 
        continent_name = response['continent_name']
        region_name    = response['region_name']
        zip_code       = response['zip']
        capital        = response["location"]["capital"]        

        with io.open('ipapi.json', "a", encoding="utf-8") as file: 
            file.write(ip + "\n" + continent_name + "\n" + region_name + "\n" + zip_code + "\n" + capital + "\n" "\r\n")

        return redirect(url_for('result', accKey=accKey, ip=ip, continent_name=continent_name, region_name=region_name, zip_code=zip_code, capital=capital))
    
if __name__ == '__main__':
    app.run()