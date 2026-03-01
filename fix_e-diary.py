from datacenter.models import Schoolkid, Mark, Lesson, Subject, Chastisement, Commendation
import random


def fix_points(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])

    for mark in marks:
        mark.points = 5
        mark.save()

    return f"Исправлено {marks.count()} оценок"


def remove_chastisement(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()
    return f'Удалил {chastisements.count()} замечаний'


def create_commendation(schoolkid, lesson):
    list_of_commendations = [
        ' Молодец!',
        ' Отлично!',
        ' Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        ' Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        ' Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!'
    ]

    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid)
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                             group_letter=schoolkid.group_letter,
                                             subject__title=lesson).first()

    commendation = random.choice(list_of_commendations)
    Commendation.objects.create(schoolkid=schoolkid,
                                subject=lesson.subject,
                                teacher=lesson.teacher,
                                text=commendation,
                                created=lesson.date)
    return f'Добавил похвалу по предмету {lesson} для {schoolkid}'