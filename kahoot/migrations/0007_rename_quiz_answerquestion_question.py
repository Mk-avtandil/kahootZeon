# Generated by Django 4.1 on 2022-09-07 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kahoot", "0006_question_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answerquestion", old_name="quiz", new_name="question",
        ),
    ]