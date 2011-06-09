from django.db import models

class Picture(models.Model):

    file = models.ImageField(upload_to="pictures")

    def __unicode__(self):
        return self.file

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

