from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    fieldsets =[
        (None,{"fields":["name", "last_name"]}),
        (None, {"fields":["email"]}),
        (None, {"fields":["active_member"]})
    ]

    list_display = ("name", "last_name", "email", "active_member")
    list_filter = ["active_member"]
    search_fields = ["name", "last_name", "email", ]

admin.site.register(Member, MemberAdmin)
