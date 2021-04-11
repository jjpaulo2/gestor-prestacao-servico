from django.contrib import admin

from django.contrib.auth import admin as auth_admin
from django.contrib.auth import models as auth_models

from . import models

# *
# Defininindo as opções do painel de Administração
# *

class GestorAdminSite(admin.AdminSite):
    site_header = 'Administração do site'
    site_title = 'Administração do site'
    index_title = 'Gestor de serviços'

admin.site = GestorAdminSite()


# *
# Registrando entidades da aplicação no Admin
# *

@admin.register(models.Cliente, site=admin.site)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'email')
    search_fields = ('nome', 'cpf', 'telefone', 'email')

    fieldsets = (
        ('Informações pessoais', {
            'fields': ('nome', 'cpf') 
        }),
        ('Informações de contato', {
            'fields': ('email', 'telefone')
        })
    )


# *
# Registrando entidades de autenticação do Django no Admin
# *

admin.site.register(auth_models.User, auth_admin.UserAdmin)
admin.site.register(auth_models.Group, auth_admin.GroupAdmin)
