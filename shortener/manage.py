# shortener/manage.py

from flask.cli import FlaskGroup
from app import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)
db.create_all(app=create_app())

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
