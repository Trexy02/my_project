import setuptools 

setuptools.setup(
    name= "my-genomic",
    description="Ce module permet de lire les fichiers fasta",
    author="Jonas Meziane",
    packages=["genomic/", "genomic/tools/"],
    entry_points={"console_scripts": ["my-genomic = genomic.genomic:run"]},
)