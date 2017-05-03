from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible #Necesario usando python3 ??
from django.core.validators import MinValueValidator

DEPARTMENTS=( # ("Model","Human-readeable"),
    ("Other","Autres"),
    ("Axes","Axes"),
    ("Frames","Cadres"),
    ("Bars","Ceintres"),
    ("Chains","Chaines"),
    ("Forks","Fourches"),
    ("Pedals","Pedales"),
    ("Pedaliers","Pedaliers"),
    ("Tires","Pneus"),
    ("Potences","Potences"),
    ("Wheels","Roues"),
    ("Saddles","Selles"),
    ("Bikes","Velos"),
)



class Article(models.Model):
    #Article (id, name, department, description, price)
    name=models.CharField(max_length=50 )
    description=models.TextField()
    price=models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0,
        validators=[ MinValueValidator(0),]
        )
    department=models.CharField(
        max_length=20,
        default="Other",
        choices=DEPARTMENTS,

        )

    def __str__(self):
        return self.name

    def get_quantity(self):
        return self.stock.quantity
        get_quantity.admin_order_field = "quantity"
        get_quantity.short_description="Remaining Stock"

    def available(self):
        return self.get_quantity() >0
    available.boolean = True
    available.short_description="available?"

    def get_date(self):
        return self.stock.pub_date



class Stock(models.Model):
    #Stock(idArticle, quantity, pub_date,)
    article=models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        primary_key=True,
        )
    quantity=models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
        null=True
        )
    pub_date=models.DateTimeField(
        default=datetime.now,
        )

    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description="Published recently?"

    def __str__(self):
        return "%s %s" % (self.article.name, self.quantity)
