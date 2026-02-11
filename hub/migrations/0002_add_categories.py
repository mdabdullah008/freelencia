from django.db import migrations

def create_categories(apps, schema_editor):
    Category = apps.get_model('hub', 'Category')
    categories = [
        'Programming and Tech',
        'Graphics and Design',
        'Video and Animation',
        'Business',
    ]
    for cat in categories:
        Category.objects.create(name=cat)

class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]
