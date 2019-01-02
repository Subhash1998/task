from django.contrib import admin
from .models import Bank_Detail
from import_export.admin import ImportExportModelAdmin
from .resources import BankDetailResource

@admin.register(Bank_Detail)
class Bank_Detail_Admin(ImportExportModelAdmin):
	resource_class = BankDetailResource
	list_disply = ['branch','city','bank_name']