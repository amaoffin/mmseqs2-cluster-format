mmseqs2-cluster-format

Does what it says on the tin! Analyzing the clusters in the original format got a bit hard to read after a while, so I wrote some simple scripts to format them in a more readable way. This takes in mmseqs results and outputs it as a csv with clusters organized with either:

a) the representative sequence separate (format_repsequence.py)
    | Cluster N               |        |
    | Representative sequence | XXXXXX |
    |                         | XXXXXX |
    |                         | XXXXXX |
b) on the same line (format_sameline.py)
    | Cluster N       | 
    | XXXXXX (repseq) | 
    | XXXXXX          |
    | XXXXXX          |
