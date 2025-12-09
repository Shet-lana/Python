import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_doctor_about_doctor_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='appointment_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='clinic.appointment')),
            ],
        ),
    ]

