from django.shortcuts import render, redirect
from users.forms import RegistrationForm

# Create your views here.
def register_user(request):
    # Create new instance of RegisterationForm.
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #commit=False means to pause the saving process
            user.set_password(user.password) #To hide the password field in the form
            user.save() #Save to db
            return redirect("home") #redirect to 'home' page
    context = {"form": form}
    return render(request, "register.html", context)

