import json
import glob


def json_indent():  
    count = 1
    for filename in glob.glob("*.json"):
        print filename
        print count
        try:
            load_file = {}
            with open(filename, 'r') as f:
                load_file = json.load(f)

            with open(filename, 'w') as f:
                json.dump(load_file, f, indent=True)
        except Exception as e:
            print("Error with file %s", filename)
        finally:
            count = count + 1

if __name__ == '__main__':
    json_indent() 

