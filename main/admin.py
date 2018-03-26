from django.contrib import admin

from main.models import *


class ScheduleInline(admin.TabularInline):
    model = Schedule


class PriceInline(admin.TabularInline):
    model = Price


class DocumentImageInline(admin.TabularInline):
    model = DocumentImage


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = 'short_name', 'name', 'short_title', 'bio',# 'schedule'
    list_editable = 'name', 'short_title', 'bio'

    inlines = [
        ScheduleInline,
    ]

    def schedule(self, instance):
        _schedule = instance.schedule()
        if not _schedule:
            return ''
        return '<br>'.join(map(str, _schedule))

    schedule.allow_tags = True


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):

    inlines = [
        PriceInline,
    ]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    inlines = [
        DocumentImageInline,
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = 'id', 'map', 'address', 'schedule', 'city_number', 'mobile_phone', 'email', 'ceo'
    list_editable = list_display[1:]
