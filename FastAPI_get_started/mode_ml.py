"""
python -m spacy download en_core_web_sm
"""
import spacy

nlp_en = spacy.load("es_core_news_sm")
doc_en = nlp_en("Apple compra una empresa de EEUU por 1 millón de dolares en Octubre")
for ent in doc_en.ents:
    print(ent.text, ent.label_)

print('Fin')