# Generated by Django 5.0.7 on 2024-08-05 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_task', '0002_categoryitem_taskitem_subtaskitem_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignedcontactitem',
            old_name='assigned_contact_id',
            new_name='user_id',
        ),
    ]
