# Generated by Django 3.2.9 on 2022-04-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GeoCodeBD', '0001_initial'),
        ('user_entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='permanent_district',
            field=models.ForeignKey(db_column='permanent_district', on_delete=django.db.models.deletion.DO_NOTHING, to='GeoCodeBD.district'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='permanent_division',
            field=models.ForeignKey(db_column='permanent_division', on_delete=django.db.models.deletion.DO_NOTHING, to='GeoCodeBD.division'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='permanent_post_office',
            field=models.ForeignKey(blank=True, db_column='permanent_post_office', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='GeoCodeBD.union'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='permanent_thana',
            field=models.ForeignKey(db_column='permanent_thana', on_delete=django.db.models.deletion.DO_NOTHING, to='GeoCodeBD.upazila'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='present_district',
            field=models.ForeignKey(db_column='present_district', on_delete=django.db.models.deletion.DO_NOTHING, related_name='present_district', to='GeoCodeBD.district'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='present_division',
            field=models.ForeignKey(db_column='present_division', on_delete=django.db.models.deletion.DO_NOTHING, related_name='present_division', to='GeoCodeBD.division'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='present_post_office',
            field=models.ForeignKey(blank=True, db_column='present_post_office', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='present_post_office', to='GeoCodeBD.union'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='present_thana',
            field=models.ForeignKey(db_column='present_thana', on_delete=django.db.models.deletion.DO_NOTHING, related_name='present_thana', to='GeoCodeBD.upazila'),
        ),
    ]