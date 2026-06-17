import hashlib

i = 0
done = []
p1 = ''
p2 = [0,0,0,0,0,0,0,0]
while len(done) < 8:
    hash2 = hashlib.md5(f'ojvtpuvg{i}'.encode("utf-8")).hexdigest()
    if hash2.startswith("00000"):
        if len(p1) < 8:
            p1 += hash2[5]
        if hash2[5].isnumeric() and int(hash2[5]) < 8 and hash2[5] not in done:
            p2[int(hash2[5])] = hash2[6]
            done.append(hash2[5])
    i += 1

print(p1)
print(''.join(p2))
