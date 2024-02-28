from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Gallery,Attendance,Data

# Create your views here.
def Home(request):
    return render(request,"index.html")
def award(request):
    return render(request,"award.html")
def about(request):
    return render(request,"about.html")


def data(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')    
    user_phone=request.user
    posts=Enrollment.objects.filter(Phonenumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)

    print(posts)
    context={"posts":posts,"attendance":attendance}
    

    return render(request,"data.html")    

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
        
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}     
    

    if request.method=="POST":
       phonenumber=request.POST.get('Phonenumber')
       Login=request.POST.get('logintime')
       Logout=request.POST.get('logouttime')
       SelectWorkout=request.POST.get('workout')
       TrainedBy=request.POST.get('trainer')

       query=Attendance(phonenumber=phonenumber,Login=login,Logout=logout,
       SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
       query.save()
       messages.warning(request,"Attendance Marked Successfully")
       return redirect('/attendance')

    return render(request,"attendance.html",context)    
def gallery(request):
    post=Gallery.objects.all()
    context={"posts":post}
    return render(request,"gallery.html",context)


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')    
    user_phone=request.user
    posts=Enrollment.objects.filter(Phonenumber=user_phone)
    print(posts)
    context={"posts":posts}
    return render(request,"profile.html",context)


def signup(request):
    if request.method=="POST":
        username=request.POST.get ('usernumber')  
        email=request.POST.get ('email')
        pass1=request.POST.get ('pass1')
        pass2=request.POST.get ('pass2')
       

        if len( username)>10 or len(username)<10:
            messages.info(request,"Phone Number must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
            
        try:    
            if User.objects.get(username=username):
               messages.warning(request,"Phone Number Already is Taken")
               return redirect('/signup') 
        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
               messages.warning(request,"Email is Already Taken")
               return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1) 
        myuser.save()
        messages.success(request,"User Created Successfully Please Login")
        return redirect('/login')
    return render(request,"signup.html")    


def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')  
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
       

        if myuser is not None: 
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
            
           
        else:
            messages.error(request,"Invalid Credentials") 
            return redirect('/login')
        

       
    return render(request,"handlelogin.html")

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Succesfully")
    return redirect('/login')    
def contact(request): 
    
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')  
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()

        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
    return render(request,"contact.html")                 
def entroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
        
    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}

    if request.method=="POST":
        fullName=request.POST.get('fullname')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        num=request.POST.get('num')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=fullName,Email=email,Gender=gender,Phonenumber=num,
        DOB=DOB, SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')

    return render(request,"entroll.html",context) 
           
