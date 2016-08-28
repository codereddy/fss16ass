Data mining in the Life Sciences with Random Forest: a walk in the park or lost in the jungle?
Wouter G. Touw, Jumamurat R. Bayjanov, Lex Overmars, Lennart Backus, Jos Boekhorst, Michiel Wels and Sacha A. F. T. van Hijum
 form) : 26th May 2012

The four most important keywords:
ii1 Random Forest
Random Forest is a machine learning technique. At training time the algorithm develops a forest of decision trees. The mode of the classes is the output.

ii2 Curse Of Dimensionality
Is a term that describes the fast increasing of a volumina while adding more dimensions. Data sets in life science normally have a lot more variables than samples. The number of parameters in life sience you have to consider is very large.

ii3 Local Variable Importance
It's the importance of a variable for a single sample. Local variables that have a certain importance for a subset of all samples can be important for classifying, even though they weren't considered as an important global variable.

ii4 Variable Interactions
Interactions between variables can cause an effect, respectively variables can sometimes become important when they interact with other variables, in particular in life science.

Brief Description
iii1  Motivational statements
In life sciences much data is collected and analyzed. The variables often interfere with each other. With Random Forest it's possible to take those interactions to account.
iii2  Hypotheses
Random Forest can extract the interactions and so enable a good insight.
iii3  Checklists
The base of the Random Forest is built upon a data matrix which consists of examples that belong to two classes and measurements of each sample. A bootstrap set is created, variables are randomly chosen and evaluated.
iii4  Related Work
There are links that show that Random Forest is discussed in a broad scientific context.
iii5  Study instruments
Random Forest
iii6  Statistical tests
variable-related information, proximity between examples, relationships and variable interactions
iii7  Commentary
They recommend the 'randomForest' Package, but considering the performance also 'Random Jungle'. There are some other implementations that suite the kind of data of life sciences
iii8  Informative visualizations
They use table summaries, and few figures
iii9  Baseline results
With Random Forest it is possible to extract additional knowledge, as well as local importances, proximity and interactions. 
iii10 Sampling procedures
It is not clear, which data they use or where exactly it comes from
iii11 Patterns
Develop a Random Forest and analyze it
iii12 Negative results
iii13 Tutorial materials
They explain how Random Forest works and describe the speciality of life sciences
iii14 New results 
They propose the Random Forest as good choice especially because of the interactions that can be analyzed
iii15 Future work
iii16 Data 
Much Life science data of different kinds.
iii17 Scripts
They have no deeper insight, which implementation they use.
iii18 Sample models
iii19 Delivery tools 

Improve paper
iv1 There is no detailed description of the data
iv2 There is no detailed description of the algorithms they use
iv3 They could use a visualization of their results
iv4 They do not compare their results with other related works.



