### triangular.py
# server
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

def final(key, value):
    print key, value

# client
def mapfn(key, value):
    results={}
    for line in value.splitlines():
        break1 = line.find(':::')
        break2 = line.find(':::',break1+1)
        authors = line[break1+3:break2].split('::')
        #print(authors.split('::'))
        words = line[break2+3:].split()
        correct_words = [word.replace('-',' ').lower().replace('.','') for word in words if len(word)>1 and word not in stopwords.allStopWords ]

        #print(correct_words)
        for author in authors:
            if author not in results:
                results[author] = correct_words
            else:
                results[author] += correct_words
    
    for res_key in results:
        yield res_key,results[res_key]   

def reducefn(key, value):
    result={}
    for word in value:
        if word not in result:
            result[word]=1
        else:
            result[word]+=1

    return result