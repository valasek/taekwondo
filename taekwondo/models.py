from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Sex(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    deadline = models.DateField()
    fee = models.IntegerField()
    instructions_url = models.CharField(max_length=200)
    langlong = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Member(models.Model):
    itf_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Matsogi(models.Model):
    name = models.CharField(max_length=50)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tull(models.Model):
    name = models.CharField(max_length=50)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Wirok(models.Model):
    name = models.CharField(max_length=50)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tki(models.Model):
    name = models.CharField(max_length=50)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MemberCompetition(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    trainee = models.BooleanField()
    coach = models.BooleanField()
    matsogi = models.ForeignKey(Matsogi, on_delete=models.CASCADE)
    tull = models.ForeignKey(Tull, on_delete=models.CASCADE)
    wirok = models.ForeignKey(Wirok, on_delete=models.CASCADE)
    tki = models.ForeignKey(Tki, on_delete=models.CASCADE)


# class Users(models.Model):
#    __tablename__ = 'users'

    # Columns
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    first_name = models.CharField(max_length=50)
#    last_name = models.CharField(max_length=50)
#    email = db.Column(db.String(100))
#    pw_hash = db.Column(db.String(100))
#    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
#    is_admin = db.Column(db.Boolean)
