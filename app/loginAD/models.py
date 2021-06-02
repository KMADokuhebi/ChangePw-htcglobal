from django.db import models
from django.contrib import admin
# Create your models here.


class UserAD(models.Model):
    usernameAD = models.CharField(max_length=20)
    tokenAD = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'{self.usernameAD} {self.pwAD}'
        return self.usernameAD


class passwAD(models.Model):
    pwAD = models.CharField(max_length=20)
    tokenAD = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pwAD

class total(models.Model):
    usernameAD = models.CharField(max_length=20)
    totals = models.IntegerField( null=True)
    date = models.DateTimeField(auto_now_add=True)
    # # return totals
    # def __str__(self):
    # #     # return f'{self.usernameAD} {self.pwAD}'
    #     return self.totals
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','usernameAD','totals','date')
class HomeAdmin2(admin.ModelAdmin):
    list_display = ('id','pwAD','tokenAD','date')
class HomeAdmin3(admin.ModelAdmin):
    list_display = ('id','usernameAD','tokenAD','date')
admin.site.register(total,HomeAdmin)
admin.site.register(passwAD,HomeAdmin2)
admin.site.register(UserAD,HomeAdmin3)
