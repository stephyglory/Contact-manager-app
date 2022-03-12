from django.http import HttpResponse
from django.shortcuts import redirect, render
from zoho.database import Database

email = ""
password = ""

def signin(request):
    if(request.method == "POST"):
        global email,password
        try:
            if(Database().signIn(request.POST["email"],request.POST["password"]) != False):
                email = request.POST["email"]
                password = request.POST["password"]
                return redirect("/contact")
            return render(request,"signinLog=.html",{"msg":"user not found"})
        except Exception as e:
            print(e)
            return render(request,"signinLog.html",{"msg":"invalid data"})
    return render(request,"signin.html")



def signup(request):
    if(request.method == "POST"):
        try:
            if(Database().signUp(request.POST["email"],request.POST["password"]) != False):
                return redirect("/")
            return render(request,"signupLog.html",{"msg":"user already found"})
        except:
            return render(request,"signupLog.html",{"msg":"invalid data"})
    return render(request,"signup.html")

def contact(request):
    if(Database().signIn(email,password) != False):
        if(request.method == "POST"):
            try:
                Database().saveContact(email,request.POST["name"],int(request.POST["phno"]),request.POST["email"])
                return redirect("/contact");
            except:
                return render(request,"contactLog.html",{"mes":"invalid data"})
        return render(request,"contact.html",{"data":Database().getContacts(email)})
    return redirect('/')


