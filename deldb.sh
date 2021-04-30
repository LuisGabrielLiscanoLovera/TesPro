rm empresa/migrations/00*
rm destajo/migrations/00*
rm casino/migrations/00*
rm integrante/migrations/00*
rm prenda/migrations/00*
rm referencia/migrations/00*
rm tarea/migrations/00*
rm db.sqlite3
cd TesPro\
python manage.py makemigrations
python manage.py migrate
