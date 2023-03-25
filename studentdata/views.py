from django.shortcuts import render,redirect,HttpResponse
import pymongo
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# https://www.pinterest.com/pin/826621706590317376/

@csrf_exempt
def users(request):
    pass

myclient=pymongo.MongoClient("mongodb://localhost:27017")
admin_db=myclient.adminDatabase
admin_col=admin_db.adminDetail

# myclient=pymongo.MongoClient("mongodb://localhost:27017")
# admin_db=myclient.adminDatabase
std_col=admin_db.StudentDetail

# Create your views here.
def home(req):
    # studentlist=mycol.find()
    if(req.method=="POST"):
        student_choice=req.POST.get("radio")
        print(student_choice,"cccccccccccccccccccccccccccccccc")
        if(student_choice!=None):
            
            return redirect("find_std", params=str(student_choice))
   
    return render(req,"home.html",{"isLogged":True})
def add_std(req):
    if(req.method=="POST"):
        Reg_no=req.POST.get("reg_no")
        name=req.POST.get("name")
        age=req.POST.get("age")
        DOB=req.POST.get("DOB")
        Mark=req.POST.get("mark")
        new_student={"std_ID":Reg_no,"name":name,"age":age,"DOB":DOB,"Mark":Mark}
        std_col.insert_one(new_student)
        print("data inserted")
        return redirect("home")

    return render(req,"add_std.html",{"isLogged":True})

def find_std(req,params):
    
    if(req.method=="POST"):
        if (params=="id"):
            params="std_ID"
        studentname=req.POST.get("detail")
        
        print(params,"ppppppppppppppppppppppppppppppp")
        print(studentname,"cccccccccccccccccccccccccccccccc")
        if(studentname!=None):
            global value
            # global data
            for data in std_col.find({params:studentname}): 
                # print(data)
                value=data  
                  
            return redirect("result")
           
        
    return render(req,"find_std.html",{"getName":params})
    

def signin(req):    
    if(req.method=="POST"):
        userName=req.POST.get("userName")
        password=req.POST.get("password")
        for eachUser in admin_col.find():
            print(eachUser["userName"]==userName,"uuuuuuuuuuuuuuuuuuuu")
            print(eachUser["password"]==password,"pppppppppppppppppppp")
            if (eachUser["userName"] == userName and eachUser["password"] == password):
                print("successfully login ssssssssssssssssss")
                req.session['userid']=userName
                return redirect("home")
        else:
            return redirect("signup")
            pass
    return render(req,"signin.html",{"isLogged":False})


def signup(req):
    if(req.method=="POST"):
        name=req.POST.get("name")
        age=req.POST.get("age")
        DOB=req.POST.get("DOB")
        userName=req.POST.get("userName")
        password=req.POST.get("password")
        admin={"name":name,"age":age,"DOB":DOB,"userName":userName,"password":password}
        admin_col.insert_one(admin)
        print("data inserted")
        return redirect("home")

    return render(req,"signup.html",{"isLogged":False})

def signout(req):
    if(req.session.get("userid")!=None):
        req.session.pop("userid")
    return redirect("signin")
    
def result(req):
    if(value==none):
        return redirect("find_std.html",{"value":value})
    else:
        return render(req,"result.html",{"value":value})
    # return render(req,"find_std.html")
# 
def edit(req,current_id):

    if(req.method=="POST"):
        global old_data
        for old_data in std_col.find({"std_ID":current_id}): 
            print(old_data)
        std_ID=current_id
        name=req.POST.get("name")
        age=req.POST.get("age")
        DOB=req.POST.get("DOB")
        Mark=req.POST.get("mark")
        new_data={"$set":{"name":name,"age":age,"DOB":DOB,"Mark":Mark}}

        
        std_col.update_one(old_data,new_data )
        print("data edited")
        return redirect("home")
    print(current_id,"cccccccccccccccccccccc")

    

    return render(req,"edit.html",{"value":value})

def delete(req,current_id):
    # std_col.get(id).remove()
    std_col.delete_one({"std_ID":current_id})
    value.clear()
    print("deleted ssssssssssssssssssss")

    return redirect ("home")