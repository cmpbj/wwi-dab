from pyspark.sql.types import *

movement_schema = StructType([
    StructField("movementKey", LongType(), False),
    StructField("dateKey", StringType(), False),
    StructField("stockItemKey", IntegerType(), False),
    StructField("stockItem", StringType(), True),
    StructField("customerKey", IntegerType(), True),
    StructField("customer", StringType(), True),
    StructField("supplierKey", IntegerType(), True),
    StructField("supplier", StringType(), True),
    StructField("transactionType", StringType(), True),
    StructField("quantity", IntegerType(), False),
])

cities_schema = StructType([
    StructField("cityKey", IntegerType(), False),
    StructField("city", StringType(), True),
    StructField("stateProvince", StringType(), True),
    StructField("country", StringType(), True),
    StructField("continent", StringType(), True),
    StructField("salesTerritory", StringType(), True),
    StructField("region", StringType(), True),
    StructField("subregion", StringType(), True),
    StructField("latestRecordedPopulation", IntegerType(), True),
    StructField("validFrom", StringType(), False),
    StructField("validTo", StringType(), False),
])

customers_schema = StructType([
    StructField("customerKey", IntegerType(), False),
    StructField("customer", StringType(), True),
    StructField("billToCustomer", StringType(), True),
    StructField("category", StringType(), True),
    StructField("buyingGroup", StringType(), True),
    StructField("primaryContact", StringType(), True),
    StructField("postalCode", StringType(), True),
    StructField("validFrom", StringType(), False),
    StructField("validTo", StringType(), False),
])

employees_schema = StructType([
    StructField("employeeKey", IntegerType(), False),
    StructField("employee", StringType(), True),
    StructField("preferredName", StringType(), True),
    StructField("isSalesPerson", BooleanType(), False),
    StructField("photo", StringType(), True),
    StructField("validFrom", StringType(), False),
    StructField("validTo", StringType(), False),
])

payment_method_schema = StructType([
    StructField("paymentMethodKey", IntegerType(), False),
    StructField("paymentMethod", StringType(), True),
    StructField("validFrom", StringType(), False),
    StructField("validTo", StringType(), False),
])

stock_item_schema = StructType([
    StructField("stockItemKey", IntegerType(), False),
    StructField("stockItem", StringType(), True),
    StructField("color", StringType(), True),
    StructField("sellingPackage", StringType(), True),
    StructField("buyingPackage", StringType(), True),
    StructField("brand", StringType(), True),
    StructField("size", StringType(), True),
    StructField("leadTimeDays", IntegerType(), False),
    StructField("quantityPerOuter", IntegerType(), False),
    StructField("isChillerStock", BooleanType(), False),
    StructField("barcode", StringType(), True),
    StructField("taxRate", FloatType(), False),
    StructField("unitPrice", FloatType(), False),
    StructField("recommendedRetailPrice", FloatType(), True),
    StructField("typicalWeightPerUnit", FloatType(), False),
    StructField("photo", StringType(), True),
    StructField("validFrom", StringType(), False),
    StructField("validTo", StringType(), False),
])

transaction_type_schema = StructType([
    StructField("transactionTypeKey", IntegerType(), False),
    StructField("transactionType", StringType(), True),
    StructField("validFrom", StringType(), False),
    StructField("validTo", StringType(), False),
])

orders_schema = StructType([
    StructField("orderKey", LongType(), False),
    StructField("cityKey", IntegerType(), False),
    StructField("address", StringType(), True),
    StructField("customerKey", IntegerType(), False),
    StructField("customer", StringType(), True),
    StructField("stockItemKey", IntegerType(), False),
    StructField("stockItem", StringType(), True),
    StructField("orderDateKey", StringType(), False),
    StructField("pickedDateKey", StringType(), True),
    StructField("salespersonKey", IntegerType(), False),
    StructField("pickerKey", IntegerType(), True),
    StructField("description", StringType(), True),
    StructField("package", StringType(), True),
    StructField("quantity", IntegerType(), False),
    StructField("unitPrice", FloatType(), False),
    StructField("taxRate", FloatType(), False),
    StructField("totalExcludingTax", FloatType(), False),
    StructField("taxAmount", FloatType(), False),
    StructField("totalIncludingTax", FloatType(), False),
    StructField("extraction_date", StringType(), True),
])

purchase_schema = StructType([
    StructField("purchaseKey", LongType(), False),
    StructField("dateKey", StringType(), False),
    StructField("supplierKey", IntegerType(), False),
    StructField("stockItemKey", IntegerType(), False),
    StructField("orderedOuters", IntegerType(), False),
    StructField("orderedQuantity", IntegerType(), False),
    StructField("receivedOuters", IntegerType(), False),
    StructField("package", StringType(), True),
    StructField("isOrderFinalized", BooleanType(), False),
    StructField("extraction_date", StringType(), True),
])

sales_schema = StructType([
    StructField("saleKey", LongType(), False),
    StructField("cityKey", IntegerType(), False),
    StructField("address", StringType(), True),
    StructField("customerKey", IntegerType(), False),
    StructField("billToCustomerKey", IntegerType(), False),
    StructField("stockItemKey", IntegerType(), False),
    StructField("stockItem", StringType(), True),
    StructField("invoiceDateKey", StringType(), False),
    StructField("deliveryDateKey", StringType(), True),
    StructField("salespersonKey", IntegerType(), False),
    StructField("salesPerson", StringType(), True),
    StructField("description", StringType(), True),
    StructField("package", StringType(), True),
    StructField("quantity", IntegerType(), False),
    StructField("unitPrice", FloatType(), False),
    StructField("taxRate", FloatType(), False),
    StructField("totalExcludingTax", FloatType(), False),
    StructField("taxAmount", FloatType(), False),
    StructField("profit", FloatType(), False),
    StructField("totalIncludingTax", FloatType(), False),
    StructField("totalDryItems", IntegerType(), False),
    StructField("totalChillerItems", IntegerType(), False),
    StructField("extraction_date", StringType(), True),
])

stock_holding_schema = StructType([
    StructField("stockHoldingKey", LongType(), False),
    StructField("stockItemKey", IntegerType(), False),
    StructField("quantityOnHand", IntegerType(), False),
    StructField("binLocation", StringType(), True),
    StructField("lastStocktakeQuantity", IntegerType(), False),
    StructField("lastCostPrice", FloatType(), False),
    StructField("reorderLevel", IntegerType(), False),
    StructField("targetStockLevel", IntegerType(), False),
    StructField("extraction_date", StringType(), True),
])

transactions_schema = StructType([
    StructField("transactionKey", LongType(), False),
    StructField("dateKey", StringType(), False),
    StructField("customerKey", IntegerType(), True),
    StructField("customer", StringType(), True),
    StructField("billToCustomerKey", IntegerType(), True),
    StructField("billToCustomer", StringType(), True),
    StructField("supplierKey", IntegerType(), True),
    StructField("supplier", StringType(), True),
    StructField("transactionTypeKey", IntegerType(), False),
    StructField("paymentMethod", StringType(), True),
    StructField("supplierInvoiceNumber", StringType(), True),
    StructField("totalExcludingTax", FloatType(), False),
    StructField("taxAmount", FloatType(), False),
    StructField("totalIncludingTax", FloatType(), False),
    StructField("outstandingBalance", FloatType(), False),
    StructField("isFinalized", BooleanType(), False),
    StructField("extraction_date", StringType(), True),
])
