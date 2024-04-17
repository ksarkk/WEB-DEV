from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    city = models.CharField(max_length=100, default="")
    address = models.TextField(default="")

    def to_jsonCom(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=30, default="")
    description = models.TextField(default="")
    salary = models.FloatField(default=0.0)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

    def to_jsonVac(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company_id': self.company.id
        }
