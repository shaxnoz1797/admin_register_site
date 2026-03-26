from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


# faculty
def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * from adminapp_faculty""")
        faculties = dictfetchall(cursor)
        return faculties

# kafedra
def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * from adminapp_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra


# groups
def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * from adminapp_groups""")
        groups = dictfetchall(cursor)
        return groups


# students
def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * from adminapp_students""")
        students = dictfetchall(cursor)
        return students


# subject
def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * from adminapp_subject""")
        subject = dictfetchall(cursor)
        return subject


# teachers
def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * from adminapp_teachers""")
        teachers = dictfetchall(cursor)
        return teachers