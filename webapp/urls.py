from django.urls import path

from webapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name='index.html'),
    path('about',views.About, name='about.html'),
    path('bookings',views.Booking, name='booking.html'),
    path('contact',views.contact, name='contact.html'),
    path('room',views.Room,name='room.html'),
    path('service',views.Service, name='service.html'),
    path('team',views.Team, name='team.html'),
    path('testimonial',views.Testimonial, name='testimonial.html'),
    path('restaurant',views.Restaurant, name='restaurant.html'),
    path('spa',views.Spa, name='spa.html'),
    path('event',views.Event, name='event.html'),
    path('cab',views.Cab, name='cab.html'),
    path('gym',views.Gym, name='gym.html'),
    path('wedding',views.Wedding, name='wedding.html'),
    path('holiday',views.Holiday, name='holiday.html'),
    path('corporate-events',views.Corporate, name='corporate.html'),
    path('activites',views.Activities, name='activities.html'),
    path('sample',views.Sample, name='sample.html'),
    # path('signup',views.Signup,name="sign_up.html"),
    # path('login',views.login,name="login.html"),
    
    
    
    path('login_user',views.login_user, name='login.html'),
    path('logout_user',views.logout_user, name='logout'),
    path('register_user',views.register_user, name='register.html'),
    path('profile_user',views.profile_user, name='profile.html'),
    path('edit_profile_user',views.edit_profile, name='edit_profile_user'),
    path('change_password/', views.change_password, name='change_password'),

    # [1] Submit Email Form                             //PasswordResetView.as_view()
    # [2] Email Sent Success Message                    //PasswordResetDoneView.as_view()
    # [3] Link to Password Reset form in Email          //PasswordResetConfirmView.as_view()
    # [4] Password successfullt changed message         //PasswordResetCompleteView.as_view()

    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
         name="reset_password"),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
         name="password_reset_complete"),
]

