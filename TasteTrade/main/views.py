from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.core.mail import send_mail
from django.conf import settings

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

def about_us(request):
    return render(request, 'main/about_us.html')

def our_services(request):
    return render(request, 'main/our_services.html')


def our_story(request):
    return render(request, 'main/our_story.html')

def sustainability(request):
    return render(request, 'main/sustainability.html')

def careers(request):
    return render(request, 'main/careers.html')

def faqs(request):
    return render(request, 'main/faqs.html')

def shipping_returns(request):
    return render(request, 'main/shipping_returns.html')

def terms_of_service(request):
    return render(request, 'main/terms_of_service.html')

def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')

def submit_application(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        cover_letter = request.POST.get('cover_letter')

        # Example of processing the application (e.g., sending an email)
        send_mail(
            'New Job Application',
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\nPosition: {position}\nCover Letter:\n{cover_letter}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.RECEIVE_APPLICATIONS_EMAIL],
            fail_silently=False,
        )

        return redirect('success')  # Redirect to a success page or another page

    return render(request, 'careers.html')

def pricing(request):
    return render(request, 'main/pricing.html')