from django.db import models


class DirectorQueryset(models.query.QuerySet):
    def delete(self):
        qs = self.filter(end_date__isnull=False)
        for obj in qs:
            obj.delete()


class DirectorModelManager(models.Manager):
    def listall(self):
        return self.filter(end_date__isnull=True)

    def get_queryset(self):
        return DirectorQueryset(self.model, using=self._db)

    def delete(self):
        return self.get_queryset().delete()