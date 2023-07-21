from django.db import models

# Create your models here.
book_audience = [
    ('electronic', 'electronic'),
    ('paper', 'paper')
]

book_category = [
    ('Computer science and the Internet', 'Computer science and the Internet'),
    ('Education and psychology', 'Education and psychology'),
    ('technology', 'technology'),
]


class Customers (models.Model):
    cust_id = models.CharField(max_length=100, primary_key=True,
                               null=False, blank=False, verbose_name="Customer ID")
    cust_name = models.CharField(
        max_length=200, null=False, blank=False, default="", verbose_name="Customer Name")


class Books (models.Model):
    book_id = models.CharField(max_length=100, primary_key=True,
                               null=False, blank=False, verbose_name="Book ID", default="")
    title = models.CharField(max_length=200, blank=False,
                             null=False, verbose_name="Book Title", default="")
    category = models.CharField(max_length=100, choices=book_category,
                                default="computer", null=True, blank=True, verbose_name="Book Category")
    num_page = models.IntegerField(
        blank=True, null=True, verbose_name="Number Pages", default=0)
    book_audience = models.CharField(max_length=100, choices=book_audience,
                                     default="electronic", null=True, blank=True, verbose_name="Book Audience")
    part_series = models.BooleanField(
        null=True, blank=True, default=False, verbose_name="Is Series Book?")
    order_of_book = models.IntegerField(
        blank=True, null=True, default=0, verbose_name="Order of Book")
    version_number = models.IntegerField(
        blank=True, null=True, default=0, verbose_name="Version Number")
    price = models.FloatField(blank=True, null=True,
                              default=0, verbose_name="Price")
    description = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Description")
    cover = models.CharField(max_length=200, null=True, blank=True,
                             verbose_name="Book Image Cover (give url)")
    is_favourite = models.BooleanField(
        default=True, blank=True, null=True, verbose_name="Is this book favourite?")
    is_blocked = models.BooleanField(
        default=False, blank=True, null=True, verbose_name="Is this book blocked?")
    author = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Author")
    publisher = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Publisher")
    language = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Language")
    isbn = models.IntegerField(
        null=True, blank=True, verbose_name="International Number")
    year = models.IntegerField(
        null=True, blank=True, verbose_name="Year of Published")


class Orders (models.Model):
    # cannot delete primary key if there is some other data
    cust_id = models.ForeignKey(
        Customers, on_delete=models.RESTRICT, verbose_name="Customer ID")
    order_id = models.CharField(
        max_length=100, primary_key=True, null=False, blank=False, verbose_name="Order ID")
    order_date = models.DateField(
        auto_now_add=False, blank=False, null=False, verbose_name="Order Date")


class OrderDetails (models.Model):
    order_id = models.ForeignKey(
        Orders, on_delete=models.RESTRICT, verbose_name="Order ID")
    order_detail_id = models.CharField(
        max_length=100, primary_key=True, null=False, blank=False, verbose_name="Order Detail ID", default="")
    book_id = models.ForeignKey(
        Books, on_delete=models.RESTRICT, verbose_name="Book ID")


class UploadBookXLS (models.Model):
    files = models.FileField(upload_to="files", blank=False,
                             null=False, verbose_name="Please Choose XLS file")
