import datetime
import os


print ('Осторожно! Файлы в выбранном каталоге будут переименованы путём\
 добавления даты последнего изменения файла в начало имени файла.')
print('Введите путь к каталогу для переименования файлов:')
root = os.path.join(input())
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        source_name = os.path.join(directory, name)
        timestamp = os.path.getmtime(source_name)
        modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace\
                        (':', '.')
        target_name = os.path.join(directory, f'{modified_date}_{name}')

        print(f'Renaming: {source_name} to: {target_name}')

        os.rename(source_name, target_name)
