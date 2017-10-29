import gzip
import shutil
with open('0.py', 'rb') as f_in:
    with gzip.open('0.py.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

with gzip.open('0.py.gz', 'rb') as f:
    file_content = f.read()
    print(file_content)
    print(gzip.compress(file_content))
