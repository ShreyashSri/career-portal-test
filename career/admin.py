from django.contrib import admin
from .models import Opportunity, Application, MockTest

admin.site.register(Opportunity)
admin.site.register(Application)
admin.site.register(MockTest)