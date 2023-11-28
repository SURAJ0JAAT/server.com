from django.shortcuts import get_object_or_404, render
from .models import job

# Create your views here.
def home(request):
    return new_func(request)

def new_func(request):
    jobs = job.objects
    return render(request,'jobs/home.html', {'jobs':jobs})
#def start(s):
#    return render(s, 'jobs/start.html')

def detail(request, job_id):
    job_detail = get_object_or_404(job, pk=job_id) 
    return render(request, 'jobs/detail.html',{'job':job_detail})
