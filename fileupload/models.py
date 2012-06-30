from django.db import models

class Picture(models.Model):

    # This is a small demo using FileField instead of ImageField, not
    # depending on PIL. You will probably want ImageField in your app.
    file = models.FileField(upload_to="pictures")
    slug = models.SlugField(max_length=50, blank=True)

    def __unicode__(self):
        return self.file

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)
