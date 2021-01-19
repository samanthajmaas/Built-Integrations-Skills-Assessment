from django.db import models

class People(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, serialize=True)
    person_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    height = models.IntegerField()
    mass = models.IntegerField()
    hair_color = models.CharField(max_length=255)
    eye_color = models.CharField(max_length=255)
    birth_year = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

    unserializable_fields = ('id',)

    class Meta:
        db_table = 'people'
    
    def to_dict(self):
        seralized = {}
        for field in self._meta.get_fields():
            if field.name in self.unserializable_fields:
                continue
            
            seralized[field.name] = getattr(self, field.name)
        return seralized
