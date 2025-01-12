from django.contrib import admin
from .models import Opportunity, Application, MockTest

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'category', 'location', 'deadline', 'is_paid')
    list_filter = ('category', 'is_paid', 'company', 'deadline')  # Added deadline to list_filter instead
    search_fields = ('title', 'company', 'location')
    # Removed date_hierarchy to avoid the datetime_trunc_sql issue

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'college', 'opportunity', 'applied_at', 'status')
    list_filter = ('opportunity__category', 'opportunity__company', 'status')
    search_fields = ('name', 'email', 'college', 'opportunity__title')
    # Removed date_hierarchy to avoid the datetime_trunc_sql issue
    readonly_fields = ('applied_at',)

    def get_opportunity_title(self, obj):
        return obj.opportunity.title
    get_opportunity_title.short_description = 'Opportunity'

@admin.register(MockTest)
class MockTestAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)