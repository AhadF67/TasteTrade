from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.shortcuts import render

def main_home(request: HttpRequest):
    context = {'home_type': 'main'}
    return render(request, 'main/main_home.html', context)

def home(request: HttpRequest):
    # Ensure the user is authenticated
    if request.user.is_authenticated:
        user_type = request.user.profile.user_type
    else:
        user_type = None
    
    context = {'user_type': user_type}
    return render(request, 'main/home.html', context)

from django.shortcuts import render

def meet_the_team(request):
    # You might want to fetch team members from the database, but for now, we'll use static data
    team_members = [
        {
            'name': 'Bushra Alnakhli',
            'role': 'Developer',
            'linkedin': 'https://www.linkedin.com/in/boshra-ali/',
            'profile_picture': 'main\images\profile.jpg', 
        },
        {
            'name': 'Ghofran Al Sanosi',
            'role': 'Designer',
            'linkedin': 'https://www.linkedin.com/in/ghofran-al-sanosi',
            'profile_picture': 'main\images\profile.jpg',  
        },
        {
            'name': 'Ahad Alotaibi',
            'role': 'Project Manager',
            'linkedin': 'https://www.linkedin.com/in/ahad-2lotaibi',
            'profile_picture': 'main\images\profile.jpg', 
        },
        {
            'name': 'Noor Alresaini',
            'role': 'Quality Assurance',
            'linkedin': 'https://www.linkedin.com/in/noor-alresaini-300061227',
            'profile_picture': 'main\images\profile.jpg', 
        },
    ]
    
    return render(request, 'main/meet_the_team.html', {'team_members': team_members})
