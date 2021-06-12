# Generated by Django 3.2.4 on 2021-06-11 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0005_auto_20210611_1237'),
        ('gigs', '0002_auto_20210611_1237'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='gig',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gigs.gig'),
        ),
        migrations.AddField(
            model_name='comment',
            name='release',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='artists.release'),
        ),
        migrations.AddField(
            model_name='comment',
            name='track',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='artists.track'),
        ),
        migrations.AddField(
            model_name='comment',
            name='venue',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gigs.venue'),
        ),
    ]