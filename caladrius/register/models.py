
#------------------------------------------------------------------------------------------


from django.utils import timezone
from django.db import models

# Create your models here.


from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# 
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, phone, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
                    email = self.normalize_email(email),
                    first_name = first_name,
                    last_name = last_name,
                    phone = phone,
                    **extra_fields
                    )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, first_name, last_name, phone, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', False)
        return self._create_user( email, password, first_name, last_name,phone, **extra_fields)
    
    def create_superuser(self, email, password, first_name, last_name, phone,  **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        return self._create_user(email, password, first_name, last_name, phone,  **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
                            db_index=True,
                            unique=True,
                            max_length=100,
                            help_text='Required. Inform a valid email address.',
                            )
    first_name = models.CharField(max_length=30)                                
    last_name = models.CharField(max_length=200)                        
    phone = models.CharField(max_length=12)
    date_joined = models.DateTimeField(default=timezone.now)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    
    def __str__(self):
        return self.email
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True