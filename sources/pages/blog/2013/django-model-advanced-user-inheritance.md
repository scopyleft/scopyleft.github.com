title: "Advanced Django user model inheritance"
date: 2013-08-05
published: true

Recently I had to manage a few user types each having its own specificities with
Django 1.5.
Not a big deal in theory.

It actually turned quite different and clues were scattered around the web.

Here is what I expected to get at the end:

- users can authenticate by email. No username at all.
- we should have individuals and professionals. We should also preserve system
users such as admin accounts.
- the _email_ must be unique. Though an individual can also have a professional
account with the same _email_ address.
- We should be able to retrieve an account with its specificities without
knowing what kind of account it refers to. That means calling it by pk
for instance.


### Email authentication

A lot of ressources available on the web.

    from django.db import models
    from django.contrib.auth.models import AbstractBaseUser

    class BaseUser(AbstractBaseUser):
        email = models.EmailField(unique=True)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELD = USERNAME_FIELD


### Extending BaseUser

Let's make BaseUser abstract and write specific Users that extend it.

    class GenericUser(BaseUser):
        pass

    class Professional(BaseUser):
        company = models.CharField(max_length=50)
        reference = models.CharField(max_length=10)

    class Individual(BaseUser):
        name = models.CharField(max_length=100)

A _GenericUser_ is a system user such as an administrator.
settings.AUTH_USER_MODEL would refer to it.

### create\_user and create\_superuser

As we're not using the default Django model, we lost these functionalities.
We can reproduce them easily.


    from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager as DjBaseUserManager)

    class BaseUserManager(DjBaseUserManager):
        def create_user(self, email=None, password=None, **extra_fields):
            now = timezone.now()
            email = BaseUserManager.normalize_email(email)
            u = GenericUser(email=email, is_superuser=False, last_login=now, **extra_fields)
            u.set_password(password)
            u.save(using=self._db)
            return u

        def create_superuser(self, email, password, **extra_fields):
            u = self.create_user(email, password, **extra_fields)
            u.is_superuser = True
            u.save(using=self._db)
            return u

    class BaseUser(AbstractBaseUser):
        is_superuser = False
        objects = BaseUserManager()
        …

We also make BaseUser.is_superuser as a hardcoded field which is False
by default.


### Call a User and get its matching subtype

So far we can't call `SomeUser.objects.get(pk=1)` and get the matching user with
its properties.
[Django model utils with InheritanceManager](https://github.com/carljm/django-model-utils#inheritancemanager)
comes to the rescue.

As our BaseUser is abstract we cannot call `BaseUser.objects.get(pk=1)`.
We need to write an intermediate concrete table that we can call `objects` on.

We also make BaseUserManager inherit from InheritanceManager.

    class BaseUserManager(DjBaseUserManager, InheritanceManager):
        …

    class CallableUser(AbstractBaseUser):
        objects = BaseUserManager()


### Ressources

- The final models file with revisions (and their associated tests) is here:
https://gist.github.com/vinyll/6103202
- Django doc about model inheritance:
https://docs.djangoproject.com/en/dev/topics/db/models/#multi-table-inheritance
- django-model-utils: https://github.com/carljm/django-model-utils
