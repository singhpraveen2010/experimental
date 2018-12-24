import config
import requests
import json

user_names = config.user_names
prefix_url = config.prefix_url
ecosystem = config.ecosystem
Authorization = config.Authorization

header = {'Authorization': Authorization}
not_found = []
package_topic_map = []
for name in user_names:
    url = prefix_url + name + "/" + ecosystem
    r = requests.get(url, headers=header)
    if r.status_code != 200:
        not_found.append(name)
        continue
    data = json.loads(r.content)
    package_topic_map.append({name: data['data']['package_topic_map']})

final_list = []
for_ecosystem = {'ecosystem': ecosystem}
final_package_dict = {}
for each_user in package_topic_map:
    name = each_user.keys()[0]
    pck_list = each_user[name]
    for k, v in pck_list.items():
        if k in final_package_dict.keys():
            v = v.extend(final_package_dict[k])
        final_package_dict[k] = list(set(v))
for_ecosystem['package_topic_map'] = final_package_dict
final_list.append(for_ecosystem)

with open('package_topic.json', 'w') as f:
    json.dump(final_list, f, indent=4)
    
empty_count = 0
for package in final_package_dict:
    if len(final_package_dict[package]) == 0:
        empty_count += 1
print("Total packages in %s = %d" % (ecosystem, len(final_package_dict)))
print("Total untagged packages %d" % empty_count)
