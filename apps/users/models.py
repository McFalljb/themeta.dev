import hashlib
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from PIL import Image
from tinymce import HTMLField

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text
from allauth.account.signals import user_signed_up


class MyUserManager(UserManager):
    """
    Custom User Model manager.

    It overrides default User Model manager's create_user() and create_superuser,
    which requires display_name field.
    """

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=False, unique=True)
    first_name = models.CharField(_('first name'), max_length=40, blank=False, null=True, unique=False)
    last_name = models.CharField(_('last name'), max_length=40, blank=True, null=True, unique=False)
    display_name = models.CharField(_('display_name'), max_length=14, blank=True, null=True, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    dob = models.CharField(verbose_name="dob", blank=True, null=True, max_length=8)
    objects = MyUserManager()

    #Set variables in profile to private.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'auth_user'
        abstract = False

    # def get_full_name(self):
    #     """
    #     Returns the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    def guess_display_name(self):
        """Set a display name, if one isn't already set."""
        if self.display_name:
            return

        if self.first_name and self.last_name:
            dn = "%s %s" % (self.first_name, self.last_name[0])  # like "Andrew E"
        elif self.first_name:
            dn = self.first_name
        else:
            dn = 'You'
        self.display_name = dn.strip()

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def __str__(self):
        return self.email

    # def natural_key(self):
    #     return (self.email,)
    

class UserProfile(models.Model):

    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    bio = HTMLField(default='Describe your self and what you are working on!')
    email_private = models.BooleanField(_('email private'), default=False)
    first_name_private = models.BooleanField(_('first name private'), default=True)
    last_name_private = models.BooleanField(_('last name private'), default=True)
    
    
    def __str__(self):
        return self.user.display_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 80 or img.width > 80:
            output_size = (80, 80)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    class Meta():
        verbose_name = _('user_profile')
        verbose_name_plural = _('user_profiles')
        db_table = 'user_profile'


@receiver(user_signed_up)
def set_initial_user_names(request, user, sociallogin=None, **kwargs):

    profile = UserProfile(user=user)

    if sociallogin:
        # Extract first / last names from social nets and store on User record


        if sociallogin.account.provider == 'facebook':
            user.first_name = sociallogin.account.extra_data['first_name']
            user.last_name = sociallogin.account.extra_data['last_name']
            # verified = sociallogin.account.extra_data['verified']
            #picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
            #    sociallogin.account.uid, preferred_avatar_size_pixels)

        if sociallogin.account.provider == 'google':
            user.first_name = sociallogin.account.extra_data['given_name']
            user.last_name = sociallogin.account.extra_data['family_name']
            # verified = sociallogin.account.extra_data['verified_email']
            #picture_url = sociallogin.account.extra_data['picture']

    def guess_display_name(self):
        """Set a display name, if one isn't already set."""
        if self.username:
            user.display_name = self.username
            return

    profile = UserProfile(user=user)
    profile.save()
    user.guess_display_name()
    user.save()