from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import loginform
from .forms import signupform
from .forms import questionform
from .forms import answerform
from .models import loginfiles
from .models import questionfiles
from .models import answerfiles
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator

@csrf_exempt
def login(request):
	data = loginfiles.objects.all() 
	if request.method == 'POST':
		entry = loginform(request.POST)
		if entry.is_valid():
			email = entry.cleaned_data['email']
			password = entry.cleaned_data['password']
			if not loginfiles.objects.filter(email=email).exists():
				messages.add_message(request,messages.ERROR,'Emailid is not Registered Please Signup')
				return redirect('/signup')
			else:
				selectfield = loginfiles.objects.get(email=email)
				if password == selectfield.password:
					messages.add_message(request,messages.SUCCESS,'Successfully logged In')
					return redirect('/dashboard')
				else:
					messages.add_message(request,messages.ERROR,'Password didn\'t match with your Emailid')
					return redirect('/login')	    	
	else:
		session = loginform()
		return render(request,'login.html',{"form":session})
@csrf_exempt
def signup(request):
	if request.method == 'POST':
		data = signupform(request.POST)
		if data.is_valid():
			name = data.cleaned_data['name']
			email = data.cleaned_data['email']
			phone = data.cleaned_data['phone']
			password = data.cleaned_data['password']
			data = loginfiles(name=name, email=email, phone=phone, password=password)
			data.save()

			messages.add_message(request,messages.SUCCESS,"Successfully Registered")
			return redirect('/dashboard')
		else:
			messages.add_message(request,messages.ERROR,"Something went wrong please enter valid data")
			return redirect('/signup')
	else:
		data = signupform()
		return render(request,'signup.html',{'form' : data})
@csrf_exempt
def dashboard(request):
	if request.method == 'POST':
		userquestion = questionform(request.POST)
		if userquestion.is_valid():		
			question = userquestion.cleaned_data['question']		
			userquestion = questionfiles(question=question)
			userquestion.save()

			messages.add_message(request,messages.SUCCESS,"Successfully Uploaded your question")
			return redirect('/listaction')
		else:
			messages.add_message(request,messages.ERROR,"error")
			return redirect('/dashboard')
		
	else:
		userquestion = questionform()
		return render(request,'home.html',{'form' : userquestion})
@csrf_exempt
def listaction(request):
	if request.method == 'POST':
		useranswer = answerform(request.POST)
		if useranswer.is_valid():
			idform_id = useranswer.cleaned_data['idform_id']
			answer = useranswer.cleaned_data['answer']
			useranswer = answerfiles(answer=answer,idform_id=idform_id)
			useranswer.save()

			messages.add_message(request,messages.SUCCESS,"Successfully Uploaded your answer")
			return redirect('/listaction')
		else:
			messages.add_message(request,messages.ERROR,"error")
			return redirect('/listaction')
	else:
	    qnstasks = questionfiles.objects.all()
	    paginator1 = Paginator(qnstasks, 1)
	    anstasks = answerfiles.objects.all()
	    paginator2 = Paginator(anstasks, 1)
	    ansform = answerform()
	    page = request.GET.get('page')
	    tasks1 = paginator1.get_page(page)
	    tasks2 = paginator2.get_page(page)  
	    
	    task = {"tasks1":tasks1,"tasks2":tasks2,"ansform":ansform}		     
	    return render(request, 'list.html',task)

