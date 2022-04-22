from django.db import models

class Node(models.Model):
	text_field = models.TextField()
	image_field = models.ImageField()
	ssilka = models.TextField()

	def get_title(self):
		self.title = self.text_field[:50]     
		return self.title

	class Meta:
		verbose_name_plural = "Плитка"

	def __str__(self):
		return str(self.text_field)


class DutyForToday(models.Model):
	kabinet_five = models.CharField(max_length=250)
	kabinet_four = models.CharField(max_length=250)
	date = models.DateField()

	class Meta:
		verbose_name_plural = "Дежурные"
  
	def __str__(self):
		return str(self.date)


class NumbersPhone(models.Model):
    number = models.CharField(max_length=255, verbose_name='Номер телефона')

    class Meta:
        ordering = ['number']
        verbose_name_plural = "Номера телефонов"

    def __str__(self):
        return self.number


class PPO(models.Model):
	name = models.CharField(max_length=255)
	technics_type = models.ManyToManyField(NumbersPhone)

	class Meta:
		verbose_name_plural = "Ответственные за ППО"
 
	def __str__(self):
		return self.name


class Messages(models.Model):
	message = models.TextField()
	date_end = models.DateField()

	class Meta:
		verbose_name_plural = "Уведомления"

	def __str__(self):
		return str(self.message)