import os

#функция возвращая путь из dataset скаченной картинки
def relative_way_dataset(subdir, number):
    return f"dataset/{subdir}/{str(number).zfill(4)}.jpg"


#относительный путь для 2 скрипта
def relative_way_changed(subdir, number):
    return f"dataset/changed_dataset/{subdir}_{str(number).zfill(4)}.jpg"


#относительный путь для рандомного
def relative_way_random(number):
    return f"dataset/random_dataset/{str(number).zfill(4)}.jpg"



def get_absolute_way(name_class, number, function):
    if function == "download":
        return os.path.abspath(relative_way_dataset(name_class, number))
    if function == "changed":
        return os.path.abspath(relative_way_changed(name_class, number))
    if function == "random":
        return os.path.abspath(relative_way_random(number))