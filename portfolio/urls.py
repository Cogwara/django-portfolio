from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Home page (handles multiple sections via template)
    path('', views.HomeView.as_view(), name='home'),

    # Components page
    path('components/', views.ComponentsView.as_view(), name='components'),

    # Portfolio sections (using same view with template variations)
    path('about/', views.HomeView.as_view(template_name='portfolio/about.html'), name='about'),
    path('resume/', views.HomeView.as_view(template_name='portfolio/resume.html'), name='resume'),
    path('services/', views.HomeView.as_view(template_name='portfolio/services.html'), name='services'),

    # Projects URLs
    path('portfolio/', views.ProjectListView.as_view(), name='projects'),
    path('portfolio/<slug:category_slug>/',
         views.ProjectListView.as_view(), name='projects_by_category'),

    # Blog URLs
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),

    # Contact URLs
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
]

# Error handlers (optional - can also be in core urls)
handler404 = 'portfolio.views.handler404'
handler500 = 'portfolio.views.handler500'
