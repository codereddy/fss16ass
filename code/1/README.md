eg0:
grep is used to find a string inside a certain file. In eg0 it is used to echo all attributes.
cat prints out the file, gawk -F, 'NF==5' shrinks the output to those lines with 5parts separated by ','; sort sorts alphabetically; column -s -t gives a table representation of the output.
j4810 is a decision tree learner. It tries to find subsets of a set that are less mixed. It measures then the entropy, if the entropy is over a threshold it continues recursively, otherwise it stops. para is a function, that replaces line breaks.

eg1
for eg1 see the cat-part in eg0

eg2
for eg2 see the j4810 part in eg0 now in addition with line numbers

eg3
Using j48 as decision tree learner. But uses twice the same training data

eg4
first prints out "j48 weather". then calls eg3 and shortens the output of eg3 to show only "actual" and "predicted". But since eg3 uses the same data twice you will always get the same answer in one line (always yes;yes or no;no).

eg5
the result is now split into the two classes "yes" and "no". Since we use the same data, our accuracy, probability of detection & precision are all 100% and the probability of a false alarm is 0% (abcd are the true|false positives|negatives).

eg6
uses the two learners j48 and jrip on the same training data. eg6 uses crossvalidation. It runs 3 times with j48 and 3 times with jrip. Every time the set is divided into 3 parts of equal size. 2 parts are used to train and the left part is to validate.
Stratified means that each subset has about the same distribution. I cannot see any method that ensures that.

eg7
does a 5x5 crossvalidation using j48 and jrip and produces two files. One includes the pd, the other the pf in that form: <learner> <value> for each round.

eg8
makes the eg7 files more readable, named columns mean use names instead of numbers so you can better work with it.

eg9
reports the results of pd and pf which are calculated by eg8.
It compares the two learners for pd & pf.
Separating the report from the execution means separation model and view. The reporting things don't have to operate on the training / test data, just on the produced output, and there they just read and do not manipulate anything.

eg10
j48: uses the C4.5 decision tree. The decision about how far away from the root a vertex is, is made by entropy. After the first decision, it continues recursively until a threshold is reached.

nb - NBTree: uses Bayes classification (leaves) and decision tree classification. Uses attributes and recursively uses first the attribute with the highest utility. if not higher than utility_current take a Bayes classifier.


