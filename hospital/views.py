from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from .models import *

# Create your views here.
def About(request):
	return render(request,'about.html')

def Contact(request):
	return render(request,'contact.html')

def Index(request):
	if not request.user.is_staff:
		return redirect('login')
	return render(request,'index.html')

def Login(request):
	error=""
	if request.method =='POST':
		Uname = request.POST['uname']
		Pwd = request.POST['pwd']
		user = authenticate(username=Uname, password=Pwd)

		try:
			if user.is_staff:
				login(request, user)
				error="no"
			else:
				error = "yes"

		except:
			error="yes"

	d={'error': error}	
	return render(request,'login.html',d)


def Logout_admin(request):
	if not request.user.is_staff:
		return redirect('login')
	logout(request)
	return redirect('login')


def View_doctor(request):
	if not request.user.is_staff:
		return redirect('login')
	doc = Doctor.objects.all()
	d= {'doc': doc}
	return render(request, 'view_doctor.html',d)


def Add_doctor(request):
	error=""
	if not request.user.is_staff:
		return redirect('login')
	if request.method =='POST':
		Name = request.POST['name']
		Contact = request.POST['contact']
		Sp= request.POST['speciality']

		try:
			Doctor.objects.create(name=Name,mobile=Contact,Speciality=Sp)
			error="no"

		except:
			error="yes"

	d={'error': error}	
	return render(request,'add_doctor.html',d)


def Delete_doctor(request, pid):
	if not request.user.is_staff:
		return redirect('login')
	doctor = Doctor.objects.get(id=pid)
	doctor.delete()

	return redirect('view_doctor')


def Add_patient(request):
	error=""
	if not request.user.is_staff:
		return redirect('login')
	if request.method =='POST':
		Name = request.POST['name']
		Gender = request.POST['gender']
		Contact = request.POST['mobile']
		Address= request.POST['address']

		try:
			Patient.objects.create(name=Name,gender=Gender,mobile=Contact,address=Address)
			error="no"

		except:
			error="yes"

	d={'error': error}	
	return render(request,'add_patient.html',d)


def View_patient(request):
	if not request.user.is_staff:
		return redirect('login')
	pat = Patient.objects.all()
	d= {'pat': pat}
	return render(request, 'view_patient.html',d)	


def Delete_patient(request, pid):
	if not request.user.is_staff:
		return redirect('login')
	patient = Patient.objects.get(id=pid)
	patient.delete()

	return redirect('view_patient')	

def Add_appointment(request):
	error=""
	if not request.user.is_staff:
		return redirect('login')

	doctor1= Doctor.objects.all()
	patient1=Patient.objects.all()	

	if request.method =='POST':
		D = request.POST['doctor']
		P = request.POST['patient']
		d1 = request.POST['date']
		t1= request.POST['time']

		doctor = Doctor.objects.filter(name=D).first()
		patient = Patient.objects.filter(name=P).first()

		try:
			Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t1)
			error="no"

		except:
			error="yes"

	d={'doctor': doctor1, 'patient': patient1, 'error': error}	
	return render(request,'add_appointment.html',d)


def View_appointment(request):
	if not request.user.is_staff:
		return redirect('login')
	app = Appointment.objects.all()
	d={'app': app}
	return render(request,'view_appointment.html',d)	


def Delete_appointment(request, pid):
	if not request.user.is_staff:
		return redirect('login')
	appointment = Appointment.objects.get(id=pid)
	appointment.delete()

	return redirect('view_appointment')	