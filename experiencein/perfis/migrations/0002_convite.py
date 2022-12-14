# Generated by Django 2.2 on 2022-10-12 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_recebidos', to='perfis.Perfil')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_feitos', to='perfis.Perfil')),
            ],
        ),
    ]
