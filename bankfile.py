#!/usr/bin/env python3

import os
import time

class BankFile:
    """Create bankload file"""
    def __init__(self):
        # List holding bank file lines
        self.lines = []
        # Set auto generated filename for the bank file
        self.filename = self.make_filename()
        self.add_top()
        
    def make_filename(self):
        """
        Construct and return bankfilename in standard format -bank<ymd>.n 
        e.g. bank190130.1, bank190130.2
        """
        # Create first date-based part
        first_part = time.strftime("bank%y%m%d.")
        # Need to work out .n counting number - depends on existing files in dir
        # Find existing bank files with same first part
        files = [f for f in os.listdir(os.getcwd()) if f.startswith(first_part)]
        # Find .n part from these files and convert to int
        matching_files_ns = [int(f.split(".")[-1])
                             for f in files if "." in f]
        # Establish .n value for our next filename 
        if matching_files_ns:
            n = 1 + max(matching_files_ns)
        else:
            n = 1
        filename = first_part + str(n)
        return filename

    def add_top(self):
        """Add top line of file to file data"""
        line = "HDR"
        self.lines.insert(0, line)
        
    def add_receipt(self,
                    amount="12345",
                    name="",
                    book_no="212156419097",
                    yearday="19001"):
        """Adds a single receipt to the file data
        Args:
            amount - payment amount in pence, no more than 11 characters
            name - applicant name, optional, no more than 18 characters
            book_no - payment book number
            yearday - date in format - 2 digits for year, 3 digits for day 
                      of year, e.g. 19030 for 30/01/2019
        """
        
        # Gather elements of line, in order
        # Sort code at start,
        line = ["300000"]
        # Collection account number (taken from payment book number)
        line.append("00" + book_no[:6])
        # Type of account and transaction type
        line.extend(["0", "99"])
        # Optional client's sort code and bank account number, can be empty
        # Using empty values here
        line.extend([" "*6, " "*8])
        # Four filler zeros
        line.append("0000")
        # Payment amount in pence, no decimal point and 
        # padded with leading 0s to 11 characters
        line.append(amount.rjust(11, "0"))
        # Client's name - padded with spaces to 18 character length
        line.append(name.ljust(18))
        # Payment book number (also 18 characters allowed but only 12 used by book?)
        line.append(book_no.ljust(18))
        # Beneficiary Name - optional, so blank
        line.append(" "*18)
        # Date in weird format - two digita for year then 3 digits for day number within the year
        # Extra space also needed? Positon 101 to 106, so 6 characters needed
        line.append(" " + yearday)
        # Create line from its elements
        self.lines.append("".join(line))
        
    def add_end(self):
        """Add footer part of file to file data"""
        line = "TLR"
        self.lines.append(line)
        
    def make_string(self):
        """Convert file data (self.lines) to a string and return it"""
        text = ""
        for line in self.lines:
            # using "\n" line end as that's what existing files have
            #(Note from windows need to write using "wb" mode from to keep this)
            text = text + line + "\n"
        return text
    
    def write(self):
        """Write current content to file using filename already set"""
        text = self.make_string()
        # Need to write in different way to ensure \n line ends on Windows
        if os.name == "nt":
            with open(self.filename, "wb") as outfile:
                outfile.write(bytes(text, "UTF-8"))
        else:
            with open(self.filename, "w") as outfile:
                outfile.write(text)

# Note CIS account details are in collection_accounts table

# Create bankfile with two payments
myfile = BankFile()
myfile.add_receipt(book_no="212156419026", amount="12345", name="CCMS", yearday="21100")
myfile.add_receipt(book_no="212156419056", amount="23456", name="CIS", yearday="21101")
myfile.add_end()
myfile.write()
print("Finished! Saved:", myfile.filename)
