import re
import itertools

input_string = """Err3 1 [('AND', 'x00', 'y00', 'wbd'), ('XOR', 'x01', 'y01', 'dqq')]
Err8:  2 ('AND', 'dqq', 'wbd', 'kwk') [('AND', 'x00', 'y00', 'wbd'), ('XOR', 'x01', 'y01', 'dqq')]
Err5:  1 ('AND', 'x00', 'y00', 'wbd')
Err5:  1 ('AND', 'dqq', 'wbd', 'kwk')
Err5:  1 ('OR', 'kwk', 'mhb', 'vnc')
Err2:  5 [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
Err5:  6 [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
Err8:  6 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
Err8:  5 ('AND', 'rgq', 'svm', 'skn') [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
Err9:  ('AND', 'rgq', 'svm', 'skn') 5
Err8:  5 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
Err8:  4 ('AND', 'rgq', 'svm', 'skn') [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
Err9:  ('AND', 'rgq', 'svm', 'skn') 4
Err8:  4 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
Err8:  3 ('AND', 'rgq', 'svm', 'skn') [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
Err9:  ('AND', 'rgq', 'svm', 'skn') 3
Err8:  3 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
Err8:  2 ('AND', 'rgq', 'svm', 'skn') [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
Err5:  1 ('AND', 'x05', 'y05', 'svm')
Err8:  2 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
Err5:  1 ('AND', 'rgq', 'svm', 'skn')
Err5:  1 ('OR', 'nbc', 'skn', 'pdf')
Err5:  1 ('AND', 'pdf', 'wcw', 'fcv')
Err5:  1 ('OR', 'fcv', 'kwc', 'cqp')
Err1:  15 ('OR', 'dkk', 'pbd', 'z15')
Err5:  16 [('OR', 'wfh', 'wth', 'cpv'), ('XOR', 'x15', 'y15', 'fwr')]
Err8:  17 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('OR', 'hdk', 'rhs', 'npf')
Err8:  16 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('AND', 'ktj', 'npf', 'hdf')
Err8:  15 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('OR', 'hdf', 'vjc', 'jfn')
Err8:  14 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('AND', 'fmc', 'jfn', 'tjk')
Err8:  13 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('OR', 'pdh', 'tjk', 'vws')
Err8:  12 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('AND', 'tbk', 'vws', 'wvf')
Err1:  23 ('AND', 'x23', 'y23', 'z23')
Err5:  24 [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  24 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  9 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('OR', 'fpb', 'rpr', 'kjr')
Err8:  23 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  8 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('AND', 'dnq', 'kjr', 'qnv')
Err8:  22 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  7 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('OR', 'kkq', 'qnv', 'ckr')
Err8:  21 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  6 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('AND', 'ckr', 'ttw', 'phn')
Err8:  20 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  5 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('OR', 'dhr', 'phn', 'tdb')
Err8:  19 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  4 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('AND', 'mdg', 'tdb', 'wth')
Err8:  18 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  3 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('OR', 'wfh', 'wth', 'cpv')
Err8:  17 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err8:  2 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
Err5:  1 ('XOR', 'cpv', 'fwr', 'kqk')
Err8:  16 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err5:  1 ('AND', 'kqk', 'rbr', 'bbm')
Err8:  15 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err5:  1 ('OR', 'bbm', 'qbc', 'gcc')
Err8:  14 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err5:  1 ('AND', 'dhd', 'gcc', 'bdv')
Err8:  13 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err5:  1 ('OR', 'bdv', 'grk', 'dbd')
Err8:  12 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err5:  1 ('AND', 'dbd', 'tcb', 'fwn')
Err8:  11 ('OR', 'cgq', 'qdg', 'ngq') [('AND', 'hpw', 'kph', 'qdg'), ('XOR', 'hpw', 'kph', 'cgq')]
Err5:  1 ('OR', 'djp', 'fwn', 'bbc')
Err1:  39 ('AND', 'bdr', 'fsp', 'z39')
Err5:  40 [('AND', 'x39', 'y39', 'nrj'), ('XOR', 'bdr', 'fsp', 'fnr')]
Err8:  40 ('OR', 'fnr', 'nrj', 'sbn') [('AND', 'x39', 'y39', 'nrj'), ('XOR', 'bdr', 'fsp', 'fnr')]
Err9:  ('OR', 'fnr', 'nrj', 'sbn') 40
Err8:  39 ('OR', 'fnr', 'nrj', 'sbn') [('AND', 'x39', 'y39', 'nrj'), ('XOR', 'bdr', 'fsp', 'fnr')]
Err9:  ('OR', 'fnr', 'nrj', 'sbn') 39
Err8:  38 ('OR', 'fnr', 'nrj', 'sbn') [('AND', 'x39', 'y39', 'nrj'), ('XOR', 'bdr', 'fsp', 'fnr')]
Err9:  ('OR', 'fnr', 'nrj', 'sbn') 38
Err8:  37 ('OR', 'fnr', 'nrj', 'sbn') [('AND', 'x39', 'y39', 'nrj'), ('XOR', 'bdr', 'fsp', 'fnr')]
Err9:  ('OR', 'fnr', 'nrj', 'sbn') 37"""

pattern = r"\(\s*'[^']+',\s*'[^']+',\s*'[^']+',\s*'[^']+'\s*\)"

# Find all matches
matches = re.findall(pattern, input_string)


s =set()
# Print the results
for match in matches:
    s.add(eval(match)[-1])

c = 0
for i in itertools.permutations([*s], 8):
    c += 1
print(c)