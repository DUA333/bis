# Generated by Django 4.1.3 on 2023-09-22 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nbheures', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nbvieux', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('idEnsei', models.AutoField(primary_key=True, serialize=False)),
                ('nomEnsei', models.CharField(max_length=100)),
                ('prenomEnsei', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('idEtud', models.AutoField(primary_key=True, serialize=False)),
                ('nomEtud', models.CharField(max_length=100)),
                ('prenomEtud', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('motdepasse', models.CharField(max_length=100)),
                ('Filiere', models.CharField(max_length=100)),
                ('Wilaya', models.CharField(max_length=100)),
                ('cours_completes', models.ManyToManyField(blank=True, related_name='etudiants_completes', to='api.cours')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cours')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Favori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cours')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='favoris',
            field=models.ManyToManyField(related_name='etudiants_favoris', through='api.Favori', to='api.cours'),
        ),
        migrations.AddField(
            model_name='cours',
            name='enseignant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.enseignant'),
        ),
        migrations.AddField(
            model_name='cours',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.matiere'),
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField()),
                ('date_commentaire', models.DateTimeField(auto_now_add=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='api.cours')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.etudiant')),
            ],
        ),
    ]
