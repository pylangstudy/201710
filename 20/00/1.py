import shutil

shutil.make_archive('a.txt', 'zip')
shutil.unpack_archive('a.txt.zip', 'a')
print(shutil.get_archive_formats())
#shutil.register_archive_format(name, function[, extra_args[, description]])
#shutil.unregister_archive_format(name)
#shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])
#shutil.unregister_unpack_format(name)
print(shutil.get_unpack_formats())

