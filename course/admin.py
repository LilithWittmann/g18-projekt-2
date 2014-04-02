from django.contrib import admin
from .models import Course, Module
from .forms import *


class CourseModelAdmin(admin.ModelAdmin):
    form = CourseForm


class ModuleModelAdmin(admin.ModelAdmin):
    form = ModuleForm


admin.site.register(Course, CourseModelAdmin)
admin.site.register(Module, ModuleModelAdmin)
