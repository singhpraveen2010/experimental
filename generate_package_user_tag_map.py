import json
from random import shuffle
import os

# Open the newly generated manifest flie
with open("Documents/manifest.json") as f:
    data = json.load(f)
package_list = data['package_list']
print("Number of Manifest files: {}".format(len(package_list)))
unique_packages = set()
for each_list in package_list:
    for package in each_list:
        unique_packages.add(package)
print("Number of Unique packages: {}".format(len(unique_packages)))
# Open the existing package topic map list
with open("Documents/package_topic.json") as f:
    data1 = json.load(f)
package_topic_map = data1[0]['package_topic_map']
tagged_already = package_topic_map.keys()
# Number of packages of this ecosystem already tagged
print("Number of already tagged packages: {}".format(
    len(unique_packages.intersection(tagged_already))))
untagged_wildfly = list(unique_packages.difference(tagged_already))
# Number of packages of this ecosystem to tag
print("Number of packages to tag: {}".format(len(untagged_wildfly)))
name_list = ["Aagam",
             "Avishkar",
             "Jyasveer",
             "Mitesh",
             "Ravindra",
             "Samuzzal",
             "Sanket",
             "Sarah",
             "Sunil",
             "Arun",
             "Geetika",
             "Jaivardhan",
             "Vasu"]
print("Number of user doing tagging: {}".format(len(name_list)))
n = len(untagged_wildfly) / len(name_list) + 1
i = 0
l = len(untagged_wildfly)
j = 0
shuffle(name_list)
print("Approx. number of packages/user to tag: {}".format(n))
while i < l:
    package_list = untagged_wildfly[i:i + n]
    temp_dict = {x: [] for x in package_list}
    package_name_dict = {'ecosystem': 'maven', 'package_topic_map': temp_dict}
    name = name_list[j] + "_user.json"
    print name
    with open(os.path.join("Documents", "manual_tagging", name), "w") as f:
        json.dump(package_name_dict, f, indent=True)
    i += n
    j += 1
