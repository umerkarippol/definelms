from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from lmsmainapp.models import *
from .models import *

@admin.register(designation)
class StudentAdmin(ImportExportModelAdmin):
    pass


@admin.register(exam)
class examAdmin(ImportExportModelAdmin):
    pass

@admin.register(course)
class examAdmin(ImportExportModelAdmin):
    pass


@admin.register(topic)
class topicadmin(ImportExportModelAdmin):
    pass
