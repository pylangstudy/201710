import glob
print(glob.glob('./[0-9].*'))
print(glob.glob('*.py'))
print(glob.glob('?.py'))
print(glob.glob('**/*.py', recursive=True))
print(glob.glob('./**/', recursive=True))
