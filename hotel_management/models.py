from django.db import models

# Create your models here.
# class RoomOccupant(models.Model):
#     id = models.AutoField(primary_key=True)
#     occupant_name = models.CharField(max_length=100)
#     occupant_email = models.EmailField()
#     occupant_occupation = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.occupant_name
    
class HotelRecord(models.Model):
    id = models.AutoField(primary_key=True)
    occupant_name = models.CharField(max_length=100)
    occupant_email = models.EmailField()
    occupant_occupation = models.CharField(max_length=100)
    room_number = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_nights = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.occupant_name + " Room " + str(self.room_number)
