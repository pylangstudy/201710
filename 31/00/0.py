import bz2
import shutil
with open('0.py', 'rb') as f_in:
    with bz2.open('0.py.bz2', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

with bz2.open('0.py.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)
    print(bz2.compress(file_content))
