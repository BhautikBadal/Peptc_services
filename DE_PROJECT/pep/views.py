from django.shortcuts import render , redirect ,HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import service_reg , reg_service_provider
import smtplib

# Create your views here.

def homepage(request):
        data = service_reg.objects.all()
        admin_data = reg_service_provider.objects.all()
        return render(request, 'index.html' , {'data':data , 'admin_data':admin_data})

def login(request):

    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        data = service_reg.objects.all()
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Your username and password not match!!!')
            return render(request, 'login.html')

    else:
        return render(request,'login.html')



def reg_customer(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['cus_email']
        username = request.POST['cus_user_name']
        password = request.POST['cus_password']
        repassword = request.POST['cus_repassword']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Your Enter User name is already  taken!!!")
                return render(request, 'reg_customer.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'You Enter E-mail is already taken!!')
                return render(request, 'reg_customer.html')
            else:
                myuser = User.objects.create_user(username=username , first_name=first_name , last_name=last_name , password=password , email=email)
                myuser.save()
                print('created!!!')
                return render(request,'login.html')
        else:
            messages.info(request,'Your Enter password and confirm password is invalid!!!')
            return render(request,'reg_customer.html')

    else:
        return render(request,'reg_customer.html')


# def reg_serviceprovider(request):
#
#     if request.method == 'POST':
#
#         myuser = reg_service_provider()
#
#         myuser.first_name = request.POST['first_name']
#         myuser.last_name = request.POST['last_name']
#         myuser.email = request.POST['ser_email']
#         myuser.user_name = request.POST['user_name']
#         myuser.password = request.POST['password']
#         myuser.address = request.POST['address']
#         myuser.phone_number = request.POST['phone']
#         repassword = request.POST['sp_repassword']
#
#         if myuser.password != repassword:
#             messages.info(request, 'Please Enter valid password !!')
#             return render(request, 'reg_service_provider.html')
#         elif len(myuser.phone_number)!=10:
#            messages.info(request,'Please Enter valid Phone number !!')
#            return render(request,'reg_service_provider.html')
#         else:
#             myuser.save()
#             return render(request,'login.html')
#     else:
#         return render(request,'reg_service_provider.html')


def serviceRegistration(requst):

    if requst.method == 'POST':

        myuser = service_reg()

        myuser.ser_user_name = requst.POST['user_name']
        myuser.user_name = requst.POST['first_name']
        myuser.service_name = requst.POST['service_name']
        myuser.date = requst.POST['date']
        myuser.time = requst.POST['time']
        myuser.email = requst.POST['email']
        myuser.phone_number = requst.POST['phone']
        myuser.address = requst.POST['address']

        if len(myuser.user_name)>30:
            messages.info(requst,'Please Enter valid user name it is to long')
            return render(requst,'serviceRegistration.html')
        elif len(myuser.phone_number)!=10:
           messages.info(requst,'Please Enter valid Phone number !!')
           return render(requst,'serviceRegistration.html')
        else:
            myuser.save()
            return redirect('homepage')

    else:
        return render(requst,'serviceRegistration.html')


def logout(request):

    auth.logout(request)

    return render(request,'index.html')

def email(request):

    if request.method == 'POST':


        email1 = request.POST['email']
        user_name = request.POST['user_name']
        phone_no = request.POST['phone']
        address = request.POST['address']
        service_name = request.POST['service_name']

        # to = email1
        content = '''----Welcome to peptc --- 
                    Your service reg. request approve succesfully.
                    Check Your service detail given below :--
                    ''' \
                  + f'service name : {service_name} ' \
                          f'phone : {phone_no}' \
                          f'\taddress : {address}' + '''
                          --written By--
                            Bhautik Badal
                          '''
        print(content)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('2018itbha002@ldce.ac.in', 'bhautikmeet@2001')
        server.sendmail('2018itbha002@ldce.ac.in', email1,content)
        server.close()

        messages.info(request,'Email sent successfully')

        return redirect('/')

    else:
        return HttpResponse('email sent')

def Delete(request , id):

    service = service_reg.objects.get(s_id=id)
    service.delete()
    messages.info(request,'Request denied successfull')
    return redirect('/')