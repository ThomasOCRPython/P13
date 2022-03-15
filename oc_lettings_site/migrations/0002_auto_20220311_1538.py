# Generated by Django 3.0 on 2022-03-11 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name="letting",
                    name="address",
                ),
                migrations.RemoveField(
                    model_name="profile",
                    name="user",
                ),
                migrations.DeleteModel(
                    name="Address",
                ),
                migrations.DeleteModel(
                    name="Letting",
                ),
                migrations.DeleteModel(
                    name="Profile",
                ),
            ],
            database_operations=[
                migrations.AlterModelTable("letting", "lettings_letting"),
                migrations.AlterModelTable("address", "lettings_address"),
                migrations.AlterModelTable("profile", "profiles_profile"),
            ],
        )
    ]
