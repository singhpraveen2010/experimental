from __future__ import division
import json


def get_data(filename):
    with open(filename, 'r') as f:
        json_data = json.load(f)
    return json_data


def get_count(data):
    for each_list in data:
        e = each_list['ecosystem']
        if e != 'maven':
            continue
        print e
        package_list = each_list['package_list']
        vertx = "vertx"
        spring = "spring-boot"
        count = 0
        print "The dep_list with both vertx and spring-boot are::\n"
        for dependency_list in package_list:
            vertx_match = False
            spring_match = False
            for dependency in dependency_list:
                if dependency.rfind(vertx) != -1:
                    vertx_match = True
                elif dependency.rfind(spring) != -1:
                    spring_match = True
            if vertx_match and spring_match:
                count += 1
            print dependency_list
            print "\n"
        l = len(package_list)
        percentage = count / l * 100
        print l
        print "\nThe percentage of packages with both vertx and springboot is:: %f" % percentage


def main():
    data = get_data('manifest.json')
    get_count(data)


if __name__ == '__main__':
    main()
