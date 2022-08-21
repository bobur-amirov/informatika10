from django.urls import path

from .views import (index, contents, video, taqdimot,
                    exhibition, textbooks, handbook, elec_textbook,
                    qiuz,quistion,course_book,result_list,
                    )

urlpatterns = [
    path('', index, name='index'),
    path('mundarija/', contents, name='contents'),
    path('video/', video, name='video'),
    path('taqdimotlar/', taqdimot, name='taqdimotlar'),
    path('korgazma/', exhibition, name='exhibition'),
    path('kitoblar/', textbooks, name='textbooks'),
    path('qullanma/', handbook, name='handbook'),
    path('exsel/', elec_textbook, name='elec_textbook'),
    path('kurs-kitob/', course_book, name='course_book'),
    path('chorak/', qiuz, name='quiz'),
    path('chorak/<int:pk>/', quistion, name='quistion'),
    path('natijalar/', result_list, name='result_list'),
]
