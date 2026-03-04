from datacenter.models import Schoolkid, Mark, Lesson, Subject, Chastisement, Commendation
import random


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        return f'Ученик {schoolkid_name} не найден'


def fix_points(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)
    return f"Исправлены оценки для {schoolkid_name}"


def remove_chastisement(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    Chastisement.objects.filter(schoolkid=schoolkid).delete()
    return f'Удалены замечания для {schoolkid_name}'


def create_commendation(schoolkid_name, lesson_title):
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

    schoolkid = get_schoolkid(schoolkid_name)

    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=lesson_title
    ).first()
    
    if not lesson:
        return f'Урок {lesson_title} не найден'

    commendation = random.choice(commendations)
    Commendation.objects.create(
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
        text=commendation,
        created=lesson.date
    )

    return f'Добавил похвалу по предмету {lesson.subject} для {schoolkid_name}'
