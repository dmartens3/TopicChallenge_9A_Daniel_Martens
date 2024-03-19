"""
Description: A small python script that gets HTML from 
             a IP lookup site and parses out the IP address.
    
Author: Daniel Martens
Section Number: 251409
Date Created: March 10, 2024

Updates: None
"""

from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    """This class extends the module HTMLParser to
    handle the data and find the IP address."""
    def handle_data(self, data):
        """This method goes through the data and find the ip address."""
        if "Current IP Address:" in data:
            ip_address = data.split(': ')[1].strip()
            print("Found the IP address :", ip_address)

    def get_ip_address(self):
        """This method requests that this class itself finds the ip address."""
        with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
            HTML = str(response.read())
        self.feed(HTML)

def main():
    """This function only runs when executed directly."""
    myparser = MyHTMLParser()
    myparser.get_ip_address()
    print("Press Enter to continue...")
    input()

if __name__ == "__main__":
    main()
