import tempfile
import os
f = tempfile.NamedTemporaryFile(delete=False)
print(f.name)
f.write(b"Hello World!\n")
f.close()
print(os.unlink(f.name))
print(os.path.exists(f.name))

