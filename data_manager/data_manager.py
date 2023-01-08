import csv

csv_file_1 = "csv_data/clean_measure.csv"
csv_file_2 = "csv_data/clean_stations.csv"

class DataManager:
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def get_from_csv(self, ):
        with open(self.csv_file_name)as file: 
            csvFile = csv.reader(file, delimiter=',') 
            data_read = [row for row in csvFile]
            return data_read

data_manager1 = DataManager(csv_file_name=csv_file_1)
data_manager2 = DataManager(csv_file_name=csv_file_2)



