import zlib

data = b'abc'
print(zlib.adler32(data))
print(zlib.compress(data))
print(zlib.compressobj())
print(zlib.crc32(data))
print(zlib.decompress(zlib.compress(data)))
print(zlib.decompressobj())

c = zlib.compressobj()
print(c.compress(data))
print(c.flush())
#print(c.copy())#ValueError: Inconsistent stream state

d = zlib.decompressobj()
print(d.unused_data)
print(d.unconsumed_tail)
print(d.eof)
print(d.decompress(zlib.compress(data)))
print(d.flush())
#print(d.copy())#ValueError: Inconsistent stream state
print(zlib.ZLIB_VERSION)
print(zlib.ZLIB_RUNTIME_VERSION)

