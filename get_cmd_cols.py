import os
import subprocess


def run_command(command):
    return os.popen(command).read().splitlines()


def get_specific_column(data, column_number):
    return [value.split()[column_number] for value in data]


def print_result(data, title):
    print "The value of %s is %s" % (title, data)


print_result(get_specific_column(run_command("df -h"), 2)[1:], 'Used')
print_result(get_specific_column(run_command("ls -l")[1:], 4), 'Size')
