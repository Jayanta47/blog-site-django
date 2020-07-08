from django.db.models.signals import post_save
# post_save called after any object is saved
from django.contrib.auth.models import User
# user is going to send the signal
from django.dispatch import receiver
# works as the reciever, also a decorator that is going to be added to our program
from User.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # runs everytime an user is created, needs to be integrated using reciever


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# the whole objective of this hassle is to make a profile
# of an user the very moment an user id is made


