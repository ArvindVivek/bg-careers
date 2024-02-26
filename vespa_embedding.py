import requests, json
from vespa.package import ApplicationPackage, Field, FieldSet, RankProfile
from vespa.deployment import VespaDocker

data_file_path = 'data/jobs_data.json'
with open(data_file_path) as f:
  data = json.load(f)

for i in range(len(data)):
    data[i]["id"] = i

app_package = ApplicationPackage(name="jobs")
app_package.schema.add_fields(
    Field(name="id", type="string", indexing=["attribute", "summary"]),
    Field(name="company_name", type="string", indexing=["attribute", "summary"]),
    Field(name="position_title", type="string", indexing=["attribute", "summary"], attribute=["fast-search"], index="enable-bm25"),
    Field(name="salary", type="string", indexing=["attribute", "summary"]),
    Field(name="location_remote", type="string", indexing=["attribute", "summary"]),
    Field(name="time", type="string", indexing=["attribute", "summary"]),
    Field(name="date_posted", type="string", indexing=["attribute", "summary"]),
    Field(name="job_description", type="string", indexing=["index", "summary"], index="enable-bm25"),
    Field(name="responsibilities", type="string", indexing=["index", "summary"], index="enable-bm25"),
    Field(name="qualifications", type="string", indexing=["index", "summary"], index="enable-bm25"),
    Field(name="learn_more", type="string", indexing=["attribute", "summary"])
)

app_package.schema.add_field_set(
    FieldSet(name="default", fields=["job_description", "responsibilities", "qualifications"])
)

vespa_docker = VespaDocker()
app2 = vespa_docker.deploy(
    application_package=app_package, 
)

for job in data:
    response = app2.feed_data_point(
        schema="jobs",
        data_id=job["id"],
        fields=job
    )

# app_package.get_schema(name="jobs").add_rank_profile(
#     RankProfile(
#         name="recommendation", 
#         inherits="default", 
#         first_phase="closeness(field, embedding)"
#     )
# )