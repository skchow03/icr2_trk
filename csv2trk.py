import sys
import csv
import numpy as np

if len(sys.argv) != 2:
    print("Usage: python csv2trk.py <TRK name>")
    sys.exit(1)

trk_name = sys.argv[1]

# Load header
with open(trk_name+'-1-header.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header line
    header = np.array(next(reader), dtype=np.int32)

# Load xsects
with open(trk_name+'-2-xsect_dlats.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header line
    xsects = np.array([row[1] for row in reader], dtype=np.int32)

# Load sect_offsets
with open(trk_name+'-3-sect_offsets.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header line
    sect_offsets = np.array([row[1] for row in reader], dtype=np.int32)
    sect_offsets = (sect_offsets * 4).tolist()

# Load xsect
with open(trk_name+'-4-xsect.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header line
    xsect_data = np.array([row[2:] for row in reader], dtype=np.int32).flatten()

# Load fsect-ground
with open(trk_name+'-5-fsect-ground.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header line
    fsects_data = np.array([row[1:] for row in reader], dtype=np.int32).flatten()

# Load sects_data
sects_data = []
with open(trk_name+'-6-sects_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header line
    for row in reader:
        sects_data.extend(row[1:])
sects_data = np.array(sects_data, dtype=np.int32)

# Merge all data
all_data = np.concatenate([header, xsects, sect_offsets, xsect_data, fsects_data, sects_data])

# Write to file
all_data.tofile(trk_name + '2.TRK', sep="")
