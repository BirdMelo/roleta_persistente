import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RenameField(
                    model_name='usuario',
                    old_name='nome',
                    new_name='username',
                ),
                migrations.RenameField(
                    model_name='usuario',
                    old_name='senha',
                    new_name='password',
                ),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='date_joined',
            field=models.DateTimeField(
                default=django.utils.timezone.now
            ),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(
                blank=True,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                related_name='usuario_set',
                related_query_name='usuario',
                to='auth.group',
                verbose_name='groups',
            ),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(
                blank=True,
                related_name='usuario_set',
                related_query_name='usuario',
                to='auth.permission',
                verbose_name='user permissions',
            ),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(
                db_column='nome',
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(
                db_column='senha',
                max_length=128,
            ),
        ),
    ]
