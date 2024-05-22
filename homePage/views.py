# from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import contact
# Create your views here.
def homepage(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Subject=request.POST['Subject']
        Massage=request.POST['Massage']

        new_contact=contact(Name=Name,Email=Email,Subject=Subject,Massage=Massage)
        new_contact.save()
        
    
    
    
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
