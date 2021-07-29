# Databricks notebook source
# dbfs.ls.unmount("/mnt/storage")

# COMMAND ----------

try:
  configs = {"fs.azure.account.auth.type": "OAuth",
             "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
             "fs.azure.account.oauth2.client.id": "a6655ff2-c720-4640-a3e4-7038f97e57c8",
             "fs.azure.account.oauth2.client.secret": "7E_Dgw.Y_JJnA19wz.7nhYYMU_-GqT6qf0",
             "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/ef90c086-be63-49c9-912c-d5365ffa61f9/oauth2/token"}

  # Optionally, you can add <directory-name> to the source URI of your mount point.
  dbutils.fs.mount(
    source = "abfss://dev@strai001.dfs.core.windows.net/",
    mount_point = "/mnt/storage",
    extra_configs = configs)

except:
  print("ADLS mounted")
