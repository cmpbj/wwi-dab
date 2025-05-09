import os
import re
import requests
import traceback
from datetime import datetime
from dateutil import parser
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from .schema import *

# Constants
WORLD_IMPORTERS_URL = "https://demodata.grapecity.com/wwi/api/v1/"

# Start Spark session
spark = SparkSession.builder.getOrCreate()

# === Utility Functions ===

def extract_json(endpoint):
    url = f"{WORLD_IMPORTERS_URL}{endpoint}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def save_as_table(data, table_name, schema):
    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        raise ValueError("Unexpected data format")

    df = spark.createDataFrame(data=data, schema=schema)

    catalog_name = "`db-raw`"
    schema_name = "wwi_raw"
    full_schema = f"{catalog_name}.{schema_name}"
    full_table_name = f"{full_schema}.{table_name}"

    # Create schema if it doesn't exist
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {full_schema}")

    # Write the data as a table
    df.write.mode("overwrite").saveAsTable(full_table_name)
    print(f"Saved: {full_table_name}")


def generic_data_func(endpoint, table_name, schema):
    data = extract_json(endpoint)
    save_as_table(data, table_name, schema)

def normalize_table_name(endpoint):
    # Convert CamelCase or PascalCase to snake_case
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', endpoint).lower()
    return name

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
            table_name = normalize_table_name(endpoint)
            generic_data_func(endpoint, table_name, schema)
        except Exception as e:
            print(f"Failed to extract {endpoint}: {e}")
            traceback.print_exc()

if __name__ == "__main__":
    main()
