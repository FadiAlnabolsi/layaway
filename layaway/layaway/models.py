from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True, blank=True)