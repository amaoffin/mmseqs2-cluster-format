import csv
from collections import defaultdict

input_file = ""
output_file = ""
clusters = defaultdict(list)

with open(input_file, 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split('\t')
        if len(parts) >= 2:
            rep, prot = parts[0], parts[1]
            clusters[rep].append(prot)

sorted_clusters = sorted(clusters.items())

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i, (rep, proteins) in enumerate(sorted_clusters, start=1):
        writer.writerow([f"Cluster {i}"])
        writer.writerow(["Representative sequence", rep])
        for prot in proteins:
            if prot != rep:
                writer.writerow(["", prot])
        writer.writerow([])
