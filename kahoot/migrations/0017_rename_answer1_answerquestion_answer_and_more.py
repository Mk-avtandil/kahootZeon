# Generated by Django 4.1 on 2022-09-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kahoot", "0016_remove_answerquestion_point_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answerquestion", old_name="answer1", new_name="answer",
        ),
        migrations.RemoveField(model_name="answerquestion", name="answer2",),
        migrations.RemoveField(model_name="answerquestion", name="answer3",),
        migrations.RemoveField(model_name="answerquestion", name="answer4",),
        migrations.RemoveField(model_name="answerquestion", name="correct_answer",),
        migrations.AddField(
            model_name="answerquestion",
            name="is_correct",
            field=models.BooleanField(default=False),
        ),
    ]
