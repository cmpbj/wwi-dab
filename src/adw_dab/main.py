import requests
import json
import pandas as pd
from datetime import datetime
from delta.tables import DeltaTable

class AdwsExtractor:
    def __init__(self):
        self.session = requests.Session()

    def write_in_volume(self, data: list, endpoint: str):
        pdf = pd.json_normalize(data)
        sdf = spark.createDataFrame(pdf)

        target_path = f"/Volumes/db-raw/wwi_raw/adw_raw/{endpoint}"

        if DeltaTable.isDeltaTable(spark, target_path):
            delta_table = DeltaTable.forPath(spark, target_path)

            # Perform merge based on unique key
            delta_table.alias("target").merge(
                sdf.alias("source"),
                "target.salesOrderDetailId = source.salesOrderDetailId"
            ).whenMatchedUpdateAll() \
             .whenNotMatchedInsertAll() \
             .execute()
        else:
            # Initial write as Delta
            sdf.write.format("delta").mode("overwrite").save(target_path)

    def extract_adw_table_full(self, endpoint: str):
        session = requests.session()
        start_page = 1

        first_response = session.get(
            endpoint, params={"PageNumber": start_page, "PageSize": 200}
        )
        pagination = first_response.headers.get("x-pagination")
        total_pages = json.loads(pagination)["TotalPages"]

        all_data = first_response.json()
        # for page in range(2, total_pages + 1):
        #     resp = session.get(
        #         endpoint, params={"PageNumber": page, "PageSize": 200}
        #     )
        #     all_data.extend(resp.json())

        return all_data

adw = AdwsExtractor()
endpoints = ["salesOrderDetails"]

for endpoint in endpoints:
    link = f"https://demodata.grapecity.com/adventureworks/api/v1/{endpoint}"
    all_page_data = adw.extract_adw_table_full(link)
    adw.write_in_volume(all_page_data, endpoint)
