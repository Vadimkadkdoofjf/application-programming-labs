import argparse
from downloader import download
from iterator import Iterator
from annotation import create

def create_parser():
   parser = argparse.ArgumentParser()
   parser.add_argument("keyword",type=str,help="keyword to search images")
   parser.add_argument("number",type=int,help="number of images")
   parser.add_argument("img_dir",type=str,help="path to the folder,where images will be downloaded")
   parser.add_argument("annotation_file",type=str,help="path to the annotation file")
   args = parser.parse_args()
   return args.keyword,args.number,args.img_dir,args.annotation_file

def main():
   keyword, number, img_dir, annotation_file = create_parser()
   try:
      download(keyword, number, img_dir)
      create(img_dir, annotation_file)
      iterator = Iterator(annotation_file)
      for i in iterator:
         print(i)
   except Exception as e:
      print(f"Something went wrong: {e} ")

if __name__ == '__main__':
   main()

