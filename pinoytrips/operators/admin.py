from django.contrib import admin
from .models import Operator, Terminal, Destination


class OperatorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields':['name', 'rating', 'features']}),
		('Contact info', 	{'fields': ['address', 'email', 'phone', 'website']}),
		('Journey info',	{'fields': ['terminal', 'destination']}),
	]
	list_display = ('name', 'website')
	list_filter = ['destination']
	search_fields = ['name','destination']

admin.site.register(Operator, OperatorAdmin)

class TerminalAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'region')

admin.site.register(Terminal)

class DestinationAdmin(admin.ModelAdmin):
	list_display = ('name', 'region')

admin.site.register(Destination, DestinationAdmin)
