from django.db import models
from django.utils import timezone


# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Ingredients(models.Model):
    ingredient_id = models.AutoField(db_column='Ingredient_id', primary_key=True)  # Field name made lowercase.
    supplement = models.ForeignKey('Product', models.DO_NOTHING, db_column='Supplement_id')  # Field name made lowercase.
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Supplier_id')  # Field name made lowercase.
    ingredient_name = models.CharField(db_column='Ingredient_name')  # Field name made lowercase.
    formula_type = models.CharField(db_column='Formula_type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingredients'



class Inventory(models.Model):
    inventory_id = models.AutoField(db_column='Inventory_id', primary_key=True)  # Field name made lowercase.
    supplement = models.ForeignKey('Product', models.DO_NOTHING, db_column='Supplement_id')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    expiration_date = models.DateField(db_column='Expiration_date', blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'Inventory'


class Product(models.Model):
    supplement_id = models.AutoField(db_column='Supplement_ID', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', blank=True, null=True)  # Field name made lowercase.
    expiration_date = models.DateField(db_column='Expiration_date', blank=True, null=True)  # Field name made lowercase.
    product_type = models.CharField(db_column='Product_type', blank=True, null=True)  # Field name made lowercase.
    dosage_amount = models.CharField(db_column='Dosage_amount', blank=True, null=True)  # Field name made lowercase.
    formula_type = models.CharField(db_column='Formula_type', blank=True, null=True)  # Field name made lowercase.
    is_fda_regulated = models.BooleanField(db_column='Is_fda_regulated', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Supplier_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class ProductIngredients(models.Model):
    id = models.AutoField(primary_key=True)
    supplement_id = models.IntegerField(db_column='Supplement_ID')  # Field name made lowercase.
    ingredient_id = models.IntegerField(db_column='Ingredient_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product_Ingredients'
        unique_together = (('supplement_id', 'ingredient_id'),)


class Supplier(models.Model):
    supplier_id = models.AutoField(db_column='Supplier_id', primary_key=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='Supplier_name')  # Field name made lowercase.
    contact_info = models.CharField(db_column='Contact_info', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplier'