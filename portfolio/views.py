from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

from blog.models import Blog
from projects.models import Project

import math

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            subject = 'New Message from ' + name
            message = request.POST.get('message')
            from_email = request.POST.get('email')
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['cmjacqu@gmail.com'])
                except BadHeaderError:
                    pass
                return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm()

        b = Blog.objects.order_by('pub_date')[:4]

        p = Project.objects.order_by('created_date')

        num_projects = list(range(0,len(p),1))

        # def splitProjects(p):
        #     s = math.floor(len(p)/2)
        #     p1 = p[0:s]
        #     p2 = p[s:len(p)]
        #     return p1, p2

        return render(request, 'index.html', {'form': form, 'blogs': b, 'projects': p, 'num_projects': num_projects})

def thanks(request):
    return render(request, 'thanks.html')
# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     success_url = '/success/'
#
#     def form_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)
