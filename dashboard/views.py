from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from main.serializers import *

"""//////////<<<< Banner model CRUD start >>>>////////////////"""

#get all
class GetAllBanner_view(ListAPIView):
    queryset = Banner.objects.all().order_by('-id')
    serializer_class = BannerSer


# create
class CreateBanner_view(CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSer


#update
class UpdateBanner_view(UpdateAPIView):
    queryset = Banner.objects.all()
    serializers_class = BannerSer


#delete
class DeleteBanner_view(DestroyAPIView):
    queryset = Banner.objects.all()
    serializers_class = BannerSer

"""////////// Banner model CRUD end ////////////////"""


"""//////////<<<< Product model CRUD start >>>>////////////////"""

#get all
class GetAllProduct_view(ListAPIView):
    quaryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSer


#create
class CreateProduct_view(CreateAPIView):
    quaryset = Product.objects.all()
    serializers_class = ProductSer


#update
class Updateprodoct_view(UpdateAPIView):
    quaryset = Product.objects.all()
    serializers_class = ProductSer


#delete
class DeleteProduct_view(DestroyAPIView):
    quaryset = Product.objects.all()
    serializers_class = ProductSer


"""////////// Product model CRUD end ////////////////"""


"""//////////<<<< Tag model CRUD start >>>>////////////////"""


#get all
class GetAllTag_view(ListAPIView):
    quaryset = Tag.objects.all().order_by('-id')
    serializers_class = TagSer


#create
class CreateTag_view(CreateAPIView):
    quaryset = Tag.objects.all()
    serializers_class = TagSer


#update
class UpdateTag_view(UpdateAPIView):
    quaryset = Tag.objects.all()
    serializers_class = TagSer


#delete
class DeleteTag_view(DestroyAPIView):
    quaryset = Tag.objects.all()
    serializers_class = TagSer


"""////////// Tag model CRUD end ////////////////"""


"""//////////<<<< Advantage model CRUD start >>>>////////////////"""

#   get all
class GetAllAdventage_view(ListAPIView):
    quaryset = Advantage.objects.all().order_by('-id')
    serializers_class = AdvantageSer


#   create
class CreateAdventage_view(CreateAPIView):
    quaryset = Advantage.objects.all()
    serializers_class = AdvantageSer


#   update
class UpdateAdventage_view(UpdateAPIView):
    quaryset = Advantage.objects.all()
    serializers_class = AdvantageSer


#   delete
class DeleteAdventage_view(DestroyAPIView):
    quaryset = Advantage.objects.all()
    serializers_view = AdvantageSer


"""////////// Advantage model CRUD end ////////////////"""


"""//////////<<<< Favorite_food model CRUD start >>>>////////////////"""

#   get all
class GetAllFavorite_food_view(ListAPIView):
    quaryset = Favorite_food.objects.all().order_by('-id')
    serializers_class = Favorite_foodSer


#   create
class CreateFavorite_food_view(CreateAPIView):
    quaryset = Favorite_food.objects.all()
    serializers_class = Favorite_foodSer


#   update
class UpdateFavorite_food_view(UpdateAPIView):
    quaryset = Favorite_food.objects.all()
    serializers_class = Favorite_foodSer


#delete
class DeleteFavorite_foot_view(DestroyAPIView):
    quaryset = Favorite_food.objects.all()
    serializers_class = Favorite_foodSer


"""////////// Favorite_food model CRUD end ////////////////"""


"""//////////<<<< Branch model CRUD start >>>>////////////////"""

#   get all
class GetAllBranch_view(ListAPIView):
    quaryset = Branch.objects.all().order_by('-id')
    serializers_class = BranchSer


#   create
class CreateBranch_view(CreateAPIView):
    quaryset = Branch.objects.all()
    serializers_class = BranchSer


#   update
class UpdateBranch_view(UpdateAPIView):
    quaryset = Branch.objects.all()
    serializers_class = BranchSer


# delete
class DeleteBranch_view(DestroyAPIView):
    quaryset = Branch.objects.all()
    serializers_class = BrnachSer



"""////////// Branch model CRUD end ////////////////"""


"""//////////<<<< Vacancy model CRUD start >>>>////////////////"""

#   get all
class GetAllVacancy_view(ListAPIView):
    quaryset = Vacancy.objects.all().order_by('-id')
    serializers_class = VacancySer


#   create
class CreateVacancy_view(CreateAPIView):
    quaryset = Vacancy.objects.all()
    serializers_class = VacancySer


#   update
class UpdateVacancy_view(UpdateAPIView):
    quaryset = Vacancy.objects.all()
    serializers_class = VacancySer


#   deleted
class DeleteVacancy_view(DestroyAPIView):
    quaryset = Vacancy.objects.all()
    serializers_class = VacancySer


"""////////// Vacancy model CRUD end ////////////////"""


"""//////////<<<< Send_request model CRUD start >>>>////////////////"""

#   get all
class GetAllSend_request_view(ListAPIView):
    quaryset = Send_request.objects.all().order_by('-id')
    serializers_class = Send_requestSer


#   create
class CreateSend_request_view(CreateAPIView):
    quaryset = Send_request.objects.all()
    serializers_class = Send_requestSer


#   update
class UpdateSend_request_view(UpdateAPIView):
    quaryset = Send_request.objects.all()
    serializers_class = Send_requestSer


#   delete
class DeleteSend_ruquest_view(DestroyAPIView):
    quaryset = Send_request.objects.all()
    serializers_class = Send_requestSer


"""////////// Send_request model CRUD end ////////////////"""


"""//////////<<<< Send_request model CRUD start >>>>////////////////"""

#   get all
class GetAllJob_benefit_view(ListAPIView):
    quaryset = Job_benefit.objects.all().order_by('-id')
    serializers_class = Job_benefitSer


#   create
class CreateJob_benefit_view(CreateAPIView):
    quaryset = Job_benefit.objects.all()
    serializers_class = Job_benefitSer


#   update
class UpdateJob_benefit_view(UpdateAPIView):
    quaryset = Job_benefit.objects.all()
    serializers_class = Job_benefitSer


#   delete
class DeleteJob_benefit_view(DestroyAPIView):
    quaryset = Job_benefit.objects.all()
    serializers_class = Job_benefitSer


"""////////// Job_benefit model CRUD end ////////////////"""


"""//////////<<<< Career model CRUD start >>>>////////////////"""

#   get all
class GetAllCareer_view(ListAPIView):
    quaryset = Career.objects.all().order_by('-id')
    serializers_class = CareerSer


#   create
class CreateCareer_view(CreateAPIView):
    quaryset = Career.objects.all()
    serializers_class = CareerSer

#   update
class UpdateCareer_view(UpdateAPIView):
    quaryset = Career.objects.all()
    serializers_class = CareerSer

#   delete
class DeleteCareer_view(DestroyAPIView):
    quaryset = Career.objects.all()
    serializers_class = CareerSer


"""////////// Career model CRUD end ////////////////"""


"""//////////<<<< About_job model CRUD start >>>>////////////////"""

#   get all
class GetAllAbout_job_view(ListAPIView):
    quaryset = About_job.objects.all().order_by('-id')
    serializers_class = About_jobSer


#   create
class CreateAbout_job_view(CreateAPIView):
    quaryset = About_us.objects.all()
    serializers_class = About_jobSer


#   update
class UpdateAbout_job_view(UpdateAPIView):
    quaryset = About_us.objects.all()
    serializers_class = About_jobSer

#   delete
class DeleteAbout_job_view(DestroyAPIView):
    quaryset = About_us.objects.all()
    serializers_class = About_jobSer


"""////////// About_us model CRUD end ////////////////"""


"""//////////<<<< New model CRUD start >>>>////////////////"""

#   get all
class GetAllNew_view(ListAPIView):
    quaryset = New.objects.all().order_by('-id')
    serializers_class = NewSer


# Create
class CreateNew_view(CreateAPIView):
    quaryset = New.objects.all()
    serializers_class = NewSer


# Update
class UpdateNew_view(UpdateAPIView):
    quaryset = New.objects.all()
    serializers_class = NewSer

# delete
class DeleteNew_view(DestroyAPIView):
    quaryset = New.objects.all()
    serializers_class = NewSer


"""////////// New model CRUD end ////////////////"""


"""//////////<<<< About_job model CRUD start >>>>////////////////"""

#   get all
class GetAllAbout_us_view(ListAPIView):
    quaryset = About_us.objects.all().order_by('-id')
    serializers_class = About_usSer


# Create
class CreateAbout_us_view(CreateAPIView):
    quaryset = About_us.objects.all()
    serializers_class = About_usSer


#   update
class UpdateAbout_us_view(UpdateAPIView):
    quaryset = About_us.objects.all().order_by('-id')
    serializers_class = About_usSer


#   delete
class DeleteAbout_us_view(DestroyAPIView):
    quaryset = About_us.objects.all()
    serializers_class = About_usSer


"""////////// About_us model CRUD end ////////////////"""


"""//////////<<<< Resume model CRUD start >>>>////////////////"""

#  get all
class GetAllResume_view(ListAPIView):
    quaryset = Resume.objects.all().order_by('-id')
    serializers_class = ResumeSer


# create
class CreateResume_view(CreateAPIView):
    quaryset = Resume.objects.all()
    serializers_class = ResumeSer


#   Update
class UpdateResume_view(UpdateAPIView):
    quaryset = Resume.objects.all()
    serializers_class = ResumeSer


#   Delete
class DeleteResume_view(DestroyAPIView):
    quaryset = Resume.objects.all()
    serializers_class = ResumeSer


"""////////// Resume model CRUD end ////////////////"""


"""//////////<<<< Testimonial model CRUD start >>>>////////////////"""

#  get all
class GetAllTestimonial_view(ListAPIView):
    quaryset = Testimonial.objects.all().order_by('-id')
    serializers_class = TestimonialSer


# create
class CreateTestimonial_view(CreateAPIView):
    quaryset = Testimonial.objects.all()
    serializers_class = TestimonialSer


# update
class UpdateTestimonial_view(UpdateAPIView):
    quaryset = Testimonial.objects.all()
    serializers_class = TestimonialSer


# update
class DeleteTestimonial_view(DestroyAPIView):
    quaryset = Testimonial.objects.all()
    serializers_class = TestimonialSer


"""////////// Resume model CRUD end ////////////////"""


"""//////////<<<< Contact model CRUD start >>>>////////////////"""

#  get all
class GetAllConact_view(ListAPIView):
    quryset = Contact.objects.all().order_by('-id')
    serializers_class = ConactSer


#   create
class CreateContact_view(CreateAPIView):
    quaryset = Contact.objects.all()
    serializers_class = ContactSer


#   update
class UpdateContact_view(UpdateAPIView):
    quaryset = Contact.objects.all()
    serializers_class = ContactSer


#   delete
class DeleteContact_view(DestroyAPIView):
    quaryset = Contact.objects.all()
    serializers_class = ContactSer


"""////////// Contact model CRUD end ////////////////"""


"""//////////<<<< Info model CRUD start >>>>////////////////"""

#  get all
class GetAllInfo_view(ListAPIView):
    quaryset = Info.objects.all().order_by('-id')
    serializers_class = InfoSer


#   create
class CreateInfo_view(CreateAPIView):
    quaryset = Info.objects.all()
    serializers_class = InfoSer


#   create
class UpdateInfo_view(UpdateAPIView):
    quaryset = Info.objects.all()
    serializers_class = InfoSer


#   delete
class DeleteInfo_view(DestroyAPIView):
    quaryset = Info.objects.all()
    serializers_class = InfoSer


"""////////// Info model CRUD end ////////////////"""




