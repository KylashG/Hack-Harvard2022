import spacy

nlp = spacy.load("en_core_web_sm")

# extractive summary by word count
text = """Differential solar heating of low and high latitudes is the mechanism which drives the earth’s large- scale atmospheric and oceanic circulations. Most of the energy from the sun entering the atmos- phere as short-wave radiation (or insolation) reaches the earth’s surface. Some is reflected back to space. The remainder is absorbed by the surface which then warms the atmosphere above it. The atmosphere and surface together radiate long- wave (thermal) radiation back to space. Although the land and ocean parts of the surface absorb different amounts of solar radiation and have different thermal characteristics, the differential solar heating between low and high latitudes dom- inates, fostering an equator-to-pole gradient in atmospheric and upper ocean temperatures.
Although increased solar heating of the tropical regions compared with the higher latitudes had long been apparent, it was not until 1830 that Schmidt made a key calculation, namely heat gains and losses for each latitude by incoming solar radiation and by outgoing longwave radiation from the earth. This showed that equatorward of about latitudes 35° there is an excess of incoming solar over outgoing longwave energy, while pole- ward of those latitudes the longwave loss exceeds solar input. If, at each latitude, the longwave loss to space equaled the solar radiation input (termed radiative equilibrium), this pattern would not be seen. That it exists is direct evidence that there must be an overall tranasfer of energy from lower to higher latitudes via the atmospheric and oceanic circulations. Put differently, while the differential solar heating gives rise to the equator- to-pole temperature gradient, the poleward energy transports work to reduce this gradient. Later and more refined calculations showed that the poleward flow (or flux) of atmospheric energy reaches a maximum around latitudes 30° and 40°, with the maximum ocean transport occurring at lower latitudes. The total poleward transport in both hemispheres is in turn dominated by the atmosphere. The amount of solar energy being received and re-radiated from the earth’s surface can be computed theoretically by mathematicians and astronomers. Following Schmidt, many such calculations were made, notably by Meech (1857), Wiener (1877) and Angot (1883) who calculated the amount of extraterrestrial insolation received at the outer limits of the atmosphere at all latitudes. Theoretical calculations of insolation in the past by Milankovitch (1920, 1930), and Simpson’s (1928–1929) calculated values of the insolation balance over the earth’s surface, were important contributions to understanding astro- nomic controls of climate. Nevertheless, the solar radiation received by the earth was only accurately determined by satellites in the 1990s."""
# tokenize
doc = nlp(text)

# create dictionary
word_dict = {}
# loop through every sentence and give it a weight
for word in doc:
    word = word.text.lower()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# create a list of tuple (sentence text, score, index)
sents = []
# score sentences
sent_score = 0
for index, sent in enumerate(doc.sents):
    for word in sent:
        word = word.text.lower()
        sent_score += word_dict[word]
    sents.append((sent.text.replace("\n", " "), sent_score/len(sent), index))

# sort sentence by word occurrences
sents = sorted(sents, key=lambda x: -x[1])
# return top 3
sents = sorted(sents[:3], key=lambda x: x[2])

# compile them into text
summary_text = ""
for sent in sents:
    summary_text += sent[0] + " "
 
print(summary_text)
