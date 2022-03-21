# Databricks notebook source
from cicd_sample_project.jobs.sample.entrypoint import SampleJob

# COMMAND ----------

job = SampleJob()

# COMMAND ----------

job.launch()

# COMMAND ----------

print("This is working")

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------

You can use the command %sh pwd in a notebook inside a Repo to check if Files in Repos is enabled.

If Files in Repos is not enabled, the response is /databricks/driver.
If Files in Repos is enabled, the response is /Workspace/Repos/<path to notebook directory> .
