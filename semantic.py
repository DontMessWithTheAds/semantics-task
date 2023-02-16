import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print (word1.similarity(word2))
print (word3.similarity(word2))
print (word3.similarity(word1))

#what i find interesting about this similaries is that clearly the two top are both mammals hence why they are quite similar
#obviously biologically and culturally a monkey and a banana are synonomous with eachother but not as close as cats due to them still being a food
#and cat and banana are the least due to cats not being known for eating bananas but i guess bananas are still food so it is not impossible
#to imagine them together 



word4 = nlp("fish")
word5 = nlp("ocean")
word6 = nlp("building")

print (f"\n{word4.similarity(word5)}")
print (word6.similarity(word5))
print (word6.similarity(word4))

#So as predicted the first two are the most closely related as fish live in the ocean 
#What i find interesting about the next two comparisons is that ocean and building are more closely related 
#I am summising this is because an ocean and building are both inhabitable places but ultimately are hugely differently
#Then clearly a building and a fish are nothing alike, a fish does not live in a building nor does it build 

