from os import walk

def import_folder(path):

    for info in walk(path):
        print(info)

import_folder("../graphics/character/run")