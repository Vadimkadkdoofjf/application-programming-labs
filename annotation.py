import csv
import os

def create(img_dir:str,csv_path:str):

    with open(csv_path,mode='w',newline='',encoding='utf-8') as annotation:
        writer = csv.writer(annotation)
        headers = ['re_path','abs_path']
        writer.writerow(headers)

        for file in os.listdir(img_dir):
            if file.endswith(("jpg","jpeg","png")):
                re_path = os.path.relpath(file,start=img_dir)
                abs_path = os.path.abspath(file)
                writer.writerow([re_path,abs_path])
            else:
                raise ValueError("This not image file")