from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, mobile='', login_status=False, created_date=None, address=''):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            mobile=mobile,
            login_status=login_status,
            created_date=created_date,
            address=address,
            requested = 0,
            donated = 0
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True)
    login_status = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    address = models.TextField(blank=True)
    requested = models.IntegerField(default=0,blank=True)  # Added requested field with default value 0
    donated = models.IntegerField(default=0,blank=True)
    password = models.CharField(max_length =15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True, verbose_name='groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', blank=True, verbose_name='user permissions')

    def __str__(self):
        return self.username

class Donate_food(models.Model):
    donator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='food_donations_made')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='food_donations_received',blank=True,null=True)
    description = models.TextField()
    food_quantity = models.IntegerField()
    type_of_food = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = True, blank=True)
    address = models.TextField()

class Donate_Grocery(models.Model):
    donator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='grocery_donations_made')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='grocery_donations_received',blank=True,null=True)
    description = models.TextField()
    grocery_quantity = models.IntegerField()
    type_of_grocery = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = True, blank=True)
    address = models.TextField()

class Request(models.Model):
    requestor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requests_made')
    helper = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requests_helped',blank=True,null=True)
    description = models.TextField()
    help = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = True, blank=True)
    address = models.TextField()

