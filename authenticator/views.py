from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .forms import Resgister
from .models import Registered_logs

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = Resgister(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            print(password)

            # checking if both password and confirm password are the same
            if password != confirm_password:
                form.add_error(
                    'confirm_password', "Password and Confirm Password do not match. Please make sure they match.")
                return render(request, 'signup.html', {'form': form})
            else:
                first_name = form.cleaned_data['first_name']
                middle_name = form.cleaned_data['middle_name']
                last_name = form.cleaned_data['last_name']
                gender = form.cleaned_data['gender']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                contact = form.cleaned_data['contact']
                country = form.cleaned_data['country']
                zipcode = form.cleaned_data['zipcode']

                # Create an instance of the model using the cleaned data
                registered_log = Registered_logs(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    gender=gender,
                    email=email,
                    password=password,
                    contact=contact,
                    country=country,
                    zipcode=zipcode
                )

                # storing into database
                registered_log.save()
                return redirect('signin')

    else:
        form = Resgister()

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

           # print(email)

        try:
            user = Registered_logs.objects.get(email=email)
            
        except Registered_logs.DoesNotExist:
            # if the user with the entered email does not exist
            return render(request, 'signin.html', {'error': 'Invalid credentials'})

        # Comparing the entered password with the stored password
        if check_password(password, user.password):
        # if passwords matches, user is authenticated
            return redirect('index')
        else:
        # if passwords do not match, user not authenticated
            return render(request, 'signin.html', {'error': 'Invalid credentials'})

    return render(request, 'signin.html')


def forget_password(request):
    return render(request, 'forget_password.html')


def index(request):
    return render(request, 'index.html')
