# docs: https://serpapi.com/youtube-search-api

from serpapi import YoutubeSearch
from urllib.parse import (parse_qsl, urlsplit)

params = {
    "api_key": "...",                    # serpapi api key
    "engine": "youtube",                 # search engine
    "search_query": "minecraft redstone" # search query
}

search = YoutubeSearch(params)           # where data extraction happens

# just to show the page number
page_num = 0

# iterate over all pages
while True:
    results = search.get_dict()          # JSON -> Python dict

    if "error" in results:
        print(results["error"])
        break

    page_num += 1
    print(f"Current page: {page_num}")

    # iterate over organic results and extract the data
    for result in results.get("video_results", []):
        print(result["position_on_page"], result["title"], sep="\n")

    # check if the next page key is present in the JSON
    # if present -> split URL in parts and update to the next page
    if "next" in results.get("serpapi_pagination", {}):
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination", {}).get("next")).query)))
    else:
        break