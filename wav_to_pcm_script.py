import pydub
import argparse
import os
from tqdm import tqdm

def main(path_from, path_to, wav_to_pcm):
    if not os.path.exists(path_to):
        os.mkdir(path_to)
    listdir = os.listdir(path_from)

    if wav_to_pcm:
        to_format = 'raw'
    else:
        to_format = 'wav'

    for i, filename in tqdm(enumerate(listdir), total=len(listdir)):
        file_to = os.path.splitext(os.path.join(path_to, filename))[0]
        file_from = os.path.join(path_from, filename)
        if os.path.isfile(file_from):
            with open(file_from, 'rb') as f, open(file_to, 'wb') as fo:
                fo.write(pydub.AudioSegment(f).export(format=to_format).read())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input and output folder')
    parser.add_argument('--path_from', metavar='path', required=True,
                        help='the path to noised dataset')
    parser.add_argument('--path_to', metavar='path', required=True,
                        help='path to clean dataset')
    parser.add_argument('--wav_to_pcm', nargs='?', required=False, const=1, type=bool)
    args = parser.parse_args()
    main(path_from=args.path_from, path_to=args.path_to, wav_to_pcm=args.wav_to_pcm)