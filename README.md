# Latent Dirichlet Allocation of Yu-Gi-Oh card text

## Introduction

In this project, we aimed to apply Term Frequency Inverse Document Frequency (TF-IDF) on various corpuses of Yu-Gi-Oh trading card text, as well as create a Latent Dirichlet Allocation (LDA) Model to categorize the cards into different groups. 

Yu-Gi-Oh is a collectible card game made and developed in Japan. The game has over 10,000 cards in its database and includes many different mechanics and card types. The cards are mainly split into 3 categories: monsters, spells, and trap cards. However, each topic has their own specific sub-group and effects. With the amount of cards and effects within the game, interaction in the game requires players to know a vast amount of information about certain cards and their effects. 

For this project, we wanted to test how effectively we could search for cards based on certain keywords using TF-IDF and if we could find any meaningful relationships between cards using LDA.

## Resources and Code

In order to get a dataset for all existing cards in the game, we turned to ygoprodeck and used their free api services to request a JSON package of every existing Yu-Gi-Oh card. The JSON package contains many different attributes about the cards, however, we’re only focusing on the card’s text description which contains the card’s effects. Furthermore, we also trimmed the card description of common stop words as well as semantics that are negligible in the context of card effects and actions (“monster”, “card”, “cannot”, etc.)

In creating a TF-IDF ranking, we referenced Juan Ramos’s Paper, “Using tf-idf to determine word relevance in document queries.” as well as prior knowledge about TF-IDF and information retrieval from taking CS 121 at UCI. Words with high TF-IDF imply that “a strong relationship with the document they appear in,” and thus would be of greater interest to the user as opposed to words with lower TF-IDF scores, which imply the word is insignificant (Ramos).

The LDA Model was created based off David M. Blei, Andrew Y. Ng, and Michael I. Jordan’s paper, “Latent dirichlet allocation.”. The paper describes a model in which groups of data such as document corpuses can be created to infer a latent set of topics. It also discusses how TF-IDF provides basic identification of words to organize documents, but it does not reveal underlying statistical relationships and structures of the documents. Our model was then made using a large majority of Professor Ihler’s code examples as a reference. The alpha and beta parameters influence the distribution of topics in relation to the document and the words in relation to the topics respectively. These parameters influence the topic and the word distributions.


## Experiment and Results

For this project, we perform searches on three queries using naive frequency and TF-IDF. We also created an LDA model on the card text, with the number of topics chosen to inference to be three to represent the card types in the game: spells, traps, and monsters. 

### Naive and TF-IDF Searches
To perform these searches, we first calculated the TF of each document by taking in the entire list of documents and the words contained in that document and divided them. To calculate the IDF,  we took the entire list of documents and their word counts and took the log of the word count across the entire corpus. To calculate the TF-IDF, we simply multipled the TF and IDF of each document. We also kept each in a list such that each document is indexed.

### Naive Search
For the naive frequency search, we took a search query and calculated that query’s frequency relative to each card’s text body. The queries we used to search were the keywords “summon”, “hand”, and “graveyard”. The top three results for the queries are as follows, along with graphs of the term frequency as the amount of documents increase:






### TF-IDF
For the TF-IDF based search, we additionally calculated the IDF as a measure of how significant a word is within the entire corpus in order to calculate the TF-IDF. The top 3 results from the search for each query are as shown:




### LDA
After obtaining a list of the cards and trimming them to just their descriptions, we focused on training the model to separate the cards and group them by monsters, spells, and traps. We used a low alpha of .001 and low beta of .001. 

We then ran the model using Gibbs sampling inference in different iterations (0, 50, 100, 200) to obtain different results.

These are the results after 0, 50, 100, and 200 iterations:


## Conclusions

In our naive and TF-IDF searches, we found that the top 3 cards were the same for both search heuristics, suggesting that TF-IDF provides a marginal gain than naive search with Yu-Gi-Oh cards.

After running the model at 0 iterations, there were many duplicate words in each grouping, but as the model is trained more, the groups each start to have different keywords and they become more distinct in which cards are grouped into which topic. The first topic seems to be related to spell cards as many spell cards affect the opponent directly while the second and third topics categorize traps and monster respectively. 

Spell cards have effects similar to monsters, but are more nuanced towards gaining advantage in the hand, or on the field through adding more cards and destroying other monsters. We can see that the first topic includes “field”, “monster”, and “deck”, words that are indicative of actions and areas of the playing field that most easily gain advantage.

Also, notable is the likely trap topic recognizing that traps tend to directly involve affecting opponent. Traps cards are usually activated in response to an opponent’s actions or monster effects with given conditions, and the keywords “card”, “attack”, “destroy” are allusions to such events in the game.

Additionally, the third topic which we identified as being related to monster cards, involve some of the more common actions relating to monster cards; effects during “battle”, changing a card’s “level”, and effects that “target” another “monster” after the monster is “summoned”.

However, these results are difficult to interpret as many of the group’s keywords are used in all three categories. They may be too general for the model to find any unique keywords that represent each type of card.

It is most likely more practical to sort cards that contain any instance of a query, and then sorting the results alphabetically. Our results from the naive and TF-IDF searches show marginal to little advantage in doing so. Furthermore, we would not recommend LDA for sorting trading cards which mainly uses general keywords in their card effects. We were unable to find any unique keywords that tied monsters, spells and traps to their respective topic; the keywords used in Yu-Gi-Oh are too general, and the text is too sparse to derive any latent relationships. LDA will work better for categories that have different topic with unique keywords, like sport articles. 


## Further Considerations



References

Ramos, Juan. "Using tf-idf to determine word relevance in document queries." Proceedings of the first instructional conference on machine learning. Vol. 242. 2003.

Blei, David M., Andrew Y. Ng, and Michael I. Jordan. "Latent dirichlet allocation." Journal of machine Learning research3.Jan (2003): 993-1022.
