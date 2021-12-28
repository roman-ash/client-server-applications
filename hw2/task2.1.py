import csv


def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    r_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in files:
        with open(file, encoding='windows-1251') as f:
            data = f.read().split('\n')
            for i in data:
                row_data = i.split(':')
                if r_data[0][0] in row_data[0]:
                    os_prod_list.append(row_data[1].strip())
                if r_data[0][1] in row_data[0]:
                    os_name_list.append(row_data[1].strip())
                if r_data[0][2] in row_data[0]:
                    os_code_list.append(row_data[1].strip())
                if r_data[0][3] in row_data[0]:
                    os_type_list.append(row_data[1].strip())
            r_data.append(
                [
                    os_prod_list[:1][0],
                    os_name_list[:1][0],
                    os_code_list[:1][0],
                    os_type_list[:1][0]
                ]
            )
    return r_data


def write_to_csv(file):
    with open(file, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        print(get_data())
        for row in get_data():
            csv_writer.writerow(row)


write_to_csv('csv_file.csv')
