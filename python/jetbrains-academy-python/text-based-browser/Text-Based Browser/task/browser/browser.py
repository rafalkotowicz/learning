from os import rmdir, mkdir, path
from urllib.parse import urlparse

import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

### INIT
expected_noof_arguments = 1
provided_args = f"You provided {len(sys.argv) - 1} arguments"
expected_args = f"Expected exactly {expected_noof_arguments} argument"

if len(sys.argv) - 1 < expected_noof_arguments:
    print(f"Too few arguments passed to script. {provided_args}. {expected_args}.")
    sys.exit(-1)
elif len(sys.argv) - 1 > expected_noof_arguments:
    print(f"Too many arguments passed to script. {provided_args}. {expected_args}.")
    sys.exit(-1)

workdir = sys.argv[1]
rmdir(workdir)
mkdir(workdir)
print(f"Directory created: {workdir}")


### UTILS
def is_url(maybe_url):
    parsed_url = urlparse(maybe_url)
    if str(parsed_url.path).__contains__("."):
        return True
    else:
        return False


def read_file(param):
    pass


def write_file(param):
    pass


def process_request(request):
    if is_url(request):
        file_path = path.join(workdir, request)
        if path.exists(file_path):
            read_file(file_path)
        else:
            write_file(file_path)
            read_file(file_path)
    else:
        print("ERROR! Provided values does not seem to be valid URL (missing dot).")
        return False


### MAIN
while True:
    requested_page = input("Provide valid URL or type 'exit' to leave the program\n")

    if requested_page == "exit":
        break

    if not process_request(requested_page):
        continue

    if requested_page == "bloomberg.com":
        print(bloomberg_com)
    elif requested_page == "nytimes.com":
        print(nytimes_com)
    else:
        print("Unrecognized web page!")
