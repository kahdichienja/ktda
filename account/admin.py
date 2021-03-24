from django.contrib import admin
from .models import FarmerModel, RecordModel
# Register your models here.


class FarmerModelModelAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name",
                    "id_number", "ktda_number", "timestamp"]
    list_display_links = ["ktda_number", "full_name"]
    list_filter = ["full_name", "ktda_number"]
    search_fields = ["full_name", "ktda_number"]

    class Meta:
        model = FarmerModel


admin.site.register(FarmerModel, FarmerModelModelAdmin)


class RecordModelModelAdmin(admin.ModelAdmin):
    list_display = ["user", "admin_name",
                    "no_of_kilo", "price", "tea_type", "timestamp"]
    list_display_links = ["tea_type", "admin_name"]
    list_filter = ["admin_name", "tea_type"]
    search_fields = ["admin_name", "tea_type"]

    class Meta:
        model = RecordModel


admin.site.register(RecordModel, RecordModelModelAdmin)
