from pubtator_loader import PubTatorCorpusReader

#dataset_reader = PubTatorCorpusReader('./pubtator_test.txt')

dataset_reader = PubTatorCorpusReader('./pubtator_test.txt')

corpus = dataset_reader.load_corpus() 

#print(corpus[0])

# with open("corpus_pubtator.txt", "r") as f: #encoding = "utf8"
#     data = f.read()
#     print(data)




"""
    10021369	Identification of APC2, a homologue of the <category="Modifier">adenomatous polyposis coli tumour</category> suppressor .	
    The <category="Modifier">adenomatous polyposis coli ( APC ) tumour</category>-suppressor protein controls the Wnt signalling pathway by forming a complex
     with glycogen synthase kinase 3beta ( GSK-3beta ) , axin / conductin and betacatenin . Complex formation induces the rapid degradation of betacatenin . 
     In <category="Modifier">colon carcinoma</category> cells , loss of APC leads to the accumulation of betacatenin in the nucleus , where it binds to and activates the
      Tcf-4 transcription factor ( reviewed in [ 1 ] [ 2 ] ) . Here , we report the identification and genomic structure of APC homologues . Mammalian APC2 , which closely
       resembles APC in overall domain structure , was functionally analyzed and shown to contain two SAMP domains , both of which are required for binding to conductin . 
       Like APC , APC2 regulates the formation of active betacatenin-Tcf complexes , as demonstrated using transient transcriptional activation assays
        in APC - / - <category="Modifier">colon carcinoma</category> cells . Human APC2 maps to chromosome 19p13 . 3 . APC and APC2 may therefore have 
        comparable functions in development and <category="SpecificDisease">cancer</category> .

10051005	A common MSH2 mutation in English and North American <category="Modifier">HNPCC</category> families: origin, phenotypic expression, and sex specific differences in <category="SpecificDisease">colorectal cancer</category> .	The frequency , origin , and phenotypic expression of a germline MSH2 gene mutation previously identified in seven kindreds with <category="SpecificDisease">hereditary non-polyposis cancer syndrome</category> (<category="SpecificDisease">HNPCC</category>) was investigated . The mutation ( A-- > T at nt943 + 3 ) disrupts the 3 splice site of exon 5 leading to the deletion of this exon from MSH2 mRNA and represents the only frequent MSH2 mutation so far reported . Although this mutation was initially detected in four of 33 <category="Modifier">colorectal cancer</category> families analysed from eastern England , more extensive analysis has reduced the frequency to four of 52 ( 8 % ) English <category="Modifier">HNPCC</category> kindreds analysed . In contrast , the MSH2 mutation was identified in 10 of 20 ( 50 % ) separately identified <category="Modifier">colorectal</category> families from Newfoundland . To investigate the origin of this mutation in <category="Modifier">colorectal cancer</category> families from England ( n = 4 ) , Newfoundland ( n = 10 ) , and the United States ( n = 3 ) , haplotype analysis using microsatellite markers linked to MSH2 was performed . Within the English and US families there was little evidence for a recent common origin of the MSH2 splice site mutation in most families . In contrast , a common haplotype was identified at the two flanking markers ( CA5 and D2S288 ) in eight of the Newfoundland families . These findings suggested a founder effect within Newfoundland similar to that reported by others for two MLH1 mutations in Finnish <category="Modifier">HNPCC</category> families . We calculated age related risks of all , <category="CompositeMention">colorectal , endometrial , and ovarian cancers</category> in nt943 + 3 A-- > T MSH2 mutation carriers ( n = 76 ) for all patients and for men and women separately . For both sexes combined , the penetrances at age 60 years for all <category="DiseaseClass">cancers</category>  and for <category="SpecificDisease">colorectal cancer</category> were 0 . 86 and 0 . 57 , respectively . The risk of <category="SpecificDisease">colorectal cancer</category> was significantly higher ( p < 0 . 01 ) in males than females ( 0 . 63 v 0 . 30 and 0 . 84 v 0 . 44 at ages 50 and 60 years , respectively ) . For females there was a high risk of <category="SpecificDisease">endometrial cancer</category> ( 0 . 5 at age 60 years ) and <category="SpecificDisease">premenopausal ovarian cancer</category> ( 0 . 2 at 50 years ) . These intersex differences in <category="Modifier">colorectal cancer</category> risks have implications for screening programmes and for attempts to identify <category="Modifier">colorectal cancer</category> susceptibility modifiers .
"""