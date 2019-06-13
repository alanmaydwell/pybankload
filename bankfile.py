
class BankFile:
    """Create bankload file"""
    def __init__(self):
        # List holding bank file lines
        self.lines = []
        self.filename = "mybankfile.txt"
        self.add_top()

    def add_top(self):
        """Add top line of file"""
        line = "HDR"
        self.lines.insert(0, line)
        
    def add_receipt(self,
                    amount="00000012345",
                    name="FRED",
                    book_no="212156419097",
                    yearday="19001"):
        
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
        """Add footer part of file"""
        line = "TLR"
        self.lines.append(line)
        
    def make_string(self):
        """Convert self.lines to a string and return it"""
        text = ""
        for line in self.lines:
            text = text + line + "\n"
        return text
    
    def write(self):
        """Write current content to file"""
        text = self.make_string()
        with open(self.filename, "w") as outfile:
            outfile.write(text)


# Note account details are in collection_accounts table


# Create bankfile with two payments
myfile = BankFile()
myfile.add_receipt(book_no="212156419026", amount="12345", name="CCMS", yearday="19100")
myfile.add_receipt(book_no="212156419056", amount="23456", name="CIS", yearday="19101")
myfile.add_end()
myfile.write()
print("Finished! Saved:", myfile.filename)

            
            