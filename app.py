import requests
from flask import Flask,render_template,url_for
from flask import request as req
import re

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method== "POST":
        API_URL = ""
        headers = {"Authorization": f"Bearer "}

        data=req.form["data"]
        pattern ='[^\”\“\"]+'
        c=re.findall(pattern,data)

        emailPattern="/^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$/ | /^([a-z0-9_\.\+-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/"
        urlPattern="/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#()?&//=]*)/ | /(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/ "
        phNoPattern="/^(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?"
        datePattern1="/([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/  "
        datePattern2="/^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/"
        datePattern3="/^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/"
        
        valEmail=""
        valPhNo=""
        valUrl=""
        valDate=""
        
        if(req.form.get("choice5")=="summarize"):
            maxL=int(req.form["maxL"])
            minL=maxL//4
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                "inputs":data,
                "parameters":{"min_length":minL,"max_length":maxL},
            })[0]
        if(req.form.get("choice1")=="email"):
            valEmail=re.findall(emailPattern,data);
        if(req.form["choice2"]=="url"):
            valUrl=re.findall(urlPattern,data);
        # if(req.form["choice3"]=="phNos"):
        #     valPhNo=re.findall(phNoPattern,data);
        if(req.form["choice4"]=="Dates"):
            valDate=re.findall(datePattern1,data);
            valDate+=re.findall(datePattern2,data);
            valDate+=re.findall(datePattern3,data);
        
        
        # 
        # print("uwu"+output["summary_text"])
        # print("uwu"+valEmail + valUrl + valPhNo +valDate)
        for i in valEmail:
            output["summary_text"]=str(i)+output["summary_text"];
            print(i)
        # for i in valUrl:
        #     output["summary_text"]=i+output["summary_text"];
        #     print(i)
        # # for i in valPhNo:
        # #     output["summary_text"]=i+output["summary_text"];
        # #     print(i)
        # for i in valDate:
        #     output["summary_text"]=i+output["summary_text"];
        #     print(i)
 
        return render_template("index.html",result= output["summary_text"])
    else:
        return render_template("index.html")