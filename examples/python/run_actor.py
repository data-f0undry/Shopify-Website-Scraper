"""Python - official apify-client."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("data_foundry/shopify-scraper").call(run_input={
    "storeUrls": [
        "https://www.allbirds.com"
    ],
    "resources": [
        "products"
    ],
    "includeVariants": true
})
print("dataset:", run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
