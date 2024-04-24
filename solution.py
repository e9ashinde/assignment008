#Q1
def number_words(filename):
    with open(filename,"r") as f:
        data=f.read()
        data.replace(",", " ")
        return len(data.split(" "))
print(number_words("/home/sierra/repository/assignment008/log.txt"))

#Q2
#2.1
from zipfile import ZipFile
def read_zipfiles(filename):
    with ZipFile(filename,'r') as zip:
        zip.printdir()
        print('Reading all the files')
        zip.extractall()
    return 'done'
print(read_zipfiles("/home/sierra/repository/assignment008/test_data.zip"))

#2.2
extracted_dir="extracted_files"
def read_files(filename):
    with ZipFile(filename,'r') as zip:
        files=zip.namelist()
        hra_files = [file for file in files if 'HRA' in file]
        for i in hra_files:
            zip.extract(i,extracted_dir)
print(read_files("/home/sierra/repository/assignment008/test_data.zip"))

#2.3
import zipfile
import csv
with zipfile.ZipFile('/home/sierra/repository/assignment008/test_data.zip', 'r') as zip_ref:
    hra_files = [f for f in zip_ref.namelist() if 'HRA' in f]
    with open('hra_resultant_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for hra_file in hra_files:
            with zip_ref.open(hra_file, 'r') as file:
                for line in file:
                    writer.writerow(line.decode().strip().split(','))
print("Processing completed.")

#Q3
import csv
task_2_output = []
with open("/home/sierra/repository/assignment008/hra_resultant_data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        selected_row = {"Age": row["Age"],"Gender": row["Gender"],
                       "JobRole": row["JobRole"]}
        task_2_output.append(selected_row)
with open("job_roles.csv", "w", newline="") as csvfile:
    fieldnames = ["Age", "Gender", "JobRole"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in task_2_output:
        writer.writerow(entry)

#Q4
with zipfile.ZipFile("job_roles.zip", "w") as zip_ref:
    zip_ref.write("/home/sierra/repository/assignment008/job_roles.csv")


#Q5
def display_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]
            for line in last_n_lines:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
# def main():
#     file_path = input("Enter the path of the file: ")
#     n = int(input("Enter the number of last lines to display: "))
#     display_last_n_lines(file_path, n)
# if __name__ == "__main__":
#     main()

#Q6
def count_word(filename,xword):
    with open(filename,"r") as f:
        data=f.read()
        cnt=data.count(xword)
        return cnt
print(count_word("/home/sierra/repository/assignment008/job_roles.csv","Female"))
            
#Q7
from PIL import Image 
filepath = "/home/sierra/repository/assignment008/1E9AdvisorsHome.png"
img = Image.open(filepath)
width, height = img.size
print(f"The dimensions of the image are:{width} x {height}")

#Q8
def main():
    with open("/home/sierra/repository/assignment008/log.txt", "a") as log_file:
        while True:
            text = input("Enter text (or type 'exit' to quit): ")
            if text.lower() == "exit":
                break
            log_file.write(text + "\n")
            print("Text written to log.txt successfully.")
if __name__ == "__main__":
    main()










