#test split

geneIdElem = 'https://research.nhgri.nih.gov/hydra/genewiki/gene_page.cgi?gene=Sc4wPfr_1127.1.g1468.t2'

gene_id = (geneIdElem.split("="))[1]

print (gene_id)
