import fileinput
with fileinput.input(files=('spam.txt', 'eggs.txt')) as f:
    for line in f:
        print(line, end='')

print(fileinput.filename())
print(fileinput.fileno())
print(fileinput.lineno())
print(fileinput.filelineno())
print(fileinput.isfirstline())
print(fileinput.isstdin())
print(fileinput.nextfile())
print(fileinput.close())

with fileinput.FileInput(files=('spam.txt', 'eggs.txt')) as input:
    print(input)

with fileinput.FileInput(files=('spam.txt', 'eggs.txt'), openhook=fileinput.hook_compressed) as input:
    print(input)

with fileinput.FileInput(openhook=fileinput.hook_encoded("utf-8", "surrogateescape")) as input:
    print(input)

