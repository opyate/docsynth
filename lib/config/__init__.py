import glob

def config(args):
    """
    Loads runtime config from args and elsewhere.
    """
    config = {}

    # fonts
    if args.fonts:
        fontpaths = args.fonts
        fonts = []
        for path in fontpaths.split(' '):
            for filename in glob.iglob('{}/**/*.otf'.format(path), recursive=True):
                fonts.append(filename)
        config['fonts'] = fonts

    return config
