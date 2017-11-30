

possible_dupes = [size for size in images if len(images[size]) > 1]
for size in possible_dupes:
    hashes = defaultdict(list)
    for fname in images[size]:
        m = md5.new()
        hashes[ m.update( file(fname,'rb').read(10000) ).digest() ] = fname
    for k in hashes:
       if len(hashes[k]) <= 1: continue
       for fname in hashes[k][1:]:
           print(fname)
