# Generated by Django 4.1 on 2022-12-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationresponse',
            name='children_count',
            field=models.SmallIntegerField(default=0, verbose_name='Antal barn'),
        ),
        migrations.AlterField(
            model_name='invitationresponse',
            name='diet',
            field=models.TextField(blank=True, verbose_name='Specialkost'),
        ),
        migrations.AlterField(
            model_name='invitationresponse',
            name='is_partying',
            field=models.CharField(blank=True, choices=[('yes', 'Ja!'), ('no', 'Nej, jag/vi deltar endast vid ceremonin')], max_length=4, verbose_name='Stannar ni till middagen?'),
        ),
        migrations.AlterField(
            model_name='invitationresponse',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='invitationresponse',
            name='note',
            field=models.TextField(blank=True, verbose_name='Övrig kommentar'),
        ),
        migrations.AlterField(
            model_name='invitationresponse',
            name='people_count',
            field=models.SmallIntegerField(default=0, verbose_name='Antal personer'),
        ),
        migrations.AlterField(
            model_name='invitationresponse',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='Kvittens skickad'),
        ),
    ]
