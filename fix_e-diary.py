from datacenter.models import Schoolkid, Mark, Lesson, Subject, Chastisement, Commendation
import random


def catch_error(schoolkid):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid)
        return schoolkid
    except Schoolkid.DoesNotExist:
        return f'Ученик {schoolkid} не найден'


def fix_points(schoolkid):
    schoolkid = catch_error(schoolkid)
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)
    return f"Исправлены оценки для {schoolkid}"


def remove_chastisement(schoolkid):
    schoolkid = catch_error(schoolkid)
    Chastisement.objects.filter(schoolkid=schoolkid).delete()
    return f'Удалены замечания для {schoolkid}'


def create_commendation(schoolkid, lesson):
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!'
    ]

    schoolkid = catch_error(schoolkid)
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=lesson
    ).first()

    if not lesson:
        return f'Урок {lesson} не найден'

    commendation = random.choice(commendations)

    Commendation.objects.create(
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
        text=commendation,
        created=lesson.date
    )

    return f'Добавил похвалу по предмету {lesson.subject} для {schoolkid}'


