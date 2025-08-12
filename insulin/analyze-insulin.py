import re

with open('/home/ec2-user/environment/data/preproinsulin-seq.txt') as f:
    raw_data = f.read()

# Hilangkan 'ORIGIN', angka, //, spasi, dan newline
clean_seq = re.sub(r'ORIGIN', '', raw_data)
clean_seq = re.sub(r'\d+', '', clean_seq)
clean_seq = clean_seq.replace('//', '')
clean_seq = clean_seq.replace('\n', '').replace(' ', '')

# Simpan hasil
with open("preproinsulin-seq-clean.txt", "w") as f:
    f.write(clean_seq)

print(len(clean_seq), clean_seq)

# Asumsikan clean_seq dari langkah sebelumnya
lsinsulin = clean_seq[0:24]
binsulin = clean_seq[24:54]
cinsulin = clean_seq[54:89]
ainsulin = clean_seq[89:110]

# Simpan ke file
with open("lsinsulin-seq-clean.txt", "w") as f: f.write(lsinsulin)
with open("binsulin-seq-clean.txt", "w") as f: f.write(binsulin)
with open("cinsulin-seq-clean.txt", "w") as f: f.write(cinsulin)
with open("ainsulin-seq-clean.txt", "w") as f: f.write(ainsulin)

print(len(lsinsulin), len(binsulin), len(cinsulin), len(ainsulin))
