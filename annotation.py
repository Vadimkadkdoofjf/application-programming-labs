import csv
import os

def create(image_dir:str,csv_path:str):

    with open(csv_path,mode='w',newline='',encoding='utf-8') as annotation:
        writer = csv.writer(annotation)
        headers = ['re_path','abs_path']
        writer.writerow(headers)

        for file in os.listdir(image_dir):
            if file.endswith(("jpg","jpeg","png")):
                re_path = os.path.relpath(os.path.join(image_dir, file), start=os.path.dirname(csv_path))
                abs_path = os.path.abspath(os.path.join(image_dir, file))
                writer.writerow([re_path,abs_path])
            else:
                raise ValueError("This not image file")