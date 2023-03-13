from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Customers')
    citizenship = models.CharField(max_length=20)
    birth_year = models.DateField()
    work_place = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} - {self.citizenship} - {self.birth_year} - {self.work_place}'


class Account(models.Model):
    number = models.CharField(max_length=16)
    account_type = models.IntegerField(default=0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='customers')

    def __str__(self):
        return f'{self.number} - {self.account_type} - {self.client}'


class Credit(models.Model):
    sum = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sum} - {self.date} - {self.account}'

