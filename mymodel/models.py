#!/usr/bin/python
# coding:utf-8
from django.db import models

# Create your models here.

class Goods(models.Model):
	ID = models.AutoField(primary_key=True,verbose_name='商品代号')
	Name = models.CharField(max_length=30,verbose_name='商品名称')
	Type = models.CharField(max_length=20,verbose_name='商品类别')
	SellingPrice = models.FloatField(verbose_name='商品售价')
	Inventory = models.IntegerField(verbose_name='库存')

	def __unicode__(self):
		return u'%d %s'%(self.ID,self.Name)

class Record(models.Model):
	Good_id = models.ForeignKey(Goods,verbose_name='商品')
	Price = models.FloatField(verbose_name='价格')
	Date = models.DateField(verbose_name='日期')
	Count = models.FloatField(verbose_name='数量')

class SalesRecord(Record):
	ID = models.AutoField(primary_key=True,verbose_name='销售记录编号')
	
	def __unicode__(self):
		return u'%d %s %lf %s %lf'%(self.ID,self.Good_id.Name,self.Price,self.Date,self.Count)
	
class StockRecord(Record):
	ID = models.AutoField(primary_key=True, verbose_name='进货记录编号')
	
	def __unicode__(self):
		return u'%d %s %s %lf %lf' %(self.ID,self.Good_id.Name,self.Date,self.Count,self.Price)
		
	


class Person(models.Model):
	Name = models.CharField(max_length=30,verbose_name='姓名')
	PhoneNum = models.CharField(max_length=20,verbose_name='电话')

class Member(Person):
	ID = models.AutoField(primary_key=True,verbose_name='会员编号')
	CardNum = models.CharField(max_length=30,verbose_name='卡号')

	
	def __unicode__(self):
		return u'%d %s %s %s'%(self.ID,self.CardNum,self.Name,self.PhoneNum)


class Staff(Person):
	ID = models.AutoField(primary_key=True,verbose_name='职员编号')
	Nickname = models.CharField(max_length=30,verbose_name='昵称')
	Age = models.IntegerField(verbose_name='年龄')
	Sex = models.CharField(max_length=10,verbose_name='性别',choices=(('M','男'),('F','女')))
	Position = models.CharField(max_length=20,verbose_name='职位',choices=(('manager','超市经理'),('buyer','采购员'),('seller','销售员')))
	Address = models.CharField(max_length=50,verbose_name='家庭住址')

	def __unicode__(self):
		return u'%d %s %s %s %s'%(self.ID,self.Name,self.Nickname,self.Position,self.PhoneNum)
	
