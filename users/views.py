from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
@csrf_exempt
def register(request):
    """Resitration page for new user"""
    if request.method != 'POST':
        #display blank form
        form = UserCreationForm()
    else:
        #process the whole form
        form = UserCreationForm(data =request.POST)

        if form.is_valid():
            new_user = form.save()
            #log the user in and redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form':form}
    return render(request,'registration/register.html',context)
