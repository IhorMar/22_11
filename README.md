# 22_11

Додано: 
requirements.txt

demo_data.json, який створюється командою: 
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > demo_data.json

І він містить записи що наявні в базі даних.

У файлі views ми бачимо кілька вюшок, вони показують як працює респонс, в тому числі бачимо що в нас міститься в request.
