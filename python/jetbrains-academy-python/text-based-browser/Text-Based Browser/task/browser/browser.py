import os
from collections import deque
from os import rmdir, mkdir, path
from urllib.parse import urlparse

import requests
import sys

# INIT
from bs4 import BeautifulSoup, ResultSet

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
    if str(parsed_url.path).__contains__("."):
        return True
    else:
        return False


def read_file(file_name):
    file_path = path.join(workdir, file_name)
    if path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file_to_read:
            print(file_to_read.read())
            history.append(file_name)


def write_file(file_name, content):
    file_path = path.join(workdir, file_name)
    with open(file_path, 'w', encoding='utf-8') as file_to_write:
        file_to_write.write(content)


def add_https_protocol(url: str):
    if not url.startswith("https://"):
        return "https://" + url


def remove_https_protocol(url: str):
    return url.replace("https://", "")


def strip_file_name(url: str):
    file_name = remove_https_protocol(url)
    return file_name[0:file_name.find(".")]

def call_the_internetz(url: str):
    response = requests.get(add_https_protocol(url))
    soup = BeautifulSoup(response.content, 'html.parser')
    found_tags = soup.find_all(['p', 'a', 'ul', 'ol', 'li'])
    string_list = []
    for tag in found_tags:
        string_list.append(tag.text)

    file_name = strip_file_name(url)
    write_file(file_name, ''.join(string_list))
    read_file(file_name)


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
        call_the_internetz(command)
    else:
        read_file(command)
