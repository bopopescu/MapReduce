# Generated by Django 2.1.2 on 2018-11-07 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computadorstatus',
            name='id_pc',
        ),
        migrations.RemoveField(
            model_name='pilhaprocessos',
            name='id_computador',
        ),
        migrations.RemoveField(
            model_name='pilhaprocessos',
            name='id_tarefa',
        ),
        migrations.RemoveField(
            model_name='tarefapalavras',
            name='id_tarefa',
        ),
        migrations.DeleteModel(
            name='computador',
        ),
        migrations.DeleteModel(
            name='computadorstatus',
        ),
        migrations.DeleteModel(
            name='pilhaprocessos',
        ),
        migrations.DeleteModel(
            name='tarefa',
        ),
        migrations.DeleteModel(
            name='tarefapalavras',
        ),
    ]
