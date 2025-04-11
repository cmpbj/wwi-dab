import os
import requests
import traceback
from datetime import datetime
from dateutil import parser
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from .schema import *

# Constants
WORLD_IMPORTERS_URL = "https://demodata.grapecity.com/wwi/api/v1/"
VOLUME_PATH = "/Volumes/dlt-db/raw/wwi_landzone"

# Start Spark session
spark = SparkSession.builder.getOrCreate()

# === Utility Functions ===

def extract_json(endpoint):
    url = f"{WORLD_IMPORTERS_URL}{endpoint}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def save_as_parquet(data, filename, schema):
    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        raise ValueError("Unexpected data format")


    df = spark.createDataFrame(data=data, schema=schema)
    df.write.mode("overwrite").parquet(os.path.join(VOLUME_PATH, filename))
    print(f"Saved: {VOLUME_PATH}/{filename}")


def generic_data_func(endpoint, filename, schema):
    data = extract_json(endpoint)
    save_as_parquet(data, f"{filename}.parquet", schema)

def main():
    endpoints = {
        "cities": cities_schema,
        "customers": customers_schema,
        "employees": employees_schema,
        "paymentMethods": payment_method_schema,
        "stockItems": stock_item_schema,
        "transactionTypes": transaction_type_schema,
        "movements": movement_schema,
        "orders": orders_schema,
        "purchases": purchase_schema,
        "sales": sales_schema,
        "stockHoldings": stock_holding_schema,
        "transactions": transactions_schema,
    }

    for endpoint, schema in endpoints.items():
        print(f"🔄 Extracting {endpoint} ...")
        try:
            generic_data_func(endpoint, endpoint, schema)
        except Exception as e:
            print(f"Failed to extract {endpoint}: {e}")
            traceback.print_exc()

if __name__ == "__main__":
    main()
