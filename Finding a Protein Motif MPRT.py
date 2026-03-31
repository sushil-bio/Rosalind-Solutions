import requests

# Read protein IDs from file
with open("rosalind_mprt.txt", "r") as file:
    ids = file.read().strip().split('\n')

# Process each protein ID
for protein_id in ids:
    
    #Extract base ID for URL
    base_id = protein_id.split('_')[0]
    
    #  Download the protein sequence
    url = "https://rest.uniprot.org/uniprotkb/" + base_id + ".fasta"
    response = requests.get(url)
    lines = response.text.strip().split('\n')
    
    #Remove the first description line
    sequence = ''.join(lines[1:])
    
    # Slide through the sequence
    matches = []
    for i in range(len(sequence) - 3):
        a = sequence[i]
        b = sequence[i+1]
        c = sequence[i+2]
        d = sequence[i+3]
        
        # Check motif N{P}[ST]{P}
        if a == 'N':
            if b != 'P':
                if c == 'S' or c == 'T':
                    if d != 'P':
                        matches.append(i + 1)
    
    #Print result
    if matches:
        print(protein_id)
        print(' '.join(map(str, matches)))
