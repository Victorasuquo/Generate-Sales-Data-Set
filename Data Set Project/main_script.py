# i import the necessary modules
import random
import os
import csv
import datetime

# this class creates a new datafileand enables some manipulations 
class DataFile:
    datafile = ""
    
    def Create_file(self, datafile:str):
        """
        This method creates a 
        """
        self.datafile = datafile
        file = open(datafile, "w")
        file.close()
        print(f"{self.datafile}, Sucessfully created...")

    def GetFilePath(self):
        # self.filename = data_set_name
        try:
            location = os.path.abspath(self.datafile)
            print(location)
        except Exception as e:
            print(f"{self.datafile} cannot be found. Please specify another path\n{e}")

    def CheckFile(self, data_set_name = None):
        self.datafile = data_set_name

        try:
            exist = os.path.exists(self.datafile)
            print(f"the dataset {self.datafile} exist")
        except FileExistsError:
            print(f"The specified file: '{self.datafile}' cannot be found")  
        except Exception as e :
            print(f"an error occured\n{e}")          
    
    def viewFile(self):
        with  open(self.datafile, "r") as data_file:
            print(data_file.read())

class Generate(DataFile):
    frame_head = ["Invoice number", "Product Code", "Quantity", "Time", "Unit Prize"]
    row = 0

    def generate(self, datafile:str, row:int):
        self.row = row
        self.filename = datafile
        counter = 1
        with open (self.filename, "w+", newline= "") as data_file:
            data_writer = csv.writer(data_file)

            # write the headers of the data_set
            data_writer.writerow(self.frame_head)
            year = random.randint(1960, 2023)

            # Generate values for the rows
            while counter < self.row:
                invoice_number = random.randint(500000, 599999)

                code_list = [23008,21625,21985,20996,'72799E',22737,22483,22561,23356,21906,23437,23198,22980,21155,23000,21391,
                    22725,21169,23306,21876,22531,23150,22667,22423,22193,'84985A',23438,21126,'90214H',21945,84598,
                    21106,22090,22411,23321,22918,22960,22614,22774,]
                
                code = random.choice(code_list)
                quantity = random.randint(0, 35)
                date = random.randint(1, 31)
                month = random.randint(1, 12)
                hours = random.randint(0, 23)
                minutes = random.randint(0,59)
                seconds = random.randint(0,59)

                try:
                    real_time = datetime.datetime(year,month,date,hours,minutes,seconds)
                except ValueError:
                    pass

                units = random.uniform(0.1, 0.9)
                
                unit_price = (random.randint(1, 99)+units)
                
 
                data_writer.writerow([invoice_number, code,quantity, real_time, f"{unit_price:.2f}"])
                
                counter += 1


  
