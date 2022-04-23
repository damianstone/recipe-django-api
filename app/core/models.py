from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    # extra to accept any other extra thing
    # create new user model
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        #normalize to make the email lowercase
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)

        # jsut good practice
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# custom user models that support using emails instead of username
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # to determine is the user is active or not
    is_active = models.BooleanField(default=True)
    #not staff
    is_staff = models.BooleanField(default=False)

    # create the user
    objects = UserManager()

    USERNAME_FIELD = 'email'
