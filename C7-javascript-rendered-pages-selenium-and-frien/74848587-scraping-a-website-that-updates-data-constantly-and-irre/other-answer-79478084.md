---
title: "Scraping a website that updates data constantly and irregularly"
site: stackoverflow
question_id: 74848587
answer_id: 79478084
url: https://stackoverflow.com/a/79478084
author: "Hillary K. Bett"
author_url: https://stackoverflow.com/users/29851111
posted: 2025-03-01T18:38:04Z
last_edited: never
accepted: false
score: -1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 32ebe52cb4f74779a65c081ce746eb1d2817de42f11118eff7f8146c0211c77c
role: another answer on the same question, kept as context; not my work
---

# Answer by [Hillary K. Bett](https://stackoverflow.com/users/29851111) — 2025-03-01

Posted on Stack Overflow, <https://stackoverflow.com/a/79478084>, 2025-03-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

    import csv
    import time
    from datetime import datetime
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    import os
    
    # Configure Chrome options (remove headless for debugging)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment if you want to run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Function to initialize the driver
    def init_driver():
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    
    # Function to scrape the data and save to CSV
    def scrape_data():
        driver = init_driver()
        driver.get("https://play.pakakumi.com/")
    
        # Set to keep track of seen burst values
        seen_burst_values = set()
    
        # Open the CSV file in append mode
        csv_file = 'burst_data.csv'
        file_exists = os.path.isfile(csv_file)
        
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Write headers if the file doesn't exist
            if not file_exists:
                writer.writerow(['burst_value', 'hash_value'])
            
            while True:
                try:
                    # Wait for the table to load by checking for the presence of the tbody element
                    WebDriverWait(driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody tr:first-child'))
                    )
                    
                    # Check if the specific element is visible
                    first_row = WebDriverWait(driver, 60).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody tr:first-child'))
                    )
    
                    burst_value = first_row.find_element(By.CLASS_NAME, 'css-19toqs6').text
                    
                    hash_value = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][readonly]').get_attribute('value')
                    
                    # Remove the 'x' from the burst value and convert to a float
                    numeric_burst_value = float(burst_value.rstrip('x'))
                    
                    # Check if the burst value has been seen before
                    if numeric_burst_value not in seen_burst_values:
                        # Add the burst value to the set of seen values
                        seen_burst_values.add(numeric_burst_value)
                        
                        
                        # Get the current timestamp
                        # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        
                        # Write the data (burst value and timestamp) to the CSV file
                        writer.writerow([numeric_burst_value, hash_value])
                        file.flush()  # Ensure data is written to the file immediately
    
                        # Print the burst value and timestamp for debugging purposes
                        print(f"Scraped burst value: {numeric_burst_value} {hash_value}")
                    
                    # Wait for the next update (adjust the sleep time if necessary)
                    time.sleep(0.001)  # Pause the script for 5 milliseconds
                except Exception as e:
                    # Print detailed error information
                    print(f"Error: {e}")
                    driver.save_screenshot('error_screenshot.png')  # Save screenshot for debugging
                    with open('page_source.html', 'w', encoding='utf-8') as f:
                        f.write(driver.page_source)  # Save the page source for debugging
                    break
    
        driver.quit()
    
    if __name__ == "__main__":
        scrape_data()

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Community](https://stackoverflow.com/users/-1)** (2025-03-02): Your answer could be improved with additional supporting information. Please [edit] to add further details, such as citations or documentation, so that others can confirm that your answer is correct. You can find more information on how to write good answers [in the help center](/help/how-to-answer).
