"""
Description: Testing installed module from 8A.
    
Author: Daniel Martens
Section Number: 251409
Date Created: March 19, 2024

Updates: A change #3 to record on GitHub
"""

import ip_checker

myparser = ip_checker.MyHTMLParser()

print("It shouldn't print IP address until you press enter...")
input()

myparser.get_ip_address()
