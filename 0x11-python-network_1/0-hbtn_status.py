#!/usr/bin/python3
"""  fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as response:
        con = response.read()

    print("Body response:")
    print(f"\t- type: {type(con)}")
    print(f"\t- content: {con}")
    print(f"\t- utf8 content: {con.decode('utf-8')}")
