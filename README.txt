Spam Email Filter

Jace Rinder 

Overview: 
 This project is designed to filter spam emails using Bayes' Therom. First, the program constructs a suitable vocabulary from a training set of data that is comprised of email
 subject lines. It takes in a list of 'stop words,' which are some of the most common words of the given language, and excludes them from the vocabulary. Then, it applies the 
 statistical probabilities it has found and applies them to a test set of email subjects. The size ratio of training and testing set should ideally be 80/20 respectively. From
 there, the program prints out the estimated number of spam/ham emails as well as the statistical values of accuracy, precision, recall, F1 score, false/true positives, and 
 false/true negatives. 
 
How to use: 
 To use the project, store the 'spamFilter.py' file in a local directory alongside the training, testing, and stopwords sets. From there, when the user runs the python program
 they will be prompted to enter the names of training, testing, and stopwords sets. After entering these filenames, the results will be printed to the command line. 
 
