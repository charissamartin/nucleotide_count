string = "CCATGAGGTGCGAAACAGTAAACCCGTGATCACTTCATTGTCAAGCAGCAAAGGAGAATCGGACAGTGAGCCTCAGGATTGTTTAGCATAATATTATGGCGTACATTCTCAAGGATTACAGTCCGGTCAGGACCCGAATAACCGGATGGCCTAATGCCTATCCTGTGTTTAGTGAAAGGTTTGGAACGGAAGCAGCGGACCATTATTAGGATGTTTGTGCGGATTGCTTGATGCTTCATGTTGATTCTAAGCCGAATTGGATCTACGCTTGCGAGTGGATACATCTCACTTCGGAGGGATTTCGAGGAGCTCTAGTCGAGGCCCACTTGGTGGCAGGTTCGTCATATAGGCATCTTCCGGGGTGATTGCGCCGGCATATGCATATGGTTCCTCGTATATCTGCCAGAGATTTTCGGGGTATGTTGTCTTACACAGCGGGACGTACCACGATAGTTGGGAATAACTCGTGAGTCCATGGCTCGGGTATGTCCCCCTGAGTTCTGATTCCTATAAATCCGCTGTAGCGCCCAGCATCGAAGCAATATAGGAGCAAGCCTATCTATTCATCTTCCACGGGGCATGAATCCTTACAGATGGCATTGCTGCGTCCGCCTATAGCTAACAAGTTATAGGACATATCCTTCCCTACATACCTTATGCCCATATCTTTAGGGGCTGAAATGCTCTTCAATATTTCAATCTTCCAATCTCGAGTTCCACCGTTTCTTAGACGTTGCATTGACTACGTTGAGTAGGCTCGTGTCACTGACGGACAGTGCCCGCGTAACTCTTGTGGTGATTCTGTAGACCTACTCTGCCTTGTACCAAATCCAAAGATGAGATACAATGACGTTCACTAGAGACGCATCGGGAATTGTTCCACTGAGCCATGCAAAGTTTAAGTCATCAGGGCGCTGAATAGACGTAACTCCCGGTTACTGCTAAATCTGGAAGCGCATCCCGGCGAACAACAGGGGAG"
a_count = 0
t_count = 0
c_count = 0
g_count = 0 
for i in string:
    if i == 'A':
        a_count+=1
    if i == 'T':
        t_count+=1
    if i == 'C':
        c_count+=1
    if i == 'G':
        g_count+=1
print(a_count)
print(c_count)
print(g_count)
print(t_count)