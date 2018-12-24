"""
package_topics.json
{
    "ecosystem": "maven",
    "package_topic_map": {
    "pck1": ["p","q"],
    "pck2": ["w","q"]
    }
}
manifest.json
{
    "ecosystem": "maven",
    "package_list": [
    ["a","b","c"],
    ["d","e","f"]
    ]
}
"""

import json


def load_json_file(file_name):
    with open(file_name, 'r') as f:
        file = json.load(f)
    return file    


def save_json_file(file_name, json_data):
    with open(file_name, 'w') as f:
        json.dump(json_data, f, indent=True)


def add_package_topics(pck_dict, output_dict):
    for k, v in pck_dict.get('package_topic_map', {}).items():
        if k in output_dict.keys():
            l = []
            l = output_dict[k]
            l.extend(v)
            l = set(l)
            output_dict[k] = list(l)
        else:
            output_dict[k] = v
    return output_dict    


def get_all_manifest(pck_dict, output_list):
    for pck_list in pck_dict.get('package_list', []):
        output_list.append(pck_list)
    return output_list


def generate_package_topic(file_list):
    p = {}
    for file_name in file_list:
        f = load_json_file(file_name)
        p = add_package_topics(f, p)
    
    package_topic = {}
    package_topic['ecosystem'] = 'maven'
    package_topic['package_topic_map'] = p
    save_json_file('package_topic.json', package_topic)


def generate_manifest(file_list):
    p = []
    for file_name in file_list:
        f = load_json_file(file_name)
        p = get_all_manifest(f, p)
    
    manifest = {}
    manifest['ecosystem'] = 'maven'
    manifest['package_list'] = p
    save_json_file('manifest.json', manifest)

if __name__ == '__main__':
        generate_package_topic(['package_topics_sb.json', 'package_topics_vertex.json'])
        generate_manifest(['manifest_sb.json', 'manifest_vertex.json' ])
