from sqlalchemy import create_engine
import boto3
import botocore
import json
import os
from test_config import *


class Jobs(object):

    def __init__(self):
        self.DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
            user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
        self.db = create_engine(self.DB_URL)
        self.session = boto3.session.Session(aws_access_key_id=ACCESS_KEY,
                                             aws_secret_access_key=SECRET_KEY)
        self.s3_resource = self.session.resource('s3', config=botocore.client.Config(
            signature_version='s3v4'), endpoint_url="http://localhost:9000", region_name="us-east-1")
        self.bucket = self.s3_resource.Bucket(AWS_BUCKET_NAME)
        self.bucket_name = AWS_BUCKET_NAME
        self.extra_manifest_list = []
        self.unique_packages = set()

    @staticmethod
    def generate_query(past_var, past_count):
        query = "select all_details -> 'ecosystem' as ecosystem, all_details -> '_resolved' as deps from worker_results"
        query += " cross join jsonb_array_elements(worker_results.task_result -> 'result')"
        query += " all_results cross join jsonb_array_elements(all_results -> 'details') all_details where worker = 'GraphAggregatorTask'"
        query += " and EXTRACT({} FROM age(to_timestamp(task_result->'_audit'->>'started_at','YYYY-MM-DDThh24:mi:ss'))) <={} and all_details->>'ecosystem'='{}';".format(
            past_var, past_count, ecosystem)
        return query

    def execute_query(self, query):
        return self.db.execute(query)

    def read_generic_file(self, filename):
        """Read a file from the S3 bucket."""
        obj = self.s3_resource.Object(self.bucket_name, filename).get()[
            'Body'].read()
        utf_data = obj.decode("utf-8")
        return utf_data

    def read_json_file(self, filename):
        """Read JSON file from the S3 bucket."""
        return json.loads(self.read_generic_file(filename))

    def write_json_file(self, filename, contents):
        """Write JSON file into S3 bucket."""
        self.s3_resource.Object(self.bucket_name, filename).put(
            Body=json.dumps(contents))

    def get_query_data(self, query):
        result = self.execute_query(query).fetchall()
        for each_row in result:
            package_list = []
            if len(each_row) == 2 and each_row[0] == ecosystem:
                for dep in each_row[1]:
                    package_name = dep.get('package')
                    package_list.append(package_name)
                    self.unique_packages.add(package_name)
                self.extra_manifest_list.append(package_list)

    def append_mainfest(self):
        filename = "maven/github/data_input_manifest_file_list/1/manifest.json"
        f = self.read_json_file(filename)
        for each in f:
            if each.get('ecosystem') == ecosystem:
                cur_package_list = each.get('package_list', [])
                cur_package_list.extend(self.extra_manifest_list)
                each['package_list'] = cur_package_list
                break
        filename = "maven/github/data_input_manifest_file_list/1/manifest123.json"
        self.write_json_file(filename, f)

    def append_package_topic(self):
        filename = "maven/github/data_input_raw_package_list/package_topic.json"
        p = self.read_json_file(filename)
        for each in p:
            if each.get('ecosystem') == "maven":
                cur_package_list = each.get('package_topic_map', {})
                for each_pck in self.unique_packages:
                    if each_pck not in cur_package_list:
                        cur_package_list[each_pck] = []
                each['package_list'] = cur_package_list
                break
        self.write_json_file(filename, p)

if __name__ == '__main__':
    j = Jobs()
    query = j.generate_query('DAYS', 7)
    j.get_query_data(query)
    j.append_mainfest()
    j.append_package_topic()
