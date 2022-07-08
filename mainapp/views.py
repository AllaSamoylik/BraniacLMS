from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from mainapp.models import *


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'adds': 'территория Петропавловская крепость, 3Ж',
            }, {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'adds': 'территория Кремль, 11, Казань, Республика Татарстан, Россия',
            }, {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'adds': 'Красная площадь, 7, Москва, Россия',
            },
        ]
        return context


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context['objects'] = Course.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = 'mainapp/courses_detail.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context['course_object'] = get_object_or_404(Course, pk=pk)
        context['lessons'] = Lesson.objects.filter(course=context['course_object'])
        context['teachers'] = CoursesTeacher.objects.filter(courses=context['course_object'])
        return context


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = News.objects.all()[:5]
        return context


class NewsDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context['news_object'] = get_object_or_404(News, pk=pk)
        return context


class NewsWithPaginatorView(NewsView):

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context





