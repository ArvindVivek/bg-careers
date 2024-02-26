import requests, json
from vespa.package import ApplicationPackage, Field, FieldSet, RankProfile
from vespa.deployment import VespaDocker

#from vespa_embedding import app2, app_package, data, vespa_docker
data_file_path = 'data/jobs_data.json'
with open(data_file_path) as f:
  data = json.load(f)

for i in range(len(data)):
    data[i]["id"] = i

def vespa_query(query):
    query_body = {
        'yql': 'select * from sources * where userQuery();',
        'select': 'id, company_name, position_title, salary, location_remote, time, date_posted, job_description, responsibilities, qualifications, learn_more',
        'where': 'userQuery()',
        'hits': 10,
        'query': query
    }
    #response = app2.query(body=query_body)

    jobs = data[:5]
    results = []

    """
    given this data for each job:  "company_name": "Adobe",
        "position_title": "Design Engineer, Full Stack Web",
        "salary": "$108,000 -- $198,500 annually",
        "location_remote": "San Francisco, California",
        "time": "Full-Time",

    create a new string that appends like this "Adobe | Design Engineer, Full Stack Web | $108,000 -- $198,500 annually | San Francisco, California | Full-Time"
    """

    for job in jobs:
        result = job["company_name"] + " | " + job["position_title"] + " | " + job["salary"] + " | " + job["location_remote"] + " | " + job["time"]
        results.append(result)

    return results

# app_package.add_schema(
#     Schema(
#         name="user", 
#         document=Document(
#             fields=[
#                 Field(
#                     name="user_id", 
#                     type="string", 
#                     indexing=["summary", "attribute"], 
#                     attribute=["fast-search"]
#                 ), 
#                 Field(
#                     name="embedding", 
#                     type="tensor<float>(d0[51])", 
#                     indexing=["summary", "attribute"]
#                 )
#             ]
#         )
#     )
# )