import csv
import os
from Iterator import iterator
import get_way


def create_annotation(subdir):
    with open("annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";")
        file_writer.writerow(["Абсолютный путь", "Относительный путь", "Класс"])
        count=iterator()
        while ( count.num != 1020 ) :
            if (os.path.isfile(get_way.get_absolute_way(subdir, count.num, "download")) == True ):
                file_writer.writerow([get_way.get_absolute_way(subdir, count.num, "download"), get_way.relative_way_dataset(subdir, count.num), subdir])
            next(count)
        
    
def main():
        print("Начало")
        subdir = "cat"
        create_annotation(subdir)
        subdir = "dog"
        create_annotation(subdir)
        print("Конец")
    
    
if __name__ == "__main__":
        main()