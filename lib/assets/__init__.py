import os
import glob
import random

# this module only returns strings, e.g. paths to things (e.g. prefab texts, fonts)

prefab_text_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'prefabs', 'text')
prefab_text_paths = glob.glob(prefab_text_path + '/*.png')

def get_random_prefab_text():
    return random.choice(prefab_text_paths)


prefab_font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts')
prefab_font_paths = glob.glob(prefab_font_path + '/*.otf')

def get_random_font():
    return random.choice(prefab_font_paths)
