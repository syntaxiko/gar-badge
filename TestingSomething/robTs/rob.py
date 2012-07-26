from Bio.Seq import Seq
from Bio import SeqIO

oligoTest = ['CCTCTCTATGGGCAGTCGGTGATTAATACGACTCACTATTAGTGGTACGCGCCAGGCTGAAGCGCGTACCAGTTCTGCGGCGTCCGGGTTCTTCTTCTGCGGCATGATCGACTGAGTCGGAGACACGCAGGGATGAGATGG','CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC']

def splitOligo(oligolist,oligo_overlap):
    splitList = []
    for oligo in oligolist:
        for x in range((len(oligo)-20)):
            left = oligo[:20+x]
            right = oligo[len(left)-1-oligo_overlap:]
            right_Seq = Seq(right)
            right = right_Seq.reverse_complement()
            splitList.append([left, str(right)])
    return splitList

def exportFasta(splitTuples):
    fileTuplesLeft = open('tupleOutputLeft.fasta', 'w')
    fileTuplesRight = open('tupleOutputRight.fasta', 'w')
    splitTuplesIndex=0
    for tuple1 in splitTuples:
        fileTuplesLeft.write('>leftSeq'+str(splitTuplesIndex)+'\n'+tuple1[0]+'\n')
        fileTuplesRight.write('>rightSeq'+str(splitTuplesIndex)+'\n'+tuple1[1]+'\n')
        splitTuplesIndex = splitTuplesIndex+1
    fileTuplesLeft.close()
    fileTuplesRight.close()

def fastaToSeq(fastaFile):
    for record in SeqIO.parse(fastaFile, 'fasta'):
        SeqIO.write()

def main():
    exportFasta(splitOligo(oligoTest,13))

if __name__ == '__main__':
    main()