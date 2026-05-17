import random

import time

from datacenter import modelds


def find_schoolkid(schoolkid_name):
    schoolkid = []
    schoolkid = Schoolkid.objects.filter(full_name__contains = schoolkid_name)
    if schoolkid.count() >= 2:
        print("Найдено несколько результатов. Уточните имя.")
    elif schoolkid.count() < 1:
        print("Ученик не найден.")
    else:
        print("Ученик найден.")
        schoolkid = schoolkid.first()
    return schoolkid


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid = schoolkid,
                                    points__in = ['2', '3'])
    print("Нахождение и изменение оценок...")
    if bad_marks.count() >= 1:
        time.sleep(random.randint(2, 5))
        Mark.objects.filter(schoolkid = schoolkid,
                            points__in = ['2', '3']).update(points = '5')
        print("Оценки изменены.")
    else:
        print("Нет плохих оценок.")


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid = schoolkid)
    if chastisements.count() >= 1:
        print("Нахождение и удаление замечаний...")
        time.sleep(random.randint(2, 5))
        Chastisement.objects.filter(schoolkid = schoolkid).delete()
        print("Все замечания удалены.")
    else:
        print("Нет замечаний.")


def create_commendation(schoolkid, subject):
    lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                    group_letter=schoolkid.group_letter,
                                    subject__title__contains=subject)
    if lessons:
        random_lesson = random.choice(lessons)
        Commendation.objects.create(text=random.choice(commendations),
                                    created=random_lesson.date,
                                    schoolkid=schoolkid,
                                    subject=random_lesson.subject,
                                    teacher=random_lesson.teacher)
    else:
        print("Урок не найден")
        return


def main():
    commendations=["лев просто",
                   "прям молодой эйнштейн",
                   "вот руку пожал бы", "красавчик",
                   "научился думать",
                   "впервые чото умное сказал"]


if __name__ == "__main__":
    main()
