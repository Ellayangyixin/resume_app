from django.contrib import admin
from .models import (
    UserProfile,
    JobExperience,
)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'wechat_username', 'phone_number')


class JobExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'title',
                    'start_date', 'end_date',
                    'isCurrent', 'description')


admin.site.register(JobExperience, JobExperienceAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
