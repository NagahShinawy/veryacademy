from apps.lotusforcontracting.models import Company, Director

directors = Director.objects.listall()

print(directors)


Director.objects.delete()

directors = Director.objects.listall()

print(directors)

ahmed = Director.objects.filter(name__iexact="ahmed")

print(ahmed)

ahmed.delete()

print(ahmed)