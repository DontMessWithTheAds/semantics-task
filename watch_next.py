import spacy

nlp = spacy.load("en_core_web_md")

f = open("movies.txt", "r")
movies = f.readlines()
f.close()


planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk landed on the planet Sakaar where he is sold into slavery and trained as a gladiator. "

planet_hulk_comparison = nlp(planet_hulk)

for descriptions in movies:
    similarity = nlp(descriptions).similarity(planet_hulk_comparison)
    print (descriptions + " - ", similarity)

#The closest to similarity would be Movie C with a score of 0.8873760093882818