from import_export import resources
from .models import Bank_Detail

class BankDetailResource(resources.ModelResource):
	class Meta:
		model = Bank_Detail
		import_id_fields = ('bank_id',)
		exclude = ('id',)
		fields = ('id','ifsc','bank_id','branch','address','city','district','state','bank_name')