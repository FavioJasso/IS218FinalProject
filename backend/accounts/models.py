from django.db import models
from django.utils import timezone


# Create your models here.
class LogComment(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date")
    supplement = models.ForeignKey('Product', models.DO_NOTHING, db_column='Supplement_id')
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    
    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.username}' comments '{self.message}' on {date.strftime('%A, %d %B, %Y at %X')}"

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


class HelloLogmessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hello_logmessage'

class AccountsLogmessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField()


    class Meta:
        managed = False
        db_table = 'accounts_logmessage'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")
    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"