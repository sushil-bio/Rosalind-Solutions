def calculate_possible_rna(protein_string):
    # A dictionary mapping each amino acid to the number of RNA codons that encode it
    codon_frequencies = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 
        'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 
        'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2
    }
    
    # We start our total at 1 (for multiplication)
    total_rna_strings = 1
    modulo_value = 1000000
    
    # Multiply the running total by the number of possible codons for each amino acid
    for amino_acid in protein_string:
        total_rna_strings = total_rna_strings * codon_frequencies[amino_acid]
        # Apply the modulo at every step to keep the number small
        total_rna_strings = total_rna_strings % modulo_value
        
    # Finally, multiply by the 3 possible stop codons at the end
    total_rna_strings = total_rna_strings * 3
    total_rna_strings = total_rna_strings % modulo_value
    
    return total_rna_strings

# Example using a tiny protein string: Methionine, Alanine
sample_protein = "MNYLADEKDCMCDTGEDNYIKRDLGETCSWYMLTVLRHCFTYSLGQSLLDMAEKRYAERIDIYRTSGKDANLQQNSAGQHIGIFIHNTQKQCIPNYLTDYMRGNSFLGELKHHAPWDDDCCTSSCEYFEEHILWALQEMIAPTRYSPVTYVIFIAMRCNFQCLFVAWPGVIIREDWVTCKITDEGWQSATCVAWWMYEWNTHACYVSDTEQYNQTDVLHPVPVCEEINVDDIPWSPPVYDYEICDKTWSEDNWNNAMCFIIRNEWNIMKFNPLDNWPDKTKRWGHETAPEKHLFNDVETVGTDQIVWLAIMPIKMHANDGCKSNMNWSNEADQVNDDNCSFPFGCSVQSDCYSSHCQLCWFRFMPCKIQLFACWAAFIRQMAWYLPWPTVYSVICMTGTKGRQDIVGFTAHHMDVYEHFDPMMPKTAWLERWTEKDGCFHVNVFKWEGGFKGAFRVNRFKSASGPSKIVPNWPAKFKKQIFMFIHFMARQQHTIRYDSDPLTCVLHDNVGSCLHEDYMAGDPCSSYRWITYPNDQMNNGFSETTDRMSYPDGYERAYKYHYQFQGESQIEKWADQYFKPLYNPCHNYDHPLYTNKKEINCMNKMNPGKHHWKCLHGQRPLIMFWDCMSFYRGMPVKYQGHMDPHRHVKFDHAHYTKGAWSQCKHANYTQFCWNMNFAFEYLDCCPQMQPICVHFRPAMLADQPFCLGNLFHYSHIFQIFGYQVERIFPHYTHRIWTINHDRWKCSCPLQDKAWIMGWYSRWSIAIPHPARNVRMHTESLMKWDRFDPNIQHNCKCQSGGKISYNSNRITTVMTEWAWSKLWTVVTLDLTGVALEFDYCGHPVFLPGMVFVTHTWKSARMNIAFIKNCQFVLNLKCTTITDWPHNNKELSVVPVNWSVEICPTFFWSEKTYTIHEINFPWLAAGIAHGIHKIIMDIMAYTWHPNERPWGPYCVSAQIKEYGRCFKKCDFMNVQGLLTCLQNINTMPVDSPFCCKGHTWYYH"
# Math check: M(1) * A(4) * Stop(3) = 12 possible RNA strings
print(f"Total possible RNA strings: {calculate_possible_rna(sample_protein)}")