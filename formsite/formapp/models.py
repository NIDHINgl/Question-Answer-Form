from django.db import models 

class loginfiles(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	phone = models.CharField(max_length=12)
	password = models.CharField(max_length=8)
	class Meta:
		db_table = "user"

class questionfiles(models.Model):
    idform=models.AutoField(primary_key=True)
    question=models.CharField(max_length=100)
    class Meta:
	       db_table ="qns"

class answerfiles(models.Model):
    answer=models.CharField(max_length=100)
    idform=models.ForeignKey(questionfiles, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
	       db_table ="ans"