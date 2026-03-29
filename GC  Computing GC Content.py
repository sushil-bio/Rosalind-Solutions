# The raw data we got from the problem
FASTA = """"""

# We need a dictionary to store the ID and the long DNA string
dna_codons = {}
key = ""

# Loop through each line one by one
for line in FASTA.splitlines():
    if line.startswith(">"):
        # This is a header line, so we save the name and start a blank string
        key = line[1:]
        dna_codons[key] = ""
    else:
        # This is a DNA sequence line, so we add it to the current ID
        dna_codons[key] = dna_codons[key] + line

# Variables to keep track of the highest GC content we find
highest_gc = 0.0
highest_id = ""

# Now we check every entry in our dictionary
for x in dna_codons:
    sequence = dna_codons[x]
    
    # Calculate GC content: (G + C) divided by total length
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_len = len(sequence)
    
    gc_value = (g_count + c_count) / total_len * 100
    
    # If this one is better than our previous best, update the "winner"
    if gc_value > highest_gc:
        highest_gc = gc_value
        highest_id = x

# Print the final results as requested
print(highest_id)
print(round(highest_gc, 6))

