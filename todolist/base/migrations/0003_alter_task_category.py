# Generated by Django 4.2.3 on 2023-07-29 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_category_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="base.category",
            ),
        ),
    ]
