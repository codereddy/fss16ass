<h1>Daniel F. Schwarz, Inke R. König and Andreas Ziegler:<i>On safari to Random Jungle: a fast implementation of Random Forests for high-dimensional data</i>. doi:10.1093/bioinformatics/btq257</h1>

Cited by

<h2>Data mining in the Life Sciences with Random Forest: a walk in the park or lost in the jungle?
Wouter G. Touw, Jumamurat R. Bayjanov, Lex Overmars, Lennart Backus, Jos Boekhorst, Michiel Wels and Sacha A. F. T. van Hijum
 form) : 26th May 2012</h2>


<h3>The four most important keywords:</h3>
<ul>
<li>ii1 Gene-Gene Interaction
Also called epistasis is the effect of one gene on a disease modified by another gene or several other genes. It is a common component of genetic architecture of human complex diseases. Unfortunately it is difficult to detect. [http://link.springer.com/referenceworkentry/10.1007%2F978-1-4419-1005-9_690]</li>
<li>ii2 Single nucleotide polymorphisms (SNPs)
Is the most common type of genetic variation among people. A SNP represents a difference in a single DNA building block (nucleotid). If SNPs occur within a gene or in a regulatory region near a gene, it may play a more direct role in disease by affecting the gene’s function. [https://ghr.nlm.nih.gov/primer/genomicresearch/snp]
</li>
<li>ii3 variable backward elimination
It is an algorithm under which one starts with fitting a model with all the variables of interest and then the least significant variable is dropped, so long as it is not significant at our chosen critical level. We continue by successively re-fitting reduced models and applying the same rule until all remaining variables are statistically significant.  </li>
<li>ii4 Potential Pathway(Biological Pathway)
A biological pathway in genes is a series of actions among different genes that can turn turn genes on and off, trigger the assembly of new molecules, spur a cell to move, or result in a condition. </li></ul>


<h3>Brief Description</h3>
<ul><li>iii1  Motivational statements
Genome-wide association (GWA) studies are known to be successful to lighten the complexity of complex genetic diseases. Compared to other methods they propose a fast approach for this kind of studies</li>
<li>iii2  Hypotheses
They present the Random Jungle tool (which is a free source software), that implements the random forests algorithm, and performs Genome-wide association(GWA) analysis faster than the previous methods.</li>
<li>iii3  Checklists
Data for rheumatoid arthritis provided for the Genetic Analysis Workshop 15
</li><li>iii4  Related Work
1) Single marker analyses (McCarthy et al., 2008; Samani et al., 2007; Wellcome Trust Case Control Consortium, 2007) to identify locations of DNA sequence on the genes( called the loci). 2) Classifiers to identify SNPs for various disease by doing GWA studies for various diseases (Jakobsdottir et al., 2009). 
</li><li>iii5  Study instruments
They use Random Jungle, http://www.randomjungle.org. SUSE Linux operating system with a 2.33 GHz Intel dual quad-core processor (8 CPUs) and 16 GB memory
</li><li>iii6  Statistical tests
They use the free software Random Jungle, which implements random forests. This software makes different permutation importance measures available, it also includes additional options such as the backward elimination method. This software is used to identify the SNPs which form the potential pathways for various diseases, especially for Crohn’s disease.
</li><li>iii7  Commentary
Calculation with RJ can be parallelized using multithreading and MPI. RJ is written in C++. Software is freely available.
</li><li>iii8  Informative visualizations
 They use graphs in supplementary tables to show the features of Random Jungle software. The results - Gini importance, scaled permutation importance and unscaled permutation importance values were plotted against different SNPs. The computing times and memory usages of Random forests, Random Jungle and Random forest using FORTRAN were compared on a horizontal bar graph.
</li><li>iii9  Baseline results
The results are compared to the results they get by using Random Forest.
</li><li>iii10 Sampling procedures
They do not provide an explanation why they used the Crohn’s disease to do their analysis. 
</li><li>iii11 Patterns
Simulation study to make it comparable to studies with Random Forest. They selected one affected sibling per affected pair for the cases and one unaffected sibling per control family for the controls. Ranks of Gini and unscaled permutation importance scores were investigated. Each program was applied 500 times. Data was analyzed using default parameter. At the end importance ranks of the predictor variables were compared using boxplots.
Anti-Pattern- Random Jungle takes more memory on a multi-core processor than on a single-core processor. 
</li><li>iii12 Negative results
Not many negative results except that when running the Random Jungle software to perform random forests on a multi-core processor, it consumes more memory than when run on a single-core processor. This is because because helping data structures have to be provided for every core of the processor.
</li><li>iii13 Tutorial materials
They explain how random forest works, the meaning of importance, and the estimation of various VI measures. They also describe briefly the RJ Software. http://www.randomjungle.org
</li><li>iii14 New results 
Random Jungle software can be used to analyze the SNPs for genetic diseases instead of the RandomForest and Random Forest in Fortran because of its faster implementation and less memory usage
</li><li>iii15 Future work
RJ consumed more memory in the multiprocessor-version. RJ discovered also new pathways that should be validated.
</li><li>iii16 Data 
Dataset is from a Crohn's disease GWA study(Duerr et al., 2006)-Dataset contains data of 513 Crohn's disease affected Caucasian cases and 515 Caucasian controls were analyzed.
</li><li>iii17 Scripts
They used the novel software package RJ, which is written in C++. They used the default parameters. They didn’t use any special scipts.
</li><li>iii18 Sample models
The Random Jungle software package can be used to implement random forests instead of using randomForest or random forest in Fortran because it additionally implements the variable backward elimination. When multiple CPU are available, it is able to perform random forests on multiple CPUs simultaneously using multithreading and Message Passing Interface (MPI) parallelization. Hence it can be a very good implementation of random forests which can be used by even people outside the community.
</li><li>iii19 Delivery tools 
The Random Jungle package can be downloaded at http://www.randomjungle.org. They used the data that was brought to the Genetic Analysis Workshop 15</li></ul>

<h3>Improve paper</h3>
<ul>
<li>iv1 They do not explain how Random Jungle technically works(the data structure it uses to implement the random forests algorithm), not even briefly.
</li><li>iv2 Since Random Jungle should be just a faster algorithm than Random Forest, they lack in explaining why Random Jungle finds new pathways.
</li><li>iv3 The reason for using the crohn’s disease dataset is not clearly stated.
</li></ul>




