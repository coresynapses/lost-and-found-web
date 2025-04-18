# Generated by Django 5.1.7 on 2025-03-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfound', '0006_alter_claimrequestreport_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item'},
        ),
        migrations.AlterField(
            model_name='claimrequestreport',
            name='contactInfo',
            field=models.CharField(default='', max_length=255, verbose_name='Contact Information'),
        ),
        migrations.AlterField(
            model_name='claimrequestreport',
            name='proofOfOwnership',
            field=models.TextField(default='', verbose_name='Proof of Ownership'),
        ),
        migrations.AlterField(
            model_name='fraudclaimreport',
            name='contactInfo',
            field=models.CharField(default='', max_length=255, verbose_name='Contact Information'),
        ),
        migrations.AlterField(
            model_name='fraudclaimreport',
            name='proofOfOwnership',
            field=models.TextField(default='', verbose_name='Proof of Ownership'),
        ),
        migrations.AlterField(
            model_name='item',
            name='contactInfo',
            field=models.CharField(default='', max_length=255, verbose_name='Contact Information'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemName',
            field=models.CharField(default='', max_length=255, verbose_name='Item Name'),
        ),
    ]
