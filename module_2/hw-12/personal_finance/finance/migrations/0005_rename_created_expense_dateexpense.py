# Generated by Django 4.0 on 2022-01-04 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_expense_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='created',
            new_name='dateExpense',
        ),
    ]
