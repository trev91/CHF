from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel
from account.models import User as amod


# Define models here

class Product(PolymorphicModel):
  #SUPERCLASS
  #ADD ATTRIBUTES FROM DCD#
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  add_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
  image = models.TextField(null=True, blank=True)
  price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  base_rental_cost = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  #category = models.ForeignKey('catalog.Categories')
  
  def __str__(self):
    #Prints for debug
    return 'Product (abstract): %s (%s)' % (self.name, self.add_date)
    
# This will not show up in the CRUD since it's a parent class. Uncomment below to have show up.
admin.site.register(Product)

RENTAL_STATUS_CHOICES = (
  ('current', 'Rentable'),
  ('damaged', 'Damaged'),
  ('retired', 'No Longer Rentable'),
)
RENTAL_STATUS_CHOICES_MAP = dict(RENTAL_STATUS_CHOICES)

##################################  RENTAL PRODUCTS  #############################################################  
class RentalProduct(Product):
  #rentable PRODUCTS... this inherits from the superclass PRODUCT above
  
  status = models.TextField(null=True, blank=True, choices=RENTAL_STATUS_CHOICES)
  rental_length = models.IntegerField(null=True, blank=True)
  daily_fee = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  
  #ADD ATTRIBUTES FROM DCD#
  
  def __str__(self):
    #Prints for debug
    return 'Rental Product: %s (%s): %s' % (self.name, self.add_date, self.status)
    
admin.site.register(RentalProduct)    
###############################  INDIVIDUAL PRODUCTS   ###########################################################    
class IndividualProduct(Product):
  #individual PRODUCTS... this inherits from the superclass PRODUCT above

  creator = models.ForeignKey('account.User')
  date_made = models.DateTimeField(null=True, blank=True)
  quantity_on_hand = models.IntegerField(default = 0, null=True, blank=True)
  #category = models.TextField(null=True, blank=True)
  #ADD ATTRIBUTES FROM DCD#
  
  def __str__(self):
    #Prints for debug
    return 'Individual Product: %s (%s): %s' % (self.name, self.add_date, self.creator.get_full_name)
    
admin.site.register(IndividualProduct)

###############################  BULK PRODUCTS   ###########################################################    
class BulkProduct(Product):
  #Bulk PRODUCTS... this inherits from the superclass PRODUCT above

  quantity = models.IntegerField(default=0)
  wholesale_value = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  #category = models.TextField(null=True, blank=True)
  #ADD ATTRIBUTES FROM DCD#

  def __str__(self):
    #Prints for debug
    return 'Bulk Product: %s (%s): %s' % (self.name, self.add_date, self.quantity)
    
admin.site.register(BulkProduct)

###############################  CATEGORIES   ###########################################################  
#class Categories(Product):
  
  #category_name = models.TextField(null=True, blank=True, default='default')
  #c_description = models.TextField(null=True, blank=True)
  
  #def __str__(self):
    #Prints for debug
    #return '(%s): %s' % (self.category_name, self.c_description)
    
#admin.site.register(Categories)
  


###############################  VENUE  ###########################################################    

class Venue(models.Model):

  #ADD ATTRIBUTES FROM DCD#
  venue_name = models.TextField(null=True, blank=True)
  address1 = models.TextField(null=True, blank=True)
  address2 = models.TextField(null=True, blank=True)
  city = models.TextField(null=True, blank=True)
  state = models.TextField(null=True, blank=True)
  zipcode = models.TextField(null=True, blank=True)
  image = models.TextField(null=True, blank=True)
  
  def __str__(self):
    #Prints for debug
    return '%s' % (self.venue_name)
    
admin.site.register(Venue) 

###############################  EVENT   ###########################################################    

class Event(models.Model):

  #ADD ATTRIBUTES FROM DCD#
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  add_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
  image = models.TextField(null=True, blank=True)
  start_date = models.DateTimeField(null=True, blank=True)
  end_date = models.DateTimeField(null=True, blank=True)
  venue = models.ForeignKey(Venue)
  
  def __str__(self):
    #Prints for debug
    return '%s' % (self.name)
  
admin.site.register(Event)
###############################  AREA   ###########################################################    

class Area(models.Model):

  #ADD ATTRIBUTES FROM DCD#
  area_name = models.TextField(null=True, blank=True)
  description =  models.TextField(null=True, blank=True)
  place_number =  models.TextField(null=True, blank=True)
  event = models.ForeignKey('Event')
  # event = models.ForeignKey(Event, related_name"areas")
  
  def __str__(self):
    #Prints for debug
    return '%s' % (self.area_name)
admin.site.register(Area)