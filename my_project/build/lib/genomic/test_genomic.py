from .tools import tool

def test_is_identifiant():
    # Test une ligne qui est clairement un identifiant FASTA
    line = ">sequence1"
    assert tool.is_identifiant(line) == True

    # Test une ligne qui est clairement une séquence
    line = "ATGCGTAGCTAGCTAGCTAGC"
    assert tool.is_identifiant(line) == False

    # Test une ligne vide
    line = ""
    assert tool.is_identifiant(line) == False
    # Test une ligne qui contient seulement le symbole '>'
    line = ">"
    assert tool.is_identifiant(line) == True

def test_read_file():
    lines = tool.read_file("example/example.fa")
    assert len(lines)!=0

def test_parse_fasta():
    lines = tool.read_file("example/example.fa")
    expected = {"seq1": "ATG", "seq2": "GTA"}
    result = tool.parse_fasta(lines)
    assert result == expected



