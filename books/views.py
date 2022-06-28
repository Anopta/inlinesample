from django.views.generic import ListView
from extra_views import (
    CreateWithInlinesView,
    UpdateWithInlinesView,
    InlineFormSetFactory,
)
from . import models


class BookListView(ListView):
    model = models.Book

    def get_queryset(self):
        return super().get_queryset().prefetch_related("edition_set", "testimonial_set")


class EditionInline(InlineFormSetFactory):
    model = models.Edition
    fields = ["publisher", "year", "pages"]
    factory_kwargs = {"extra": 0}


class TestimonialInline(InlineFormSetFactory):
    model = models.Testimonial
    fields = ["name", "testimonial"]
    factory_kwargs = {"extra": 1}


class BetterMixin:
    def get_template_names(self):
        if self.request.GET.get("better"):
            return ["books/book_better_form.html"]
        return super().get_template_names()


class BookCreateView(BetterMixin, CreateWithInlinesView):
    model = models.Book
    inlines = [EditionInline, TestimonialInline]
    fields = ["title", "author"]

    def get_success_url(self):
        return "/"


class BookUpdateView(BetterMixin, UpdateWithInlinesView):
    model = models.Book
    inlines = [EditionInline, TestimonialInline]
    fields = ["title", "author"]

    def get_success_url(self):
        return "/"
