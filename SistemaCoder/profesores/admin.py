from django.contrib import admin
from .models import Profesor, Curso

class ProfesorAdmin( admin.ModelAdmin):
    
    list_display = ('id', 'nombre', 'apellido','curso')
    
class CursoAdmin(admin.ModelAdmin):
    exclude = ('creacion',)
    list_display = ('id', 'nombre')
    
# Register your models here.
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Curso, CursoAdmin)
