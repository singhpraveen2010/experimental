import json

def generate_dep(filename):
	filepath = "Github/fabric8-analytics-data-model/ref_stacks" + filename + ".json"
	load_file = {}
    pom_dep = ""
    with open(filepath, "r") as f:
        load_file = json.load(f)
        d = load_file['dependencies']
    for k,v in d.items(): 
        g, a = k.split(":")
        v = v
        st = """
    <dependency>
        \t<groupId>{0}</groupId>
        \t<artifactId>{1}</artifactId>
        \t<version>{2}</version>
    </dependency>""".format(g, a, v)
        pom_dep = pom_dep + "\n" + st
    print pom_dep

if __name__ == '__main__':
	filename = "springboot27"
	generate_dep()