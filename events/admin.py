from django.contrib import admin
from django.contrib.admin import ModelAdmin
from events.models import Cultural_Events, Sports_Events, Technical_Events, UserManager, User, Event_Registrations, Payment, Accommodation


def mark_paid(ModelAdmin, request, queryset):
    queryset.update(paid=True)

mark_paid.short_description = "Mark selected as paid"

def mark_unpaid(ModelAdmin, request, queryset):
    queryset.update(paid=False)

mark_unpaid.short_description = "Mark selected as Unpaid"

def activate(ModelAdmin, request, queryset):
    queryset.update(active=True)

activate.short_description = "Mark User Active"


def deactivate(ModelAdmin, request, queryset):
    queryset.update(active=False)

deactivate.short_description = "Mark User Inactive"


class Event_RegistrationsAdmin(admin.ModelAdmin):
    list_display = ("event_name", "users_name", "college", "paid")
    actions = (mark_paid, mark_unpaid)
    search_fields = ("event_name", "user_id", "paid")
    list_filter = ("paid",)

class Cultural_EventsAdmin(admin.ModelAdmin):
    list_display = ("name", "club", "fees_snu", "fees_amount", "prize_money", "team_size_min", "team_size_max")
    search_fields = ("name", "club",)
    list_filter = ("club",)
    
class Technical_EventsAdmin(admin.ModelAdmin):
    list_display = ("name", "club", "fees_snu", "fees_amount", "prize_money", "team_size_min", "team_size_max")
    search_fields = ("name", "club",)
    list_filter = ("club",)
    
class Sports_EventsAdmin(admin.ModelAdmin):
    list_display = ("name", "fees_amount", "prize_money", "team_size_min", "team_size_max")
    search_fields = ("name", )
    
class UsersAdmin(admin.ModelAdmin):
    list_display = ("full_name", "id", "email", "college", "mobile_num")
    search_fields = ("first_name", "last_name", "id", "email", "college", "mobile_num")
    list_filter = ("college", "staff", "admin", "active")
    actions = (activate, deactivate)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("events", "name", "college", "partial", "amount", "paid")
    search_fields = ("events", "name")

class AccomodationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "type", "include_food", "number_of_people", "start_date", "amount")
    search_fields = ("name", "college", "number_of_people")
    list_filter = ("start_date", "number_of_people", "include_food")

# Register your models here.
admin.site.register(Cultural_Events, Cultural_EventsAdmin)
admin.site.register(Sports_Events, Sports_EventsAdmin)
admin.site.register(Technical_Events, Technical_EventsAdmin)
admin.site.register(User, UsersAdmin)
admin.site.register(Event_Registrations, Event_RegistrationsAdmin)
#admin.site.register(Event_Registrations)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Accommodation, AccomodationAdmin)


