import factory

from django.contrib.auth.models import User

from .models import Room

class UserFactory(factory.Factory):
    class Meta:
        model = User
    username = 'nicacio'
    email = 'nicacionetobsb@gmail.com'
    password = 'admin'



class RoomPremiumFactory(factory.Factory):
    class Meta:
        model = Room
    room_title = "Suíte Presidencial",
    room_location = "Decimo andar, cobertura",
    room_description = "Suite super luxo, com cama kingsize, frigobar, ar condicionado",
    author_id = 1

class RoomEconimicFactory(factory.Factory):
    class Meta:
        model = Room

    room_title = "Quarto econômico",
    room_location = "Segundo andar",
    room_description = "Quarto pequeno, duas camas de solteiro, equipado com ventilador",
    author_id = 1