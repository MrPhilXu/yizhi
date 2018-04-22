import xadmin
from .models import Transfer
from xadmin import views

class TransferAdmin(object):
     list_display = ['name','image','type','subject','number','price','add_time']
     search_fields = ['name','image','type','subject','number','price']
     list_filter = ['name','image','type','subject','number','price','add_time']




xadmin.site.register(Transfer,TransferAdmin)  