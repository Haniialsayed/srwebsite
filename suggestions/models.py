from django.db import models


class Method(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', default='default.png')
    description = models.TextField()
    """score = models.IntegerField(default=0,
                                validators=[MaxValueValidator(5),
                                            MinValueValidator(0)
                                            ])"""
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)  # automatically populate field with the time suggestion was created.

    def __str__(self):
        # this function would enable us get the name in text when we call it from the shell programmatically
        return self.name

    def snippet(self):
        return self.description[:150] + "..."

    def str(self):
        return str(self.pk)



