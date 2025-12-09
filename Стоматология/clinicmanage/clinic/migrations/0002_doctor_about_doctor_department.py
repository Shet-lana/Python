from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='О враче'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.CharField(blank=True, max_length=100, verbose_name='Отделение'),
        ),
    ]

