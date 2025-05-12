from glob import glob
import fileinput
import os

def load_file(input_directory: str):
    files = glob(f'{input_directory}/*')
    with fileinput.input(files = files) as f:
        sequence = [(input_directory.split('/')[3], line) for line in f]
    return sequence

def create_ouptput_directory(output_directory: str):
    if os.path.exists(output_directory):
        for file in glob(f'{output_directory}/*'):
            os.remove(file)
        os.rmdir(output_directory)
    os.makedirs(output_directory)