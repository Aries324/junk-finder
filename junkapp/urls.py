from django.urls import path
from junkapp import views, view_helper
from django.contrib.auth.decorators import login_required

handler404 = 'junkapp.views.error_404'
handler500 = 'junkapp.views.error_500'
# handler403 = 'junkapp.views.error_403'
# handler400 = 'junkapp.views.error_400'


urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.HomeView.as_view(), name='home'),
    path('logout/', views.logout_action, name='logout'),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup),
    # path('sort_by_date/', views.items_by_date_view, name='sort_by_date'),

    path('postitem/', login_required(views.PostItemView.as_view())),
    path('<int:id>/details/', views.item_detail_view, name='item_detail'),
    path('<int:id>/edit/', views.item_edit_view, name='edit'),
    # on form submission, takes form_type and passes it to helper
    # function that takes the type, loads the form data, then redirects
    # to another page
    path('<str:form_type>/standard_form/', view_helper.form_redirect),
    path('filterclaimedfalse/', views.SortByClaimedFalse.as_view()),
    path('filterfurniture/', views.SortByFurniture.as_view()),
    path('filterelectronics/', views.SortByElectronics.as_view()),
    path('filterhomeimprovement/', views.SortByHomeImprovement.as_view()),
    path('filterscraps/', views.SortByScraps.as_view()),
    path('filterclothing/', views.SortByClothing.as_view()),
]
