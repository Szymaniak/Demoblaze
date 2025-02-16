import csv



class DataReader:
    @staticmethod #metoda statyczna jest jedna, nie będzie tworzyło kopii.wielu obiektów
    def get_csv_data(filename):
        rows = []
        with open(filename, "r") as data_file:
            reader = csv.reader(data_file)
            next(reader,None) #pomin pierwszy wiersz
            for row in reader:
                rows.append(row)

        return rows
