
library(dplyr)
library(stringr)
library(tidyr)
library(tidytext)
library(wordcloud)
library(textstem)
library(igraph)
library(ggraph)
library(gridExtra)
library(stm)
library(tm)


#Import data on cybersecurity patent documents submitted to the USPTO in recent years (a sample)
#In text mining parlance, this will be our "corpus" and the individual patent documents within it 
#will be our "documents"

cybersecurity.raw.data=read.csv("C:/Users/MSI-NB/Documents/R Studio/Raw data/Metamorphosis Raw Data (2).csv")

#What are column names and data dimension?
names(cybersecurity.raw.data)
dim(cybersecurity.raw.data)

#Let's view the text of the first (Fitbit) patent (US20160154952A1)
cybersecurity.raw.data$Claims[cybersecurity.raw.data$Publication.Number=="US20160154952A1"]

#Let's clean the data by removing numbers, punctuation, etc.

cybersecurity=cybersecurity.raw.data%>%

              #Put everything to lower case
              mutate(lc=str_to_lower(Text, locale = "en"))%>%
              
              select(-Text)%>%
              
              #Remove web links
              mutate(spec.no.web=str_replace_all(lc,"\\bwww.[[:alnum:]]+.[[:alnum:]]+\\b|\\bhttp://[[:alnum:]]+.[[:alnum:]]+\\b|\\bhttps://[[:alnum:]]+.[[:alnum:]]+\\b|[[:graph:]]+.com\\b|[[:graph:]]+.org\\b|[[:graph:]]+.edu\\b|[[:graph:]]+.gov\\b|[[:graph:]]+.net\\b"," "))%>%
              
              select(-lc)%>%
              
              #Strip common patenting-related words
              mutate(spec.strip.words=str_replace_all(spec.no.web,
                                                      
                                                      "\\bcompris[[:alpha:]]*\\b|\\bclaim[[:alpha:]]*\\b|\\bmethod[[:alpha:]]*\\b|\\bsystem[[:alpha:]]*\\b|\\binvent[[:alpha:]]*\\b|\\bpatent[[:alpha:]]*\\b|\\bapplication[[:alpha:]]*\\b|\\bfig[[:alpha:]]*\\b|\\bfigure[[:alpha:]]*\\b|\\bdrawing[[:alpha:]]*\\b|\\bexhibit[[:alpha:]]*\\b|\\bembodiment[[:alpha:]]*\\b|\\bassignee[[:alpha:]]*\\b|\\bprior art\\b|\\bcross reference[[:alpha:]]*\\b|\\bsystem and method\\b|\\bsystems and methods\\b|\\bwhat is claimed\\b|\\bfield of invention\\b|\\bfield of the invention\\b|\\bbackground art\\b|\\bbackground of the invention\\b|\\bbackground of invention\\b|\\bsummary of the invention\\b|\\bsummary of invention\\b|\\bsummary\\b|\\bbrief description of the drawings\\b|\\bbrief description of drawings\\b|\\buser[[:alpha:]]*\\b|\\brelated art\\b|\\bi\\b|\\bwe\\b|\\bart\\b|\\bskilled in the art\\b|\\bdetailed description\\b", " "))%>%
              
              select(-spec.no.web)%>%
              
              #Strip punctuation
              mutate(spec.no.punct=str_replace_all(spec.strip.words,"[[:punct:]]"," "))%>%
              
              select(-spec.strip.words)%>%
              
              #Strip isolated numbers and numbers that are followed by a letter either immediately or after a blank (e.g. 1A or 3 C)
              mutate(spec.no.numb=str_replace_all(spec.no.punct,"\\b[[:digit:]]+\\b|\\b[[:digit:]]+[[:blank:]]*[[:alpha:]]{1}\\b"," "))%>%
              
              select(-spec.no.punct)%>%
              
              #Strip roman numerals
              mutate(spec.no.roman=str_replace_all(spec.no.numb, "\\b[i,v,x]+\\b" ," "))%>%
              
              select(-spec.no.numb)%>%
              
              #Suppress some special signs that are not getting dropped with punct
              mutate(spec.no.signs=str_replace_all(spec.no.roman,"<|>|="," "))%>%
              
              select(-spec.no.roman)%>%
              
             
              #Suppress extra blanks into a single blank
              mutate(spec.no.blank=str_replace_all(spec.no.signs,"[[:blank:]]+"," "))%>%
              
              select(-spec.no.signs)%>%
              
              
              #Strip word version of Greek letters
              mutate(strip.greek=str_replace_all(spec.no.blank,
                                                 
                                                 "\\balpha\\b|\\bbeta\\b|\\bgamma\\b|\\bdelta\\b|\\bepsilon\\b|\\bupsilon\\b|\\bzeta\\b|\\beta\\b|\\btheta\\b|\\biota\\b|\\bkappa\\b|\\blambda\\b|\\bmu\\b|\\bnu\\b|\\bxi\\b|\\bomicron\\b|\\bpi\\b|\\brho\\b|\\bsigma\\b|\\btau\\b|\\bphi\\b|\\bchi\\b|\\bpsi\\b|\\bomega\\b", " "))%>%
              
              select(-spec.no.blank)%>%
              
              
              #Strip all single alphabetical characters
              mutate(strip.single.char=str_replace_all(strip.greek, "\\b[[:alpha:]]{1}\\b", " "))%>%
              
              select(-strip.greek)%>%
              
              
              #Suppress extra blanks into a single blank
              mutate(clean.text.w.stopw=str_replace_all(strip.single.char,"[[:blank:]]+"," "))%>%
              
              select(-strip.single.char)

#Let's view the cleaned text of the Fitbit Patent (US20160154952A1)
cybersecurity$clean.text.w.stopw[cybersecurity$Publication.Number=="US20160154952A1"]

#Let us represent each document as a list of all the words that are in that document. 
#This way we map the document to a sequence of words that comprise the document. 
#This is called "tokenization". After running the code below, view resulting "cybersecurity.tok" dataset
#to see the results. Note, how the document that had 1,410 rows quickly became a document
#with 1,557,848 rows!

cybersecurity.tok=cybersecurity%>%
                       unnest_tokens(output=word,input=clean.text.w.stopw, token="words")


#Let's view the vector of words corresponding to the Fitbit Patent (US20160154952A1)
View(cybersecurity.tok[cybersecurity.tok$Publication.Number=="US20160154952A1",])
  
#We can see that each document is now represented as a sequence of words that are present in the
#document, but we see that many of those words are articles such as "a", "the"; auxiliary 
#verbs such as "is", "are", etc.; prepositions such as "at", "in", etc. These are called
#"stop words" in text mining. We are going to get rid of them. We will use the dataset
#called "stop_words" that is part of the "tidytext" package, to identify and remove stop words
#in each document. Note how the 1,557,848 rows shrank to 781,464 rows!

#First, let's view the "stop_words" dataset
View(stop_words)

#And now, let's get rid of the stop words from our corpus
cybersecurity.tok.no.stopw=cybersecurity.tok%>%
                              anti_join(stop_words)


#Let's view the Fitbit Patent vector without stop words (US20160154952A1)
View(cybersecurity.tok.no.stopw[cybersecurity.tok.no.stopw$Publication.Number=="US20160154952A1",])


#Notice that in our vocabulary of words many words can have the 
#same stem, e.g. the irreducible part to which inflectional affixes (e.g. "-ing", "-ion", etc.) then get added to
#form words. Examples are "detecting", "detected"; "detective", etc. would need to shrink to "detect"
#Or, "accept", "acceptance", "acceptability", etc. We will reduce each such word to its
#"stem" i.e. to its irreducible part to which inflectional affixes get added to form words. 

cybersecurity.stemmed=cybersecurity.tok.no.stopw%>% 
  mutate(stemmed=stem_words(word))

#How many unique terms are there in our cleaned sample of 1,410 documents?
#Those unique terms comprise the "vocabulary" of our data
length(unique(cybersecurity.stemmed$stemmed))

#How many terms (rounded) are there on average in a cleaned document?
num.words.per.doc=cybersecurity.stemmed%>%group_by(Publication.Number)%>%tally()
mean(num.words.per.doc$n)

#Now that the text corpus is cleaned, let's see some of the common terms appearing
#in it. We will use a special type of a visualization that is called a "wordcloud". The size
#of each term will be proportional to the number of times it appears in the corpus.
#Note, that inside the wordcloud function there is a parameter set at 30
#Change as needed.

par(mar=c(0,0,0,0))

cybersecurity.stemmed%>%count(stemmed)%>%with(wordcloud(stemmed,n, max.words=30))

#what if we actually need to recreate this wordcloud but instead of individual words
#we want consecutive 2-word expressions that appear the most often? Those
#consecutive word expressions are called "bigrams" in text mining.

#Run lines from 164 to 185 below by highlighting and running at once.
#Only using expressions that appear more than 300 times!
#For viewing, click on Zoom under plots

set.seed(2019)
cybersecurity.graph=cybersecurity%>%
unnest_tokens(bigram,clean.text.w.stopw, token="ngrams", n=2)%>%
separate(bigram, c("word1", "word2"), sep=" ")%>%
filter(!word1 %in% stop_words$word)%>%
filter(!word2 %in% stop_words$word)%>%
mutate(stemmed.word1=stem_words(word1))%>%  
mutate(stemmed.word2=stem_words(word2))%>%    

#Note, that on the second line below we are filtering only on bigrams appearing
#more than 300 times. Change that parameter as needed.
  
count(stemmed.word1, stemmed.word2, sort=TRUE)%>%
filter(n>2)%>%
graph_from_data_frame()
a <- grid::arrow(type = "closed", length = unit(.15, "inches"))
ggraph(cybersecurity.graph, layout = "fr") +
  geom_edge_link(aes(edge_alpha = n), show.legend = FALSE,
                 arrow = a, end_cap = circle(.07, 'inches')) +
  geom_node_point(color = "lightblue", size = 5) +
  geom_node_text(aes(label = name), vjust = 1, hjust = 1) +
  theme_void()


#Let's save the last data frame, since we will be using it in the next lectures

#save(cybersecurity.stemmed, file="C:/Users/MSI-NB/Documents/R Studio/Raw data/metamorphosis.stemmed.csv")
write.csv(cybersecurity.stemmed, file = "C:/Users/MSI-NB/Documents/R Studio/Raw data/metamorphosis.stemmed.csv", row.names = FALSE)


#What if we want to compare 2 patent documents to see how they differ?
#One convenient type of a visualization is the "comparison cloud".
#Let's say we want to compare the Fitbit application (US20160154952A1) 
#with Google patent on social networks (US7716140B1).

counts=cybersecurity.stemmed%>%group_by(Publication.Number, stemmed)%>%count()
for.comp.cloud=counts%>%filter(Publication.Number %in% c("US20160154952A1", "US7716140B1"))
tdm.for.cloud=for.comp.cloud%>%cast_tdm(Publication.Number, stemmed, n)
tdm.mat=t(as.matrix(tdm.for.cloud))
comparison.cloud(tdm.mat, max.words=50, title.bg.colors = "white", title.size = 1.5)


#So comparison cloud is a type of a visualization that shows how the words appearing in a given number of documents
#compare to each other in terms of their frequency of appearance.

#But what if we want to compare how specific a given word (or words) are to a
#given document COMPARED TO THE REST OF THE CORPUS?

#So it would be nice to have a numeric metric to quantify how specific a word
#is for a given document, relative to the rest of the corpus. The word frequency by itself won't be a sufficient metric
#since a word may appear very frequently in a document but that word can be a very common
#word across the corpus. Examples are the stop words,which we removed. But even
#among the non-stop words, there are a number of words that are very common in all the
#patent documents. Thus the frequency by itself does not tell us how specific a word is to a given document.

#A popular metric is the term frequency - inverse document frequency (often referred to as "tf-idf")
#which weights the term frequency by the inverse of the proportion of documents in which that term appears
#If a word appears in every document of the corpus then tf-idf is 0. If the word appears
#many times in a given document and only in a given document, then its tf-idf is going to be relatively large,
#compared to a word that appears throughout the corpus.

#Below is a user-defined function that takes as an argument the
#publication number of a patent document and returns a bar chart of the
#10 words with highest tf-idf values. I.e. for any document we can see the most
#document-specific terms, that can indicate what the document is "about" relative
#to the rest of the corpus.

tf.idf.tbl=counts %>%
  bind_tf_idf(stemmed, Publication.Number, n)%>%
  group_by(Publication.Number)%>%
  arrange(desc(tf_idf), .by_group = TRUE)%>%
  top_n(10)

plot_tf_idf<-function(pubnum){
  tf.idf.doc=tf.idf.tbl%>%filter(Publication.Number==pubnum)%>%
    mutate(stemmed = reorder(stemmed, tf_idf))
  
par(mar=c(4,7,3,1))  
barplot(tf.idf.doc$tf_idf~tf.idf.doc$stemmed, horiz=TRUE, las=2, ylab="", xlim=c(0,max(tf.idf.doc$tf_idf)+0.1), main=pubnum, xlab="Tf-idf")
  
}

#Try a few documents, by passing their publication numbers within the double quotes
#in the function below. To try: US7716140B1, US20160154952A1.
#NOTICE: how the word "information" in US7716140B1 is not in top 10
#even though it appeared with a very large size on the comparison cloud. 
#Similarly, word "device" for US20160154952A1 doesn't appear among top terms with tf-idf


plot_tf_idf("US7716140B1")


#Acknowledgement: Some code and material in this program was adopted from:

#"Text Mining with R: A Tidy Approach" textbook by Julia Silge and David Robinson, O'Reilly (2017)
#https://www.tidytextmining.com/ 

#https://juliasilge.com/blog/sherlock-holmes-stm/
