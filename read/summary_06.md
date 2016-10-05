Reading 4
<a href="http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7008118">http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7008118</a>
<h1>
  Multiple Instance Learning for Breast Cancer 
  Magnetic Resonance Imaging.<br>Maken, McClymont & Bradley <br>  
</h1>


The above paper cited this:

<h2>Data mining in the Life Sciences with Random Forest: a walk in the park or lost in the jungle?
Wouter G. Touw, Jumamurat R. Bayjanov, Lex Overmars, Lennart Backus, Jos Boekhorst, Michiel Wels and Sacha A. F. T. van Hijum
 form) : 26th May 2012</h2>

<h3>The four most important keywords:</h3>
<ul>
<li>ii1  Multiple Instance Learning l(MIL): is a variation of supervised learning. The learner receives not single instances but bags. Those are labeled positive if at least one instance of its subset is positive and negative if all instances of its subset are negative.
</li><li>ii2 Citation-kNN: Adaption from the normal kNN to MIL. A distance function between bags is added. Citation-kNN then predicts the lagel of a bag taking the k neighbours and the citers of the bag into concern.
</li><li>ii3 Tile-based features: A subimage is seen taken like one bag of feature vector, which are extracted from one individual tile. Due to the size, classification performance is not affected by the accuracy of the segmented regions.
</li><li>ii4 Region-of-interest (ROI) based features: A ROI is a part of samples that have been specially selected due to a specifc purpose. In this paper, based on the data each lesion becomes a labelled instance in the dataset. The features extracted from each lesion are then  individually  labelled  as either  benign  (negative)  or  malignant  (positive) (s. I Instruction)
</li></ul>

<h3>Brief Description</h3>
<ul><li>iii1 Motivational Statement:
They want to test the ability of MIL in the use for magnetic resonance images (mri), they want to compare it to the normal kNN or Random Forest methods. 
</li><li> iii2 Informative visualizations:
They use bar charts and line charts, always with visualized standard deviation.
</li><li> iii3 Data:
MRI data,  165  clinical  bilateral  breast  MRI  investigations  of  150  subjects.
</li><li> iii4 Baseline results: The results show that citation-kNN works better than tile-based kNN. The performance of ckNN is the same as ROI-based SIL. They say ckNN is a suitable choice, in addition they figured out that it could be used as screening tool under certain circumstances.
</li></ul>

<h3>Improve paper</h3>
<ul><li>iv1 They don't mention related work
</li><li> iv2 They don't show any example pictures
</li><li> iv3 The discussion part is really huge.
</li><li> iv4 They don't deliver tutorial materials, the do not explain their techniques, only very briefly.
</li></ul>
