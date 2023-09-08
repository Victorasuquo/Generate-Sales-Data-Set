# test script/ usage

from main_script import DataFile , Generate

data_set_name = "sales_data_set.csv"
data_set = DataFile() 
# create an object of the datafile class
data_set.Create_file(data_set_name) # create data file
data_set.CheckFile(data_set_name) # checks if the file path exists
data_set.GetFilePath() # finds and returns the location of the datafile
data_set.viewFile() # prints the content of the file
print(data_set.datafile)  # print the name of the data file

Generate_data = Generate()
# creating an object of the Generate Class
print(Generate_data.datafile)
Generate_data.generate(data_set_name, 500)
data_set.viewFile()  # prints the content of the data file 
