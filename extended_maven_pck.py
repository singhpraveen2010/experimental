import glob
import json

def open_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def save_file(filename, json_data):
    with open(filename, 'w') as f:
        json.dump(json_data, f, indent=True)

def create_extended_list(data, glob_name):
    pck_list = data[0]['package_list']
    pck_set = [set(pl) for pl in pck_list]
    e_list = []
    for filename in glob.glob(glob_name):
        load_file = {}
        load_file = open_file(filename)
        d = load_file['dependencies']
        d_set = set(d.keys())
        if d_set not in pck_list:
            e_list.append(list(d_set))
    return e_list

def create_new_data(e_list, data):
     pck_list = data[0]['package_list']           
    for pl in e_list:
        pck_list.append(pl)   
    new_d = {}
    new_d['ecosystem'] = data[0].get('ecosystem')
    new_d['package_list'] = pck_list
    new_l = [new_d]
    return new_l

def main():
    filename = "manifest.json"
    data = open_file(filename)
    extended_list = []
    reg_list = ["maven", "springboot"]
    for name in reg_list:
        glob_name =  "ref_stacks/" + reg_list + "*_.json"
        e_list = create_extended_list(data, glob_name)
        extended_list.extend(e_list)
    new_data = create_new_data(extended_list, data)
    save_file("manifest_resultant.json", new_data)    

if __name__ == '__main__':
    main()    

    