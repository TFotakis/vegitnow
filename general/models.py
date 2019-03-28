from django.db import models


class Language(models.Model):
	Name = models.CharField(default='', max_length=100)
	Code = models.CharField(default='', max_length=10)

	def __str__(self): return self.Code + ': ' + self.Name


class StaticPage(models.Model):
	Main = models.ForeignKey('StaticPageTranslation', blank=True, null=True, on_delete=models.DO_NOTHING)

	def __str__(self): return self.Main.Name


class StaticPageTranslation(models.Model):
	StaticPage = models.ForeignKey(StaticPage, blank=True, null=True, on_delete=models.CASCADE)
	Language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
	Name = models.CharField(default='', max_length=1024)
	Content = models.TextField(blank=True)
	# Todo: Make single field (Listed/Unlisted/Private)
	Listed = models.BooleanField(default=False)
	Private = models.BooleanField(default=True)

	def __str__(self): return self.Name


class NewsletterUser(models.Model):
	email = models.CharField(default='', max_length=254)
	SubscribeDateTime = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.email
