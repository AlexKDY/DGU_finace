# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chart(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.ForeignKey('Item', models.DO_NOTHING, db_column='code', blank=True, null=True)
    window_size = models.IntegerField(blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    open = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    high = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    low = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    close = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chart'


class Fundamental(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.ForeignKey('Item', models.DO_NOTHING, db_column='code', blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    close = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    issued_share = models.BigIntegerField(blank=True, null=True)
    cap = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sector_per = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dividend = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    div_release_date = models.DateField(blank=True, null=True)
    div_payment_date = models.DateField(blank=True, null=True)
    fin_closing_date = models.DateField(blank=True, null=True)
    fin_prev_closing_date = models.DateField(blank=True, null=True)
    total_revenue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    operating_income = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    net_income = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    total_assets = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    total_liabilities = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    total_equity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fundamental'


class Investagentvol(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.ForeignKey('Item', models.DO_NOTHING, db_column='code', blank=True, null=True)
    window_size = models.IntegerField(blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    foreign_share = models.BigIntegerField(blank=True, null=True)
    foreign_share_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    foreign_buy_volume = models.BigIntegerField(blank=True, null=True)
    isttt_share = models.BigIntegerField(blank=True, null=True)
    isttt_share_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    isttt_buy_volume = models.BigIntegerField(blank=True, null=True)
    indi_share = models.BigIntegerField(blank=True, null=True)
    indi_share_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    indi_buy_volume = models.BigIntegerField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    close = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investagentvol'


class Item(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    fullcode = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    market = models.CharField(max_length=50, blank=True, null=True)
    sector_name = models.CharField(max_length=100, blank=True, null=True)
    sector_code = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.ForeignKey(Item, models.DO_NOTHING, db_column='code', blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class User(models.Model):
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Volume(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.ForeignKey(Item, models.DO_NOTHING, db_column='code', blank=True, null=True)
    window_size = models.IntegerField(blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    trading_val = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume'
