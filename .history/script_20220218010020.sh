#!/bin/bash
rm -rf acumulado/__pycache__ && rm -rf acumulado/migrations/__pycache__ $$ rm -rf acumulado/migrations/000*
rm -rf authapp/__pycache__ && rm -rf authapp/migrations/__pycache__ $$ rm -rf authapp/migrations/000*
rm -rf casino/__pycache__ && rm -rf casino/migrations/__pycache__ $$ rm -rf casino/migrations/000*
rm -rf despacho/__pycache__ && rm -rf despacho/migrations/__pycache__ $$ rm -rf despacho/migrations/000*
rm -rf color/__pycache__ && rm -rf color/migrations/__pycache__ $$ rm -rf color/migrations/000*
rm -rf destajo/__pycache__ && rm -rf destajo/migrations/__pycache__ $$ rm -rf destajo/migrations/000*
rm -rf empresa/__pycache__ && rm -rf empresa/migrations/__pycache__ $$ rm -rf empresa/migrations/000*
rm -rf home/__pycache__ && rm -rf home/migrations/__pycache__ $$ rm -rf home/migrations/000*
rm -rf integrante/__pycache__ && rm -rf integrante/migrations/__pycache__ $$ rm -rf integrante/migrations/000*
rm -rf patinador/__pycache__ && rm -rf patinador/migrations/__pycache__ $$ rm -rf patinador/migrations/000*
rm -rf prenda/__pycache__ && rm -rf prenda/migrations/__pycache__ $$ rm -rf prenda/migrations/000*
rm -rf referencia/__pycache__ && rm -rf referencia/migrations/__pycache__ $$ rm -rf referencia/migrations/000*
rm -rf segimientoOp/__pycache__ && rm -rf segimientoOp/migrations/__pycache__ $$ rm -rf segimientoOp/migrations/000*
rm -rf tarea/__pycache__ && rm -rf tarea/migrations/__pycache__ $$ rm -rf tarea/migrations/000*
rm -rf xtarea/__pycache__ && rm -rf xtarea/migrations/__pycache__ $$ rm -rf xtarea/migrations/000*
rm -rf db.sqlite3
python manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver


