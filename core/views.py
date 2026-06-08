from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Project, TeamMember,NewsPost
from django.views.generic import ListView, TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():

            messages.success(
                request,
                "Message sent successfully!"
            )

            return redirect('contact')

        return self.render_to_response({
            'form': form
        })

# SERVICES
class ITSolutionsView(TemplateView):
    template_name = "services/it_solutions.html"


class ElectricalEngineeringView(TemplateView):
    template_name = "services/electric.html"


class SecuritySystemsView(TemplateView):
    template_name = "services/security_systems.html"


class TelecommunicationsView(TemplateView):
    template_name = "services/telecommunications.html"


class MaintenanceView(TemplateView):
    template_name = "services/maintenance.html"


# COMPANY
class AboutView(TemplateView):
    template_name = "company/about.html"


class ProjectsView(ListView):
    model = Project
    template_name = "company/projects.html"
    context_object_name = "projects"


class TeamView(ListView):
    model =TeamMember
    template_name = "company/team.html"
    context_object_name = "team_members"


class CareersView(TemplateView):
    template_name = "company/careers.html"


class NewsView(ListView):
    model=NewsPost
    template_name = "company/news.html"
    context_object_name = "posts"


class ContactView(TemplateView):
    template_name = "company/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save() 

            messages.success(
                request,
                "Message sent successfully!"
            )

            return redirect('contact')

        return self.render_to_response({
            'form': form
        })