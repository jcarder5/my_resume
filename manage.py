from flask_script import Manager
from songbase import app, db, Professor, Song

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    debra = Professor(name='Debra Dragone', about='Accounting')
    jackson = Professor(name='Jackson Gillespie', about='Accounting')
    song1 = Song(name='Yellow', year=2000, lyrics="Look at the stars", artist=debra)
    song2 = Song(name='Sugar', year=2014, lyrics="I'm hurting, baby, I'm broken down", artist=jackson)
    db.session.add(debra)
    db.session.add(jackson)
    db.session.add(song1)
    db.session.add(song2)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
