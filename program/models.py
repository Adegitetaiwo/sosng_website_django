from xml.dom.minidom import Document
from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils import timezone as tz
import datetime
import pytz

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Program(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    flyer = models.ImageField(
        upload_to="images", height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(max_length=300, unique=True, editable=False, default="nan")
    body = models.TextField()
    google_form = models.URLField(blank=True, null=True)
    google_form_check = models.BooleanField(default=False, editable=False)
    tag_one = models.CharField(max_length=50, null=True, blank=True)
    tag_two = models.CharField(max_length=50, null=True, blank=True)
    tag_three = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    posted = models.DateTimeField(
        auto_now=False, auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True, auto_now_add=False)
    feature = models.BooleanField(default=True)


    def __str__(self) -> str:
        return (self.title).__str__()
    
    class Meta:
        verbose_name_plural = 'Programs'
        ordering = ("-posted",)
    
    def save(self, *args, **kwargs):
        # create a random string
        random_str = get_random_string(5)
        if self.google_form:
            self.google_form_check = True
        # add string to title for unique slug
        self.slug = slugify(self.title + str(self.start_date))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def not_started(self):
        return self.start_date > tz.now() and self.end_date > tz.now()

    @property
    def is_ongoing(self):
        return self.start_date < tz.now() and self.end_date > tz.now()
            
    @property
    def is_past_due(self):
        return self.start_date < tz.now() and self.end_date < tz.now()
            

    def get_absolute_url(self):
        return reverse("program:program_detail", kwargs={"slug": self.slug})

# length of program code
CODE_LENGTH = 20

def generate_id_length():
    return get_random_string(CODE_LENGTH)

class PassCode(models.Model):
    program = models.OneToOneField(Program, on_delete=models.CASCADE)
    code = models.CharField(max_length=CODE_LENGTH,
            editable=True,
            null=True, blank=True,
            default=generate_id_length
        )

    def __str__(self) -> str:
        return f"Pass Code: {self.code[:5]}xxxxxx for {self.program} Program".__str__()

@receiver(post_save, sender=Program)
def create_passcode(sender, instance=None, created=False, **kwargs):
    if created:
        PassCode.objects.create(program=instance)

Choices = (
    ('video', 'Video Link'),
    ('document', 'Document Upload/link')
)
class ProgramResource(models.Model):
    program = models.ForeignKey(
        Program, verbose_name="Program", on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    type_of = models.CharField(max_length=150, 
    choices= Choices)
    link = models.URLField(max_length=1000, blank=True, null=True)
    Document_upload = models.FileField(upload_to='media', max_length=100, blank=True, null=True)
    file_title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.file_title}"