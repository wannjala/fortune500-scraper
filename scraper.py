import requests
from bs4 import BeautifulSoup as BS
import random
import time
import json
import pandas as pd
import os


# Function to get the website's content for a specific year
def get_website_content(year):
    """
    Sends a GET request to the Fortune Magazine website for a specific year and returns a BeautifulSoup object.

    Args:
        year (int): The year for which to retrieve the data.

    Returns:
        BeautifulSoup: Parsed HTML content of the webpage if successful, otherwise None.
    """
    url = f"https://fortune.com/ranking/global500/{year}/search/"

    # Specify headers to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }

    try:
        # Make the request
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print(
                f"Successfully retrieved data for the year {year}, Status code: {response.status_code}"
            )

            # Parse the HTML content with BeautifulSoup
            soup = BS(response.text, "html.parser")
            return soup
        else:
            print(
                f"Failed to retrive data for the year {year}, Status code: {response.status_code}"
            )
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def extract_json_data(soup):
    """
    Extracts JSON data from the HTML soup object by finding the script tag with the id '__NEXT_DATA__'.

    Args:
        soup (BeautifulSoup): BeautifulSoup object of the webpage content.

    Returns:
        dict: Parsed JSON data extracted from the script tag if found, otherwise None.
    """
    try:
        # Find the script tag with id "__NEXT_DATA__"
        script_tag = soup.find("script", id="__NEXT_DATA__")
        if script_tag:
            # Extract the text content
            json_data = json.loads(script_tag.string)
            return json_data
        else:
            print("Couldn't find the '__NEXT_DATA__' script tag.")
            return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON data: {e}")
        return None


def extract_companies_data(json_data, year):
    """
    Extracts company data from the JSON response and adds the year to each record.

    Args:
        json_data (dict): Parsed JSON data from the webpage.
        year (int): The year the data corresponds to.

    Returns:
        list: A list of dictionaries containing the company data for the specified year.
    """
    try:
        # Navigate the JSON structure to get the list of companies
        companies_list = json_data["props"]["pageProps"]["franchiseList"]["items"]

        companies_data = []

        # Loop through each company and extract relevant data
        for company in companies_list:
            company_data = {
                "Year": year,
                "name": company.get("name"),
                "rank": company.get("rank"),
                "order": company.get("order"),
                "Revenues ($M)": company["data"].get("Revenues ($M)"),
                "Revenue Percent Change": company["data"].get("Revenue Percent Change"),
                "Profits ($M)": company["data"].get("Profits ($M)"),
                "Profits Percent Change": company["data"].get("Profits Percent Change"),
                "Assets ($M)": company["data"].get("Assets ($M)"),
                "Headquarters City": company["data"].get("Headquarters City"),
                "Headquarters State": company["data"].get("Headquarters State"),
                "Change in Rank": company["data"].get("Change in Rank"),
                "Gained in Rank": company["data"].get("Gained in Rank"),
                "Dropped in Rank": company["data"].get("Dropped in Rank"),
                "Years on Global 500 List": company["data"].get(
                    "Years on Global 500 List"
                ),
                "Newcomer to the Global 500": company["data"].get(
                    "Newcomer to the Global 500"
                ),
                "Profitable": company["data"].get("Profitable"),
                "Female CEO": company["data"].get("Female CEO"),
                "Growth in Jobs": company["data"].get("Growth in Jobs"),
                "Sector": company["data"].get("Sector"),
                "Fastest Growing Companies": company["data"].get(
                    "Fastest Growing Companies"
                ),
                "Change the World": company["data"].get("Change the World"),
                "World's Most Admired Companies": company["data"].get(
                    "World's Most Admired Companies"
                ),
                "Fortune 500": company["data"].get("Fortune 500"),
                "Best Companies": company["data"].get("Best Companies"),
                "Non-U.S. Companies": company["data"].get("Non-U.S. Companies"),
                "Employees": company["data"].get("Employees"),
                "Industry": company["data"].get("Industry"),
                "Country / Territory": company["data"].get("Country / Territory"),
                "slug": company.get("slug"),
            }
            # Append the company data to the list
            companies_data.append(company_data)

        return companies_data

    except KeyError as e:
        print(f"Error: Missing key in JSON data - {e}")
        return None


def save_to_dataframe(all_companies_data, file_name="fortune_500_global_1995_2024.csv"):
    """
    Save the extracted companies' data to a pandas dataframe and save it as a CSV file
    in a folder called 'data'. If the folder doesn't exist, it will be created.

    Parameters:
    - all_companies_data (list): List of dictionaries containing company data.
    - filename (str): The desired name for the CSV file (without path).
    """
    # Convert the list of dictionaries (all_companies_data) into a pandas DataFrame
    df = pd.DataFrame(all_companies_data)

    # SPecify the foler where the file will be saved
    folder_path = "data"

    # Check if the folder exists, and if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the dataframe to a CSV file inside the 'data' folder
    file_path = os.path.join(folder_path, file_name)
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")
    return df  # This may not be necessary if there is no further use for the dataset.


def main():
    """
    Main function to iterate through years, extract company data, and save the result to a CSV file.

    Loops over a range of years, makes requests to the website, extracts company data for each year,
    and compiles it into a single DataFrame which is saved as a CSV file.
    """

    years = range(1995, 2025)

    all_companies_data = []

    for year in years:
        print(f"Processing data for the year {year}")
        soup = get_website_content(year)

        if soup:
            print(f"Extracting data for the year {year}...")
            json_data = extract_json_data(soup)

            if json_data:
                print(f"Successfully extracted JSON data for the year {year}")
                companies_data = extract_companies_data(json_data, year)
                if companies_data:
                    all_companies_data.extend(
                        companies_data
                    )  # Add each year's companies to the overall list
                    print(f"Successfully extracted company data for the year {year}")
                else:
                    print(f"Failed to extract company data for the year {year}")

            else:
                print(f"Failed to extract JSON data for the year {year}")

        else:
            print(f"Skipping the year {year} due to data retrieval failure.")

        # Introduce a random pause period between 3 and 10 seconds
        wait_time = random.uniform(3, 10)
        print(f"Waiting for {wait_time:.2f} seconds before the next request...")
        time.sleep(wait_time)
        print("\n")
        print("*" * 50)
        print("\n")

    save_to_dataframe(all_companies_data)


if __name__ == "__main__":
    main()
