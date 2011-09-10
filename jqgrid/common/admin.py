from django.contrib import admin

from common.models import Something

class SomethingAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex')

    class Media:
        css = {
            "all": (
                "css/redmond/jquery-ui-1.8.16.custom.css",
                "css/ui.jqgrid.css",
            ),
        }
        js = (
            "js/jquery-1.5.2.min.js",
            "js/i18n/grid.locale-en.js",
            "js/jquery.jqGrid.min.js",
            "js/admin-jqgrid.js"
        )

admin.site.register(Something, SomethingAdmin)
