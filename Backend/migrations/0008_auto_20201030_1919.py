# Generated by Django 3.1.2 on 2020-10-30 16:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_auto_20201030_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.IntegerField(verbose_name='ID животного')),
                ('createdAt', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('first_name_order', models.CharField(max_length=100, verbose_name='Имя')),
                ('second_name_order', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic_name_order', models.CharField(max_length=100, verbose_name='Отчество')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='status_animal',
            field=models.CharField(choices=[('avaible', 'Готов к социализации'), ('unavaible', 'Не готов к социализации')], default='', max_length=100, verbose_name='Готовность к социализации'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='color_animal',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('black', 'Черная'), ('white', 'Белая'), ('brown', 'Коричневая'), ('grey', 'Серая'), ('redhead', 'Рыжая'), ('striped', 'Полосатая'), ('spotted', 'Пятнистая')], max_length=1000, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='gender_animal',
            field=models.CharField(choices=[('boy', 'Мальчик'), ('girl', 'Девочка')], max_length=7, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='type_color_animal',
            field=models.CharField(choices=[('monochrome', 'Монотонная'), ('multicolor', 'Многоцветная')], max_length=10, verbose_name='Тип окраса'),
        ),
    ]