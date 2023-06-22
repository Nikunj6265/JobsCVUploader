from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.template import loader
# Create your views here.

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        template = loader.get_template('myapp/home.html')
        context = {'candidates':candidates, 'form':form}
        return HttpResponse(template.render(context, request))
        #return render(request,'myapp/home.html',{'candidates':candidates, 'form':form})
    
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          template = loader.get_template('myapp/home.html')
          context = {'form':form}
          return HttpResponse(template.render(context, request))
          #return render(request,'myapp/home.html',{'form':form})
        
class CandidatesView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        template = loader.get_template('myapp/candidate.html')
        context = {'candidate':candidate}
        return HttpResponse(template.render(context, request))
        #return render(request, 'myapp/candidate.html',{'candidate':candidate})        