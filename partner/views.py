from django.shortcuts import render
from django import forms
from partner.models import *
from django.core import mail
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _


class MailForm(forms.ModelForm):
    color = {}
    def clean(self):
        if self.cleaned_data.get('sender'):
            self.color['sender'] = 'has-success'
        else:
            self.color['sender'] = 'has-error'

        if self.cleaned_data.get('email'):
            self.color['email'] = 'has-success'
        else:
            self.color['email'] = 'has-error'

        if self.cleaned_data.get('subject'):
            self.color['subject'] = 'has-success'
        else:
            self.color['subject'] = 'has-error'

        if self.cleaned_data.get('message'):
            self.color['message'] = 'has-success'
        else:
            self.color['message'] = 'has-error'


    class Meta:
        model = Mail
        fields = ['sender', 'email', 'subject', 'message']
        localized_fields = ('__all__',)
        widgets = {
            'sender': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'type': 'text',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ваш Email',
                'type': 'email',
                'class': 'form-control',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Введите тему',
                'type': 'text',
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Введите сообщение',
                'type':'text',
                'class': 'form-control',
                'rows': 5,
            }),
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)
    search.widget = forms.TextInput(attrs={'placeholder': 'Поиск...', 'class': 'form-control',})


def index(request):
    data = {
        'carousel_images': CarouselImage.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.all()[0],
    }
    return render(request, 'partner/index.html', data)


def equipment(request):
    data = {
        'equipments': Equipment.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.all()[0],
        'form': SearchForm(),
    }
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_str = form.cleaned_data['search']
            data['equipments'] = Equipment.objects.filter(name__contains=search_str)
            data['form'] = form
    return render(request, 'partner/equipment.html', data)


def features(request):
    data = {
        'features': Feature.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.all()[0],
    }
    return render(request, 'partner/features.html', data)


def pricing(request):
    data = {
        'equipment_prices': EquipmentPrice.objects.all(),
        'monitoring_prices': MonitoringPrice.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.all()[0],
    }
    return render(request, 'partner/pricing.html', data)


def services(request):
    data = {
        'services': Service.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.all()[0],
    }
    return render(request, 'partner/services.html', data)


def company(request):
    data = {
        'partners': Partner.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.all()[0],
        'about_company': Blog.objects.get(mark="about_company"),
    }
    return render(request, 'partner/company.html', data)


def workers(request):
    data = {
        'workers': Worker.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.all()[0],
    }
    return render(request, 'partner/workers.html', data)


def contacts(request):
    # office = Office.objects.all()[0]
    office_mail = office.email
    server_mail = 'ooo.service-partner@yandex.ru'
    data = {
        'office': office,
        'widgets': SocialWidget.objects.all(),
        'form': MailForm(),
        'thank': False,
        'color': {},
    }
    if request.method == 'POST':
        form = MailForm(request.POST)
        form.full_clean()
        data['color'] = form.color
        if form.is_valid():
            sender = form.cleaned_data['sender']
            email = form.cleaned_data['email']
            subj = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            s = ":".join([sender, email, subj])
            mail.send_mail(s, message, server_mail, [office_mail], fail_silently=False)
            data['form'] = form
            data['thank'] = True
            form.save()
        else:
            data['form'] = form
    return render(request, 'partner/contacts.html', data)