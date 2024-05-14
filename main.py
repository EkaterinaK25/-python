import os
from pathlib import Path
import logging
from collections import namedtuple
import argparse

print(os.listdir())

FORMAT = '{asctime}: {levelname}\n{asctime}: {levelname}\n'
                    
logging.basicConfig(filename='history_log', filemode='w', format=FORMAT, level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

def dir_namedtuple():
    way_list = []
    сurrent_directory = Path(Path().cwd())
    Way = namedtuple('Way', ['name', 'extension', 'parent_div'])

    #dir_list = os.listdir()
    for dir_path, dir_name, file_name in os.walk(сurrent_directory):
        for obj_ext in file_name:
            name_extension = obj_ext.split('.')
            object = Way(name_extension[0], None if len(name_extension) == 1 else name_extension[1], dir_path.split('\\')[-1])
            way_list.append(object)
        
        for dirs in dir_name:
            object = Way(dirs, 'None', dir_path.split('\\')[-1])
            way_list.append(object)

    return way_list
                    


def parse_args():
    parser = argparse.ArgumentParser(description="First parser")
    parser.add_argument('path', metavar='N', type=str, help='Введите путь до директории на ПК', default=None, nargs='?')
    return parser.parse_args().path
