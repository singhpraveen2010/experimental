import json
list=['patternfly.json']

for fname in list:
	dep={}                                     
        data={}
        with open(fname, 'r') as fo:
                data=json.load(fo)
                for d in data['dependencies']:
                        dep[d['package_name']]=d['version_spec']['spec']
                data['dependencies']=dep 
        with open(fname+"_new",'w') as fp:            
                json.dump(data,fp, indent=4)
