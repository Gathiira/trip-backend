from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Member

User = get_user_model()


admin.site.register(Member)


# Register your models here.
# admin.site.unregister(User)
# admin.site.unregister(Group)
# admin.site.unregister(Site)