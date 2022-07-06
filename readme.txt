python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py startproject movies
python manage.py startapp register

python manage.py migrate 
python manage.py runserver

python3 manage.py makemigrations main
python3 manage.py sqlmigrate movies 0001
python3 manage.py sqlmigrate main
remember to after change to orm/db:
python manage.py migrate

python manage.py createsuperuser

super user: felix
email: felix@gmail.com
password: caladrius, i9#w3*3H

FirstPatient
password: FOXTROTpapa616




-----------------------------------------------------
create and Drop database; grant permission to user.
--------------------------------------->
DROP DATABASE caladrius_db;
DROP DATABASE caladriusDB;
CREATE DATABASE caladrius_db;
CREATE DATABASE caladriusDB;
FLUSH PRIVILEGES;
GRANT ALL ON caladrius_db.* TO felix@localhost;
GRANT ALL ON caladriusDB.* TO felix@localhost;
FLUSH PRIVILEGES;
----------------------------------------------------