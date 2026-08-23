from django.contrib import admin
from .models import (
    User,
    Product,
    Branch,
    Inquiry,
    ContactMessage,
    Category,
    Invoice,
    InvoiceItem,
    Banner,
    images,
)

# Register all models
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Branch)
admin.site.register(Inquiry)
admin.site.register(ContactMessage)
admin.site.register(Category)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Banner)
admin.site.register(images)
