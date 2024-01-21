import requests
from flask import Flask,render_template,url_for
from flask import request as req
import re

app = Flask(__name__)




@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method== "POST":

        data=req.form["data"]
        
        matching_emails = re.findall(r'[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}', data)
        matching_urls = re.findall(r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#()?&//=]*)', data)
        matching_phones = re.findall(r'\b(?:\+\d{1,3}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,10}\b', data)
        matching_dates = re.findall(r'\b(?:\d{4}-\d{2}-\d{2})|(?:\d{1,2}\/\d{1,2}\/\d{2,4})\b', data)

        
        API_URL = ""
        headers = {"Authorization": f"Bearer "}

        API_URL = ""  
        headers = {"Authorization": f"Bearer "}  

        max_length = int(req.form["maxL"])
        min_length = max_length // 4

        payload = {
            "inputs": data,
            "parameters": {"min_length": min_length, "max_length": max_length},
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.json()[0]


        return render_template("index.html",  emails=matching_emails, urls=matching_urls, phones=matching_phones, dates=matching_dates)
    else:
        return render_template("index.html")

@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
