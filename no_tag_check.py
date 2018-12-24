import json


def get_data(filename):
    with open(filename, 'r') as f:
        json_data = json.load(f)
        return json_data


def get_no_tag_packages(data):
    for each_list in data:
        package_list = each_list['package_topic_map']
        e = each_list['ecosystem']
        print "\nThe packages with no tag in %s ecosystem are:\n" % e.upper()
    for package_name, topic_list in package_list.items():
        if len(topic_list) == 0:
            print package_name


def main():
    data = get_data('package_topic.json')
    get_no_tag_packages(data)


if __name__ == '__main__':
    main()
