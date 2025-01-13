from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Opportunity, MockTest
from .forms import ApplicationForm

def home(request):
    return render(request, 'career/home.html')

def opportunity_list(request, category):
    opportunities = Opportunity.objects.filter(category=category)
    template_name = f'career/{category}s.html'
    context = {
        'opportunities': opportunities,
        'category': category,
        'category_title': category.title()  # Capitalizes the category name
    }
    return render(request, template_name, context)

def apply(request, opportunity_id):
    opportunity = get_object_or_404(Opportunity, id=opportunity_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.opportunity = opportunity
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('home')
    else:
        form = ApplicationForm()
    
    return render(request, 'career/application_form.html', {
        'form': form,
        'opportunity': opportunity
    })

def mock_tests(request):
    tests = MockTest.objects.all()
    return render(request, 'career/mock_tests.html', {'tests': tests})

def activity_points(request):
    return render(request, 'career/activity_points.html')