Dutilh, Bas E., et al. "FACIL: fast and accurate genetic code inference and logo." Bioinformatics 27.14 (2011): 1929-1933.

Cited by

Data mining in the Life Sciences with Random Forest: a walk in the park or lost in the jungle?
Wouter G. Touw, Jumamurat R. Bayjanov, Lex Overmars, Lennart Backus, Jos Boekhorst, Michiel Wels and Sacha A. F. T. van Hijum
 form) : 26th May 2012


The four most important keywords:
ii1 Codon
A sequence of three nucleotides which form a specific amino acid. You find codons in the DNA, mRNA and tRNA. The three nucleotides form a code.
ii2 FACIL
Means Fast and Accurate Genetic Code Inference and Logo. It's the tool they present in their paper to evaluate nucleic acid sequences for their genetic code that detects alternative codes even in species distantly related to known organisms.
ii3 Homology-based
Proteins that are evolutionarily related to each other have similar structures. Proteins are in addition are better conserved than amino acid structures. 
ii4 Globobulimina pseudospinescens
Is a single-celled organism, it is a inhabitant of the sea.

Brief Description
iii1  Motivational statements
The stepping up in sequencing DNA will reveal a lot of genetic code.
iii2  Hypotheses
Their tool FACIL will valuate nucleic acid sequences fast and reliably.
iii3  Checklists
5866 annotated DNA sequences including 3269 bacterial, 176 archael and 2421 organellar genomes.
iii4  Related Work
Gendecoder: encodes another aspect about DNA.
iii5  Study instruments
They use Random Forest, the randomForest R package version 2.11.0 was used
iii6  Statistical tests
They use Random Forest
iii7  Commentary
After the prepocessing of the input DNA sequence, they do a homology-based prediction for each codon and then let the Random Forest work.
iii8  Informative visualizations
      They use table summaries, and some figures
iii9  Baseline results
FACIL is a fast and reliable tool and detects alternative genetic code, especially if the examined species aren't close related to known ones.
iii10 Sampling procedures
Randomly selecting 1000 regions of different lengths (all x10^x). Used three Random Forests, each containing 100 trees.
iii11 Patterns
The three steps are described in iii7
iii12 Negative results
The homology-based prediction caused a very low precision (24%) for stop codons.
iii13 Tutorial materials
They don't use much explanations on a basics level how there algorithm works. But it is sufficient if you are on an intermediate level.
iii14 New results 
they relay only on general protein domains, no explicit or implicit phylogenetic relatedness used.
iii15 Future work
future genetic work will "benefit from a more phylogenetically balanced selection of reference sequences, a proper model of evolution and a probabilistic phylogenetic method" they wrote.
iii16 Data 
5866 annotated DNA sequences including 3269 bacterial, 176 archael and 2421 organellar genomes. 
iii17 Scripts
randomForest R package version 2.11.0
iii18 Sample models
iii19 Delivery tools 
http://www.cmbi.ru.nl/FACIL/input/complete_training_table.txt.gz.

Improve paper
iv1 they do not clearly show their results and their negative points
iv2 they give no information about the Globobulimina pseudospinescens regarding their design decision.
iv3 Paper is difficult to understand if you are not used to all biology terms.
iv4 There is no discussion why they used that randomForest R package.



