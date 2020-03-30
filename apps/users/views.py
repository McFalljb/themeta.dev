from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin, UpdateView
from django.shortcuts import render, redirect
from .forms import UserEditForm, ProfileUpdateForm


@login_required
def UserProfile(request):
    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('account_profile')
    
    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)

@login_required
def UserEditProfile(request):
    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('account_profile')
    
    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

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


# class UserEditViewa(UpdateView):
#     """Allow view and update of basic user data.

#     In practice this view edits a model, and that model is
#     the User object itself, specifically the names that
#     a user has.

#     The key to updating an existing model, as compared to creating
#     a model (i.e. adding a new row to a database) by using the
#     Django generic view ``UpdateView``, specifically the
#     ``get_object`` method.
#     """
#     form_class = UserEditForm
#     #template_name = "users/profile_edit.html"
#     #view_name = 'account_edit'
#     #success_url = reverse_lazy(view_name)

#     def get_object(self):
#         return self.request.user

#     def form_valid(self, form):
#         form.save()
#         messages.add_message(self.request, messages.INFO, 'User profile updated')
#         return super(UserEditView, self).form_valid(form)
#account_edit = login_required(UserEditView.as_view())
