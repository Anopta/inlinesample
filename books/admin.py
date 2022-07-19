from django.contrib import admin
from .models import *


class EditionInline(admin.StackedInline):
        model = Edition
        extra = 0

class TestimonialInline(admin.StackedInline):
        model = Testimonial
        extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [EditionInline, TestimonialInline ]




