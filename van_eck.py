import sys
if len(sys.argv) < 2:
	print("Please specify a length!")
	exit()
seq = [0, 0]
seq_len = int(sys.argv[1])
for i in range(2, seq_len):
	if seq[-1] in seq[:-1]:
		indices = [i for i, x in enumerate(seq) if x == seq[-1]]
		largest_index = indices[-2]
		dist = (len(seq) - 1) - largest_index
		seq.append(dist)
	else:
		seq.append(0)

van_eck_index = 0
for n in seq:
	van_eck_index += 1
	print(str(van_eck_index) + ": " + str(n))
