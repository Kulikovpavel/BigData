import stopwords
import cPickle as pickle 
line = 'conf/ac/IbaL01:::Wayne Iba::Pat Langley:::Unsupervised Learning of Probabilistic-Concept Hierarchies.'
break1 = line.find(':::')
break2 = line.find(':::',break1+1)

authors = line[break1+3:break2].split('::')
print(authors)

words = line[break2+3:].split()
correct_words = [word.replace('-',' ').lower().replace('.','') for word in words if len(word)>1 and word not in stopwords.allStopWords ]

#print(correct_words)
import glob
import stopwords
text_files = glob.glob('hw3data/*')


def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))
              for file_name in text_files)
result = []
def mapfn(key, value):
    for line in value.splitlines():
        
        break1 = line.find(':::')
        break2 = line.find(':::',break1+1)
        authors = line[break1+3:break2].split('::')
        #print(authors.split('::'))
        words = line[break2+3:].split()
        correct_words = [word.replace('-',' ').lower().replace('.','') for word in words if len(word)>1 and word not in stopwords.allStopWords ]

        #print(correct_words)
        
        for author in authors:
            result.append( (author, correct_words))
    return result



def reducefn(key, value):
    result={}
    for correct_words in value:
        for word in correct_words:
            if word not in result:
                result[word]=1
            else:
                result[word]+=1

    return result


a=mapfn('d',source['hw3data\\c0001'])

#print a
 

b=reducefn('ss',[['applications', 'temporal', 'databases', 'knowledge based', 'simulations'],['applications', 'temporal', 'databases', 'knowledge based', 'simulations']])
#print b



# lets create something to be pickled
# How about a list?

# now create a file
# replace filename with the file you want to create
#file = open('pickle', 'w')#

# now let's pickle picklelist
#pickle.dump(a,file)

# close the file, and your pickling is complete
#file.close()


file = open('pickle', 'r')

b = pickle.load(file)
file.close()

print b['Ramachandran Vaidyanathan']


