
from django.urls import path
from .views import (
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView,
    AssignAgentView, CategoryListView, CategoryDetailView, LeadCategoryUpdateView,
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, LeadJsonView, 
    FollowUpCreateView, FollowUpUpdateView, FollowUpDeleteView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='leads-list'),
    path('json/', LeadJsonView.as_view(), name='leads-list-json'),
    path('<int:pk>/', LeadDetailView.as_view(), name='leads-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='leads-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='leads-delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='leads-category-update'),
    path('<int:pk>/followups/create/', FollowUpCreateView.as_view(), name='leads-followup-create'),
    path('followups/<int:pk>/', FollowUpUpdateView.as_view(), name='leads-followup-update'),
    path('followups/<int:pk>/delete/', FollowUpDeleteView.as_view(), name='leads-followup-delete'),
    path('create/', LeadCreateView.as_view(), name='leads-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
]