from django.contrib import admin
from .models import QuestionsP
from .models import QuestionsSchool
from .models import QuestionsGraduates
from .models import QuestionsDropouts

# Register your models here.

admin.site.register(QuestionsP)
admin.site.register(QuestionsSchool)
admin.site.register(QuestionsGraduates)
admin.site.register(QuestionsDropouts)



