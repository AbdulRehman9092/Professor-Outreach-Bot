import sys
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import suppress
from seleniumbase import SB
#cahnge Query 8 as per your info or insert your templete.
sys.argv.append("-n")
sys.argv.append("--timeout=60")

write_lock = threading.Lock()

def find_paragraph_by_start(paragraphs, start_text):
    for p in paragraphs:
        if p.strip().lower().startswith(start_text.lower()):
            return p.strip()
    return ""

def get_university_names(file_path="a.txt"):
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

def activate_cdp_with_retry(sb, url, max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            sb.activate_cdp_mode(url)
            return True
        except Exception as e:
            print(f"CDP mode activation failed (attempt {attempt + 1}/{max_retries}): {e}")
            time.sleep(delay)
    return False

def process_university(sb, university_name):
    base_url = "https://www.perplexity.ai/"
    if not activate_cdp_with_retry(sb, base_url):
        print("Failed to reactivate CDP mode after retries.")
    sb.sleep(2)

    try:
        query1 = (f"""{university_name} , i want you to List all professors that has background related to environmental or Civil Engineering. Take as much time as u want but give me full list""")  # First query remains unchanged
        sb.type('textarea[placeholder="Ask anything..."]', query1, timeout=60)
        sb.sleep(5)
        sb.wait_for_element_visible('button[aria-label="Submit"]', timeout=60)
        sb.click('button[aria-label="Submit"]')
        sb.wait_for_element_visible("#markdown-content-0", timeout=60)
        sb.sleep(5)
        with suppress(Exception):
            sb.wait_for_element_not_visible('button[data-testid="stop-button"]', timeout=60)
    except Exception as e:
        print(f"Error during first query for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    
    try:
        query2 = "i dont want retired professor. Check any of these professors you provided has current running projects or any of them have a lab or any of them is accepting students. Check all one by one, take as much time as u want but give me full answer"
        sb.type('textarea[placeholder="Ask follow-up"]', query2, timeout=60)
        sb.wait_for_element_visible('button[aria-label="Submit"]', timeout=60)
        sb.click('button[aria-label="Submit"]')
        sb.wait_for_element_visible("#markdown-content-1", timeout=60)
        sb.sleep(5)
        with suppress(Exception):
            sb.wait_for_element_not_visible('button[data-testid="stop-button"]', timeout=60)
    except Exception as e:
        print(f"Error during 2 query for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    
    try:
        query3 = "now first professor from all the professors u found that are involved in ongoing projects and might be accepting new students. For email address, Make deep search by that first professor name on on google search then search by yourself , then search on university official website." 
        sb.type('textarea[placeholder="Ask follow-up"]', query3, timeout=60)
        sb.wait_for_element_visible('button[aria-label="Submit"]', timeout=60)
        sb.click('button[aria-label="Submit"]')
        sb.wait_for_element_visible("#markdown-content-2", timeout=60)
        sb.sleep(5)
        with suppress(Exception):
            sb.wait_for_element_not_visible('button[data-testid="stop-button"]', timeout=60)
    except Exception as e:
        print(f"Error during 3 query for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    
    try:
        query4 = "now second professor from all the professors u found that are involved in ongoing projects and might be accepting new students. For email address, Make deep search by that second professor name on google search then search by yourself , then search on university official website."  # First query remains unchanged
        sb.type('textarea[placeholder="Ask follow-up"]', query4, timeout=60)
        sb.wait_for_element_visible('button[aria-label="Submit"]', timeout=60)
        sb.click('button[aria-label="Submit"]')
        sb.wait_for_element_visible("#markdown-content-3", timeout=60)
        sb.sleep(5)
        with suppress(Exception):
            sb.wait_for_element_not_visible('button[data-testid="stop-button"]', timeout=60)
    except Exception as e:
        print(f"Error during 3 query for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    
    try:
        query5 = "now third professor from all the professors u found that are involved in ongoing projects and might be accepting new students. For email address, Make deep search by that third professor name on on google search then search by yourself , then search on university official website."
        sb.type('textarea[placeholder="Ask follow-up"]', query5, timeout=60)
        sb.wait_for_element_visible('button[aria-label="Submit"]', timeout=60)
        sb.click('button[aria-label="Submit"]')
        sb.wait_for_element_visible("#markdown-content-4", timeout=60)
        sb.sleep(5)
        with suppress(Exception):
            sb.wait_for_element_not_visible('button[data-testid="stop-button"]', timeout=60)
    except Exception as e:
        print(f"Error during 3 query for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    
    try:
        query6 = "now fourth professor from all the professors u found that are involved in ongoing projects and might be accepting new students. For email address, Make deep search by that fourth professor name on on google search then search by yourself , then search on university official website." 
        sb.type('textarea[placeholder="Ask follow-up"]', query6, timeout=60)
        sb.wait_for_element_visible('button[aria-label="Submit"]', timeout=60)
        sb.click('button[aria-label="Submit"]')
        sb.wait_for_element_visible("#markdown-content-5", timeout=60)
        sb.sleep(5)
        with suppress(Exception):
            sb.wait_for_element_not_visible('button[data-testid="stop-button"]', timeout=60)
    except Exception as e:
        print(f"Error during 3 query for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    

    
    try:
        query7 = "Now from these four professors. Choose randomly 1 professor whose email u found and is related to environmental or Civil Engineering from the professors u found that are involved in ongoing projects and might be accepting new students."
        sb.type('textarea[placeholder="Ask follow-up"]', query7, timeout=60)
        sb.wait_for_element_visible('button[aria-label="Submit"]', timeout=60)
        sb.click('button[aria-label="Submit"]')
        sb.wait_for_element_visible("#markdown-content-6", timeout=60)
        sb.sleep(8)
        answer_container = sb.find_element("#markdown-content-6")
        html_content = answer_container.get_attribute("innerHTML")
    except Exception as e:
        print(f"Error during 4th query for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    
    try:
        soup = sb.get_beautiful_soup(html_content)
        full_text = soup.get_text(" ")
        email_matches = re.findall(r'[\w\.-]+@[\w\.-]+', full_text)
        email_address = email_matches[-1] if email_matches else "email_matches[]"
    except Exception as e:
        print(f"Error extracting email for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    
    try:
        query8 = ("""
Subject: Prospective PhD Student Fall 2025 - Need information on research opportunities ".Blank line after that." 
Hello "put Professor Name without quotation", ".Blank line after that." 
Hope you are doing well. ".Blank line after that." 
My name is YourName, and I have completed Bachelor’s in Civil Engineering from University, Pakistan in September 2024. 
I have read your article about your research project related to “ Project Title ” and I really liked your work. 
I am currently working in a similar area “ His Project Title Related area ” in my internship at Waqas Waqar Engineers & Contractors. ".Blank line after that." 
My project Titled “Project” was presented in International Conference and Published in international Journal at Konya Turkey was fully funded by Council. 
I was also engaged in a project related to “Related to his Research interest work” during my internship at company u do internship in 2023. 
Additionally, looking at the new developments in “some words related to his Research interest without these upper commas” I have developed a keen interest to study in this field. 
Hence I would like to learn about the research opportunities to study and work under your guidance. 
I am attaching my CV with this mail for your reference. ".Blank line after that." 
Looking forward to your reply. Thank you. ".Blank line after that." 
Sincerely, ".Blank line after that." 
YourName ".Blank line." 
.Now I want you to write exactly in that format. Dont change anything in this except what i guide u in "quotations". 
Dont change anything in format. i just want format as it is and i dont want anything in your answer result . not a single extra word. 
I strictly guide you to Fill and authentic and real info of professor as generated only from previous response. 
and fill up all the things that i highlighted in upper commas. 
Make Email as per guidance and as per Professor name, his Project Title, His Research Interest, and email. 
and dont change i single thing in format.""")
        sb.type('textarea[placeholder="Ask follow-up"]', query8, timeout=60)
        sb.click('button[aria-label="Submit"]')
        sb.wait_for_element_visible("#markdown-content-7", timeout=60)
        sb.sleep(15)
        answer_container = sb.find_element("#markdown-content-7")
        html_content = answer_container.get_attribute("innerHTML")
    except Exception as e:
        print(f"Error during third query for {university_name}: {e}")
        if not activate_cdp_with_retry(sb, base_url):
            print("Failed to reactivate CDP mode after query1 error.")
        return
    
    try:
        soup = sb.get_beautiful_soup(html_content)
        paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
        fixed_subject = "Subject: Prospective Master’s Student Fall 2025 - Need information on research opportunities"
        hello_line = find_paragraph_by_start(paragraphs, "Hello")
        hope_line = find_paragraph_by_start(paragraphs, "Hope")
        my_name_paragraph = find_paragraph_by_start(paragraphs, "My name is")
        my_project_paragraph = find_paragraph_by_start(paragraphs, "My project titled")
        looking_forward_line = find_paragraph_by_start(paragraphs, "Looking forward")
        formatted_lines = [
            email_address, fixed_subject, "", hello_line, "", hope_line, "", my_name_paragraph, "",
            my_project_paragraph, "", looking_forward_line, "", "Sincerely,", "Muhammad Abdul Rehman"
        ]
        final_text = "\n".join(formatted_lines)
        with write_lock:
            with open("adan.txt", "a", encoding="utf-8") as f:
                f.write(final_text + "\n\n")
    except Exception as e:
        print(f"Error formatting/saving email for {university_name}: {e}")
    
    
def worker(universities, user_data_dir):
    with SB(uc=True, test=True, ad_block=True, user_data_dir=user_data_dir) as sb:
        base_url = "https://www.perplexity.ai/"
        if not activate_cdp_with_retry(sb, base_url):
            print(f"Initial CDP activation failed for worker with dir {user_data_dir}")
            return
        for uni in universities:
            process_university(sb, uni)

def main():
    university_names = get_university_names("a.txt")
    num_workers = 5
    # Split the university names among workers
    chunks = [university_names[i::num_workers] for i in range(num_workers)]
    # Define a unique user data directory for each instance
    user_data_dirs = [
        "C:\\1",
        "C:\\2",
        "C:\\3",
        "C:\\4",
        "C:\\5"
    ]
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(worker, chunk, user_data_dirs[i]) for i, chunk in enumerate(chunks) if chunk]
        for future in futures:
            future.result()

if __name__ == "__main__":
    main()
