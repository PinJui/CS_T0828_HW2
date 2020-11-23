import json
import ast
counter = 1
alllist = []
thresh = 0
imgdict = {'bbox':[],'score':[],'label':[]}
with open('result_output10epochhw2.txt','r') as f:
    line = f.readline()
    while line:
        line = ast.literal_eval(line)
        if len(line) != 0:
            for j in line:
                if float(j[-1]) >= thresh:
                    imgdict['bbox'].append(tuple((round(j[1]), round(j[0]), round(j[3]), round(j[2]))))
                    imgdict['score'].append(float(j[-1]))
                    imgdict['label'].append(int(counter))
        counter+=1
        if counter==11:
            alllist.append(imgdict)
            imgdict = {'bbox':[],'score':[],'label':[]}
            counter=1
        line = f.readline()

with open('309505013_7.json','w') as m:
    json.dump(alllist, m)



