from django.shortcuts import render

# Create your views here.
import account.views

import myapp.forms


class SignupView(account.views.SignupView):

   form_class = myapp.forms.SignupForm

   def after_signup(self, form):
       self.create_profile(form)
       super(SignupView, self).after_signup(form)

   def create_profile(self, form):
       profile = self.created_user.userprofile  # replace with your reverse one-to-one profile attribute
       profile.birthdate = form.cleaned_data["birthdate"]

       profile.save()


# 2
def about(request):
    return render(request, "about.html", {})


# 3
def dash(request):
    return render(request, "dash.html", {})