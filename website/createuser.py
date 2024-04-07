from django.contrib.auth.models import User
user = User.objects.create_user(username='qwerty', email='qwerty@qwerty.com', password='qwerty')
user.last_name = "Lennon"
user.save()