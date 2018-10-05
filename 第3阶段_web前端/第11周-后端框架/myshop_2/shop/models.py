from django.db import models


class Navigation(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    add_user = models.CharField(max_length=30)
    add_time = models.CharField(max_length=30)
    status = models.SmallIntegerField()


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=30, null=True)


class User_Receiving_Address(models.Model):
    userid = models.ForeignKey('User')  # 外键
    areaid = models.CharField(max_length=32)
    Address = models.CharField(max_length=300)


class Classify(models.Model):
    name = models.CharField(max_length=30)
    Parentid = models.IntegerField()
    add_time = models.DateTimeField(auto_now=True)
    add_user_id = models.ForeignKey('shop_manage.Manage', default=1)


class Commodity(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    number = models.IntegerField()
    classify_id = models.ForeignKey('Classify')  # 外键
    add_time = models.CharField(max_length=30)
    add_adminuser_id = models.ForeignKey('shop_manage.Manage', default=1)
    status = models.SmallIntegerField()


class Commodity_introduce(models.Model):
    commodity_id = models.ForeignKey('Commodity')  # 外键
    content = models.TextField()


class Commodity_img(models.Model):
    commodity_id = models.ForeignKey('Commodity')  # 外键
    path = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now=True)


class Commodity_evaluate(models.Model):
    commodity_id = models.ForeignKey('Commodity')  # 外键
    user_id = models.ForeignKey('User')  # 外键
    Content = models.TextField()
    status = models.SmallIntegerField()


class Shopping_cart(models.Model):
    commodity_id = models.ForeignKey('Commodity')  # 外键
    user_id = models.ForeignKey('User')  # 外键
    number = models.IntegerField()
    checked = models.SmallIntegerField()
    add_time = models.DateTimeField(auto_now=True)



class Order_form(models.Model):
    code_num = models.CharField(max_length=32, unique=True)  # 唯一索引
    add_time = models.CharField(max_length=30)
    user_id = models.ForeignKey('User')  # 外键
    money = models.DecimalField(max_digits=10, decimal_places=2)
    pay_time = models.CharField(max_length=30)
    pay_money = models.DecimalField(max_digits=10, decimal_places=2)
    pay_type = models.CharField(max_length=50)
    pay_status = models.SmallIntegerField()
    status = models.SmallIntegerField()


class Order_particulars(models.Model):
    order_id = models.ForeignKey('Order_form')  # 外键
    commodity_id = models.ForeignKey('Commodity')  # 外键
    number = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Collection(models.Model):
    user_id = models.ForeignKey('User')  # 外键
    commodity_id = models.ForeignKey('Commodity')  # 外键
    add_time = models.CharField(max_length=30)
    status = models.SmallIntegerField()


class Home_floor(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    img_path = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now=True)
    add_user = models.CharField(max_length=10, default=0)



class Home_floor_commodity(models.Model):
    floot_id = models.ForeignKey('Home_floor')  # 外键
    commodity_id = models.ForeignKey('Commodity')  # 外键
    paixu = models.CharField(max_length=20, default=0)


class Commodity_recommend(models.Model):
    commodity_id = models.ForeignKey('Commodity')  # 外键
    end_time = models.CharField(max_length=30)
    sort = models.IntegerField()
    status = models.SmallIntegerField()
    add_username = models.CharField(max_length=30)
    add_time = models.CharField(max_length=30)
