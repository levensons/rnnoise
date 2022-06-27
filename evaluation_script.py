from subprocess import call
import argparse
import os
from tqdm import tqdm

def main(noised_folder, denoised_folder):
    if not os.path.exists(denoised_folder):
        os.mkdir(denoised_folder)

    listdir = os.listdir(noised_folder)

    for i, filename in tqdm(enumerate(listdir), total=len(listdir)):
        file = os.path.join(noised_folder, filename)
        if os.path.isfile(file):
            denoised_file = os.path.join(denoised_folder, filename)
            call(["./examples/rnnoise_demo", file, denoised_file])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input and output folder')
    parser.add_argument('--noised_path', metavar='path', required=True,
                        help='the path to noised dataset')
    parser.add_argument('--denoised_path', metavar='path', required=True,
                        help='path to clean outputs')
    # parser.add_argument('--clean_path', metavar='path', required=False,
    #                     help='path to clean dataset')
    args = parser.parse_args()
    main(noised_folder=args.noised_path, denoised_folder=args.denoised_path)