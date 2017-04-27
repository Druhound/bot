import csv


def parsing(file):
    first = True
    header = None
    obj = []
    with open('/home/druhound/virtualprojects/source/bot/data/' + file, 'r') as f:
        csv_file = csv.reader(f, delimiter=str(';'))
        for line in csv_file:
            if first:
                header = line
                first = False
            else:
                obj.append(dict(zip(header, line)))
    return obj, header
