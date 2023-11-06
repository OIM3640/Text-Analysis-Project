import part1 as p
import natural_language_processing as nlp

cf = p.Cuba_freedom
hc = p.history_Cuba
mmp = p.murder_piracy
cuba_list = [cf, hc, mmp]

nlp.find_most_sentiment(cuba_list)
