import os
from pathlib import Path

import spacy
from spacy import displacy

#from scispacy.umls_linking import UmlsEntityLinke
 
# nlp = spacy.load("en_core_web_sm")
# # text = "What video sharing service did Steve Chen, Chad Hurley, and Jawed Karim create in 2005?"
# # doc = nlp(text)
 


# # svg = displacy.render(doc, style="dep")
# # output_path = Path(os.path.join("./", "ent.svg"))
# # output_path.open('w', encoding="utf-8").write(svg)

# string = "Antiretroviral therapy ( ART ) is recommended for all HIV-infected individuals"
# doc = nlp(string)

nlp = spacy.load("en_ner_bc5cdr_md")

text = '''Myeloid derived suppressor cells (MDSC) are immature 
          myeloid cells with immunosuppressive activity. 
          They accumulate in tumor-bearing mice and humans 
          with different types of cancer, including hepatocellular 
          carcinoma (HCC). The patient had a heart attack. He also had a stroke. 
          They were diagnosed with a Tuberculosis'''

doc = nlp(text)

# for ent in doc.ents:
#     print(ent.text)

for token in doc:
    print(token.ent_type_)
# for token in doc: 
#     if token.is_oov:
#         print(token.text)