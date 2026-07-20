from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import PersonalInfoForm
from .models import PersonalInfo

# Create your views here.

@login_required
def personal_info(request):
    
    profile = PersonalInfo.objects.filter(user=request.user).first()
    
    # print("Logged in user:", request.user) #Debug
    # print("Profile:", profile)
     
    if request.method == "POST":
        form = PersonalInfoForm(request.POST, instance=profile)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = PersonalInfoForm(instance=profile)
    return render(request, 'users/personal_info.html', {'form':form})

@login_required
def delete_profile(request):
    profile = get_object_or_404(PersonalInfo, user=request.user)
    user = request.user
    if request.method == "POST":
        profile.delete()
        user.delete()
        
        return redirect('signup')
    return render(request, 'users/profile_delete.html', {'profile':profile})
            