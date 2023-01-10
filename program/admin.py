from django.contrib import admin
from .models import Program, PassCode, ProgramResource
# Register your models here.


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'google_form_check')


admin.site.register(PassCode)

@admin.register(ProgramResource)
class ProgramResourceAdmin(admin.ModelAdmin):
    list_display = ("file_title", "program")
    list_filter = ("program",)



