import os
from Iterator import iterator
import get_way
import shutil

#копирование в другую директорию
def copy_to_another(class_name):
    count = iterator()
    while (count.num!=1020):
        if (os.path.isfile(get_way.get_absolute_way(class_name, count.num, "download")) == True ):
            shutil.copyfile(get_way.get_absolute_way(class_name, count.num, "download"), get_way.get_absolute_way(class_name, count.num, "changed"))
        next(count)


def main():
        print("Начало")
        if not os.path.isdir("dataset/changed_dataset"):
            os.makedirs("dataset/changed_dataset")
        class_name = "cat"
        copy_to_another(class_name)
        class_name = "dog"
        copy_to_another(class_name)
        print("Конец")
    
if __name__ == "__main__":
        main()