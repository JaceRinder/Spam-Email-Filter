#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#Jace Rinder 
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
import numpy as np 
import matplotlib.pyplot as plt
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#Functions used to parse files and create the spam filter
def cleantext(text): 
    text = text.lower()
    text = text.strip()
    for letters in text: 
        if letters in """!.,"-@!#$%^&*()+/?""":
            text = text.replace(letters, " ")
    return text

def counter(text, is_spam, counted): 
    for each_word in words: 
        if each_word in counted: 
            if is_spam == 1: 
                counted[each_word][1] = counted[each_word][1] + 1
            else: 
                counted[each_word][0] = counted[each_word][0] + 1 
        else: 
            if is_spam == 1: 
                counted[each_word] = [0, 1]
            else: 
                counted[each_word] = [1, 0]
    return counted

def make_percent_list(k, theCount, spams, hams): 
    for each_key in theCount: 
        theCount[each_key][0] = (theCount[each_key][0] + k)/(2*k+hams)
        theCount[each_key][1] = (theCount[each_key][1] + k)/(2*k+spams)
    return theCount

def bayes(P_spam, P_ham, subject, vocab):
    s = 0
    s_n = 0
    for each_word in vocab: 
        if each_word in subject: 
            s_n = s_n + np.log(vocab[each_word][0])
            s = s + np.log(vocab[each_word][1])
        else: 
            s_n = s_n + np.log(1 - vocab[each_word][0])
            s = s + np.log(1 - vocab[each_word][1])
    s = np.power(np.e, s)
    s_n = np.power(np.e, s_n)
    classify = 1 / (1 + (s_n/s))
    return classify
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Specifier for how accurate the filter will be 
margin_of_error = 0.5
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Create the vocabulary based on the training set
spam = 0 
ham = 0 
counted = dict() 
training_file = input("Please enter the file name of the training set: ")
fin = open(training_file, "r", encoding = 'unicode-escape')
textline = fin.readline()
while textline != "": 
    is_spam = int(textline[:1])
    if is_spam == 1: 
        spam = spam + 1 
    else: 
        ham = ham + 1 
    textline = cleantext(textline[1:])
    words = textline.split()
    words = set(words)
    counted = counter(words, is_spam, counted)
    textline = fin.readline()
vocab = (make_percent_list(1, counted, spam, ham))

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Filter out the stopwords from the vocabulary
stopwords_file = input("Please enter the file name for the list of stop words: ")
fin = open(stopwords_file, "r", encoding = 'unicode-escape')
textline = fin.readline()
while textline != "": 
    textline = cleantext(textline)
    textline = textline.split('\n')[0]
    if textline in vocab: 
        vocab.pop(textline)
    textline = fin.readline()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Apply the vocabulary as a spam filter for the test set, using Bayes' Theorem
tp = 0
tn = 0
fp = 0
fn = 0
accuracy = 0
precision = 0
recall = 0
f1 = 0
spam_t = 0
ham_t = 0
P_spam = 0
P_ham = 0
testing_file = input("Please enter the file name of the test set: ")
fin = open(testing_file, "r", encoding = 'unicode-escape')
textline = fin.readline()
while textline != "": 
    is_spam = int(textline[:1])
    if is_spam == 1: 
        spam_t = spam_t + 1 
    else: 
        ham_t = ham_t + 1 
    textline = fin.readline()
fin.seek(0)
P_spam = spam_t/(ham_t + spam_t)
P_ham = ham_t/(ham_t + spam_t)
textline = fin.readline()

while textline != "": 
    is_spam = int(textline[:1])
    textline = cleantext(textline[1:])
    words = textline.split()
    words = set(words) 
    classify = bayes(P_spam, P_ham, words, vocab)
    if classify < margin_of_error: 
        if is_spam == 1: 
            fn = fn + 1
        else: 
            tn = tn + 1
    else: 
        if is_spam == 1:
            tp = tp + 1
        else: 
            fp = fp + 1
    textline = fin.readline()
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Calculating statistics for the results
accuracy = (tp + tn)/(tp + tn + fp + fn)
precision = tp/(tp + fp)
recall = tp/(tp + fn)
f1 = (1/((1/precision)+(1/recall))) * 2
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Final output
print("Number of Spam Emails: " + str(spam_t))
print("Number of Ham Emails: " + str(ham_t))
print("Number of False Positives: " + str(fp))
print("Number of True Positives: " + str(tp))
print("Number of False Negatives: " + str(fn))
print("Number of True Negatives: " + str(tn))
print("Accuracy: " + str(accuracy))
print("Precision: " + str(precision))
print("Recall: " + str(recall))
print("F1: " + str(f1))
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
