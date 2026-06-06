#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User

# Crear Superuser
superuser, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@rrhh.com',
        'is_staff': True,
        'is_superuser': True,
        'first_name': 'Administrador',
        'last_name': 'Sistema'
    }
)

if created:
    superuser.set_password('Admin123456!')
    superuser.save()
    print(" Superuser creado:")
    print(f"   Username: {superuser.username}")
    print(f"   Email: {superuser.email}")
    print(f"   Password: Admin123456!")
    print(f"   is_staff: {superuser.is_staff}")
    print(f"   is_superuser: {superuser.is_superuser}")
else:
    print(" Superuser 'admin' ya existe")

# Crear Usuario Normal
usuario_normal, created = User.objects.get_or_create(
    username='empleado',
    defaults={
        'email': 'empleado@rrhh.com',
        'is_staff': False,
        'is_superuser': False,
        'first_name': 'Juan',
        'last_name': 'Pérez'
    }
)

if created:
    usuario_normal.set_password('Usuario123456!')
    usuario_normal.save()
    print("\n Usuario normal creado:")
    print(f"   Username: {usuario_normal.username}")
    print(f"   Email: {usuario_normal.email}")
    print(f"   Password: Usuario123456!")
    print(f"   is_staff: {usuario_normal.is_staff}")
    print(f"   is_superuser: {usuario_normal.is_superuser}")
else:
    print(" Usuario 'empleado' ya existe")

# Listar todos los usuarios
print("\n Usuarios en el sistema:")
for user in User.objects.all():
    role = " Superuser" if user.is_superuser else (" Admin" if user.is_staff else " Normal")
    print(f"   {role} - {user.username} ({user.email})")
