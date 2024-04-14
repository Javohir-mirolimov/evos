from .views import *
from django.urls import path

urlpatterns = [
    #   Banner urls start
    path('get-all-banner/', GetAllBanner_view.as_view()),
    path('create-banner/', CreateBanner_view.as_view()),
    path('update-banner/<int:pk>/', UpdateBanner_view.as_view()),
    path('delete-banner/<int:pk>/', DeleteBanner_view.as_view()),
    #   Banner urls end

    #   Product urls start
    path('get-all-product/', GetAllProduct_view.as_view()),
    path('create-product/', CreateProduct_view.as_view()),
    path('update-product/<int:pk>/', Updateprodoct_view.as_view()),
    path('delete-product/<int:pk>/', DeleteProduct_view.as_view()),
    #   Product urls end

    #   Tag urls start
    path('get-all-tag/', GetAllTag_view.as_view()),
    path('create-tag/', CreateTag_view.as_view()),
    path('update-tag/<int:pk>/', UpdateTag_view.as_view()),
    path('delete-tag/<int:pk>/', DeleteTag_view.as_view()),
    #   Tag-objects urls end

    #   Advantage urls start
    path('get-all-advantage/', GetAllAdventage_view.as_view()),
    path('create-advantage/', CreateAdventage_view.as_view()),
    path('update-advantage/<int:pk>/', UpdateAdventage_view.as_view()),
    path('delete-advantage/<int:pk>/', DeleteAdventage_view.as_view()),
    #   Advantage-objects urls end

    #   Favorite_food urls start
    path('get-all-favorite_food/', GetAllFavorite_food_view.as_view()),
    path('create-favorite_food/', CreateFavorite_food_view.as_view()),
    path('update-favorite_food/<int:pk>/', UpdateFavorite_food_view.as_view()),
    path('delete-favorite_food/<int:pk>/', DeleteFavorite_foot_view.as_view()),
    #   Favorite_food -objects urls end

    #   Branch urls start
    path('get-all-favorite_food/', GetAllBranch_view.as_view()),
    path('create-favorite_food/', CreateBranch_view.as_view()),
    path('update-favorite_food/<int:pk>/', UpdateBranch_view.as_view()),
    path('delete-favorite_food/<int:pk>/', DeleteBranch_view.as_view()),
    #   Branch    -objects urls end

    #   Vacancy urls start
    path('get-all-vacancy/', GetAllVacancy_view.as_view()),
    path('create-vacancy/', CreateVacancy_view.as_view()),
    path('update-vacancy/<int:pk>/', UpdateVacancy_view.as_view()),
    path('delete-vacancy/<int:pk>/', DeleteVacancy_view.as_view()),
    #   Vacancy -objects urls end

    #   Send_request urls start
    path('get-all-send_request/', GetAllSend_request_view.as_view()),
    path('create-send_request/', CreateSend_request_view.as_view()),
    path('update-send_request/<int:pk>/', UpdateSend_request_view.as_view()),
    path('delete-send_request/<int:pk>/', DeleteSend_ruquest_view.as_view()),
    #   Send_request -objects urls end

    #   Job_benefit urls start
    path('get-all-job_benefit/', GetAllJob_benefit_view.as_view()),
    path('create-job_benefit/', CreateJob_benefit_view.as_view()),
    path('update-job_benefit/<int:pk>/', UpdateJob_benefit_view.as_view()),
    path('delete-job_benefit/<int:pk>/', DeleteJob_benefit_view.as_view()),
    #   Job_benefit -objects urls end

    #   Career urls start
    path('get-all-career/', GetAllCareer_view.as_view()),
    path('create-career/', CreateCareer_view.as_view()),
    path('update-career/<int:pk>/', UpdateCareer_view.as_view()),
    path('delete-career/<int:pk>/', DeleteCareer_view.as_view()),
    #   Career -objects urls end

    #   About_job urls start
    path('get-all-about_job/', GetAllAbout_job_view.as_view()),
    path('create-about_job/', CreateAbout_job_view.as_view()),
    path('update-about_job/<int:pk>/', UpdateAbout_job_view.as_view()),
    path('delete-about_job/<int:pk>/', DeleteAbout_job_view.as_view()),
    #   About_job -objects urls end

    #   New - objects urls start
    path('get-all-new/', GetAllNew_view.as_view()),
    path('create-new/', CreateNew_view.as_view()),
    path('update-new/<int:pk>/', UpdateNew_view.as_view()),
    path('delete-new/<int:pk>/', DeleteNew_view.as_view()),
    #   New -objects urls end

    #   About_us - objects urls start
    path('get-all-about_us/', GetAllAbout_us_view.as_view()),
    path('create-about_us/', CreateAbout_us_view.as_view()),
    path('update-about_us/<int:pk>/', UpdateAbout_us_view.as_view()),
    path('delete-about_us/<int:pk>/', DeleteAbout_us_view.as_view()),
    #   About_us -objects urls end

    #   Resume - objects urls start
    path('get-all-resume/', GetAllResume_view.as_view()),
    path('create-resume/', CreateResume_view.as_view()),
    path('update-resume/<int:pk>/', UpdateResume_view.as_view()),
    path('delete-resume/<int:pk>/', DeleteResume_view.as_view()),
    #   Resume -objects urls end

    #   Testimonial - objects urls start
    path('get-all-testimonial/', GetAllTestimonial_view.as_view()),
    path('create-testimonial/', CreateTestimonial_view.as_view()),
    path('update-testimonial/<int:pk>/', UpdateTestimonial_view.as_view()),
    path('delete-testimonial/<int:pk>/', DeleteTestimonial_view.as_view()),
    #   Testimonial -objects urls end

    #   Contact - objects urls start
    path('get-all-contact/', GetAllConact_view.as_view()),
    path('create-contact/', CreateContact_view.as_view()),
    path('update-contact/<int:pk>/', UpdateContact_view.as_view()),
    path('delete-contact/<int:pk>/', DeleteContact_view.as_view()),
    #   Contact -objects urls end

    #   Info - objects urls start
    path('get-all-info/', GetAllInfo_view.as_view()),
    path('create-info/', CreateInfo_view.as_view()),
    path('update-info/<int:pk>/', UpdateInfo_view.as_view()),
    path('delete-info/<int:pk>/', DeleteInfo_view.as_view()),
    #   Info -objects urls end

]
