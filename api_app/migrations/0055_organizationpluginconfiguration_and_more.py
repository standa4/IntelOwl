# Generated by Django 4.2.8 on 2024-01-09 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("django_celery_beat", "0018_improve_crontab_helptext"),
        ("certego_saas_organization", "0002_membership_is_admin"),
        ("api_app", "0054_job_jobbisearch"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganizationPluginConfiguration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.IntegerField()),
                ("disabled", models.BooleanField(default=False)),
                ("disabled_comment", models.TextField(blank=True, default="")),
                (
                    "rate_limit_timeout",
                    models.DurationField(
                        blank=True,
                        null=True,
                        help_text="Expects data in the format 'DD HH:MM:SS'",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="organizationpluginconfiguration",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="organizationpluginconfiguration",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="certego_saas_organization.organization",
            ),
        ),
        migrations.AddField(
            model_name="organizationpluginconfiguration",
            name="rate_limit_enable_task",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="django_celery_beat.periodictask",
            ),
        ),
    ]
