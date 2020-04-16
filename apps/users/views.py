from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserEditForm, ProfileUpdateForm
from apps.blog.models import Post
from django.views.generic import ListView, DetailView
from .models import UserProfile, User



# def UserProfile(request, display_name):
    
#     context = {

#         'posts': Post.objects.all()
#     }

    
#     user = User.objects.get(display_name=display_name)
#     return render(request, 'users/profile.html', {"user":user})

#     #return render(request, 'users/profile.html', context)

def get_user_profile(request, display_name):
    user = User.objects.get(display_name=display_name)
    post = {'posts': Post.objects.all()}
    return render(request, 'users/profile.html', {"user":user, "post":post})

@login_required
def UserEditProfile(request):

    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        #pp_form = UserPrivateForm(request.POST)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #pp_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('user_profile')
    
    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        #pp_form = UserPrivateForm()
    
    context = {
        'u_form': u_form,
        'p_form': p_form,       
        #'pp_form' : pp_form,
    }
    # user = User.objects.get(display_name=display_name)
    # return render(request, 'users/profile_edit.html', {"user":user})

    return render(request, 'users/profile_edit.html', context)


class MyModelInstanceMixin(FormMixin):
    def get_model_instance(self):
        return None

    def get_form_kwargs(self):
        kwargs = super(MyModelInstanceMixin, self).get_form_kwargs()
        instance = self.get_model_instance()
        if instance:
            kwargs.update({'instance': instance})
        return instance
