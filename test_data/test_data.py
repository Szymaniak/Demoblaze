import csv



class DataReader:
    @staticmethod #metoda statyczna jest jedna, nie będzie tworzyło kopii.wielu obiektów
    def get_csv_data(filename):
        rows = []
        data_file = open(filename, "r")
        reader = csv.reader(data_file)
        next(reader,None) #pomin pierwszy wiersz
        for row in reader:
            rows.append(row)

        return rows
