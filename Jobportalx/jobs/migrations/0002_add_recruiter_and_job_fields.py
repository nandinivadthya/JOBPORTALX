# Generated migration file for updated Job and Application models

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='recruiter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_jobs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='jobs.Job'),
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='application',
            name='cover_letter',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together={('user', 'job')},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-applied_date']},
        ),
    ]
