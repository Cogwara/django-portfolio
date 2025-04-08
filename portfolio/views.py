from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from .models import PortfolioItem, Profile, Expertise, Experience, Education, Skill, Service, Project, BlogPost, ProjectCategory
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            profile = Profile.objects.first()
            context['profile'] = profile
            context['expertise'] = Expertise.objects.filter(profile=profile)
            context['services'] = Service.objects.filter(profile=profile)
            context['skills'] = Skill.objects.filter(profile=profile)
            context['experience'] = Experience.objects.filter(
                profile=profile).order_by('-start_date')
            context['education'] = Education.objects.filter(
                profile=profile).order_by('-start_date')
            context['projects'] = Project.objects.all().order_by('-date')[:6]
            context['blog_posts'] = BlogPost.objects.all().order_by(
                '-date_posted')[:3]

            category_slug = self.request.GET.get('category')
            if category_slug:
                category = get_object_or_404(
                    ProjectCategory, slug=category_slug)
                context['portfolio_items'] = PortfolioItem.objects.filter(
                    category=category)
            else:
                context['portfolio_items'] = PortfolioItem.objects.all()

            context['categories'] = ProjectCategory.objects.all()

        except Exception as e:
            print(f"Error fetching data: {e}")  # Log the error
            # Provide an error message to the template
            context['error_message'] = "Failed to load data."
        return context


class ComponentsView(TemplateView):
    template_name = 'portfolio/components.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(ProjectCategory, slug=category_slug)
            return Project.objects.filter(category=category).order_by('-date')
        return Project.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        context['active_category'] = self.kwargs.get('category_slug')
        return context


class BlogListView(ListView):
    model = BlogPost
    template_name = 'portfolio/blog.html'
    context_object_name = 'posts'
    paginate_by = 3


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()  # Save the form data to the model

            try:
                send_mail(
                    subject=f"New message from {contact_message.name}",
                    message=contact_message.message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,  # Set to False for debugging
                )
                return redirect('portfolio:contact_success')
            except Exception as e:
                print(f"Error sending email: {e}")
                # Handle the error appropriately, e.g., display an error message to the user
                return render(request, 'portfolio/index.html', {'form': form, 'error_message': 'Failed to send email. Please try again later.'})
        else:
            # Form is invalid
            return render(request, 'portfolio/index.html', {'form': form, 'error_message': 'Please correct the errors below.'})
    else:
        form = ContactForm()
    return render(request, 'portfolio/index.html', {'form': form})


def contact_success_view(request):
    return render(request, 'portfolio/contact_success.html')


# Removed redundant portfolio_view
