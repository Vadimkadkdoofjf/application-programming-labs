import argparse


from image import *
from histogtam import *


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_image",type= str,help="path to default image")
    parser.add_argument("output_image",type=str,help="path to the new image")
    args =parser.parse_args()
    return args.input_image,args.output_image

def main():
    input_image,output_image = create_parser()
    try:
        image = input_image
        img = read_img(image)
        print_h_w(img)
        show(img)

        r_hist,g_hist,b_hist = create_hist(img)
        draw(r_hist,g_hist,b_hist)

        inverted_img = inverted(img)
        show(inverted_img)
        save(inverted_img,output_image)

    except Exception as e:
        print(e)
if __name__ == '__main__':
    main()
