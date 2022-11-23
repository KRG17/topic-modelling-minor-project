from gensim.models import CoherenceModel
from try_gsdmm import *

cm_gsdmm = CoherenceModel(topics=topics,
                          dictionary=dictionary,
                          corpus=bow_corpus,
                          texts=docs,
                          coherence='u_mass')

# get coherence value
coherence_gsdmm = cm_gsdmm.get_coherence()
print()
print("Coherence : ",coherence_gsdmm)