import os
from collections import deque
from os import rmdir, mkdir, path
from urllib.parse import urlparse
from colorama import Fore

import requests
import sys
import pickle

# INIT
from bs4 import BeautifulSoup, ResultSet, PageElement

print("[DEBUG] Initialization STARTED")

expected_noof_arguments = 1
provided_args = f"You provided {len(sys.argv) - 1} arguments"
expected_args = f"Expected exactly {expected_noof_arguments} argument"

if len(sys.argv) - 1 < expected_noof_arguments:
    print(f"[ERROR] Too few arguments passed to script. {provided_args}. {expected_args}.")
    sys.exit(-1)
elif len(sys.argv) - 1 > expected_noof_arguments:
    print(f"[ERROR] Too many arguments passed to script. {provided_args}. {expected_args}.")
    sys.exit(-1)

workdir = sys.argv[1]
if os.path.exists(workdir):
    for root, dirs, files in os.walk(workdir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    rmdir(workdir)
    print(f"[DEBUG] Directory found and removed: {workdir}")

mkdir(workdir)
print(f"[DEBUG] Directory created: {workdir}")

print("[DEBUG] Initialization DONE")


# UTILS
def is_url(maybe_url):
    parsed_url = urlparse(maybe_url)
    if "." in parsed_url.path or "." in parsed_url.hostname:
        return True
    else:
        return False


def read_file(file_name):
    file_path = path.join(workdir, file_name)
    if path.exists(file_path):
        with open(file_path, 'r') as file_to_read:
            return file_to_read.read()


def write_file(file_name, content):
    file_path = path.join(workdir, file_name)
    with open(file_path, 'w') as file_to_write:
        file_to_write.write(content)


def add_https_protocol_if_needed(url: str):
    if not url.startswith("https://"):
        return "https://" + url
    else:
        return url


def remove_https_protocol(url: str):
    return url.replace("https://", "")


def strip_file_name(url: str):
    file_name = remove_https_protocol(url)
    return file_name[0:file_name.rfind(".")]

def print_the_page(response):
    soup = BeautifulSoup(response, 'html.parser')
    found_tags = soup.find_all(['p', 'ul', 'ol', 'li'])
    found_links = soup.find_all('a')

    for tag in found_tags:
        print(tag.text)

    for link in found_links:
        print(Fore.BLUE + link.get('href'))


def call_the_internet(url: str):
    requested_url = add_https_protocol_if_needed(url)
    response = requests.get(requested_url)

    soup = BeautifulSoup(response.content, 'html.parser')

    file_name = strip_file_name(url)
    write_file(file_name, soup.prettify())
    response_read = read_file(file_name)

    print_the_page(response_read)




# MAIN
history = deque()

while True:
    command = input("Provide valid URL or type 'exit' to leave the program\n")

    if command == "exit":
        break

    if command == "back":
        print(f"History len: {len(history)}")
        if len(history) == 0:
            continue
        else:
            history.pop()
            command = history.pop()

    if is_url(command):
        call_the_internet(command)
        history.append(remove_https_protocol(command))
    else:
        print_the_page(read_file(command))
        history.append(remove_https_protocol(command))

