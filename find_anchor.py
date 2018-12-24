# coding: utf-8
"""
manifest format:
[
    {
        ecosystem:<value>
        package_list: [
        [...]
        [...]
        [...]
        ]
    }
]
"""

from __future__ import division
import json
import operator


class AnchorPackage(object):

    def __init__(self, anchor_list):
        self.anchor_list = anchor_list

    def read_file(self, filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        return json_data

    def write_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.anchor_list, f, indent=True)

    def find_highest(self, input_filename, output_filename, threshold=None):
        if threshold is None:
            threshold = 15

        json_data = self.read_file(input_filename)
        for data_set in json_data:
            ecosystem = data_set['ecosystem']
            anchor_packages = []
            result_dict = {}
            package_list = data_set['package_list']
            total_package_lists = len(package_list)
            package_name_count = {}

            for dependency_list in package_list:
                for dependency in dependency_list:
                    if dependency in package_name_count:
                        package_name_count[dependency] += 1
                    else:
                        package_name_count[dependency] = 1
            for name, count in package_name_count.items():
                count_percentage = count / total_package_lists * 100
                round_off_count = round(count_percentage, 4)
                if round_off_count >= threshold:
                    anchor_packages.append((name, round_off_count))
            result_dict['ecosystem'] = ecosystem
            result_dict['anchor_packages'] = anchor_packages
            result_dict['manifest_count'] = total_package_lists
            self.anchor_list.append(result_dict)
        self.write_file(output_filename)
        return


def main():
    l = []
    a = AnchorPackage(l)
    a.find_highest('/home/smasud/Downloads/manifest.json', 'anchor.json', 15)

if __name__ == '__main__':
    main()
