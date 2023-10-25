from flask import Flask,render_template,request,redirect,url_for
import requests
app=Flask(__name__)

URL="https://api.mfapi.in/mf/"
list1=[]

@app.route("/",methods=["POST","GET"])
def func1():
    if request.method=="POST":
        Name=request.form.get("Name")
        Fund_Code=request.form.get("Fund_Code")
        Funds=requests.get(URL+str(Fund_Code))
        Fund_house1=Funds.json().get("meta").get("fund_house")
        Invested_Amount=request.form.get("Invested_Amount")
        Unit_Held=request.form.get("Unit_Held")
        nav=Funds.json().get("data")[0].get("nav")

        dict1={}
        dict1.update({"Name":Name})
        dict1.update({"Fund_house1":Fund_house1})
        dict1.update({"Invested_Amount":Invested_Amount})
        dict1.update({"Unit_Held":Unit_Held})
        dict1.update({"nav":nav})
        current_value=float(dict1.get("nav"))*int(dict1.get("Invested_Amount"))
        dict1.update({"current_value":current_value})
        Growth=float(dict1.get("current_value"))-int(dict1.get("Unit_Held"))
        dict1.update({"Growth":Growth})

        list1.append(dict1)

    return render_template("home.html",list2=list1)

@app.route('/edit/<string:id>',methods=["POST","GET"])
def edit(id):
    if request.method=="POST":
        Name=request.form.get("Name")
        Fund_Code=request.form.get("Fund_Code")
        Invested_Amount=request.form.get("Invested_Amount")
        Unit_Held=request.form.get("Unit_Held")

        dict1=list1[int(id)-1]
        dict1.update({"Name":Name})
        dict1.update({"Fund_Code":Fund_Code})
        dict1.update({"Invested_Amount":Invested_Amount})
        dict1.update({"Unit_Held":Unit_Held})

        return redirect(url_for("func1"))
    f1=list1[int(id)-1]
    return render_template("edit.html",f1=f1)

@app.route('/delete/<string:id>',methods=["POST","GET"])
def delete(id):
    list1.pop(int(id)-1)
    return render_template("home.html",list2=list1)

if __name__=="__main__":
    app.run(debug=True)