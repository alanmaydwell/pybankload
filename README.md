# pybankload
Helps make bankload files for CIS/CCMS      
File format based on info in *Receipting CIS & CWX Payments into CCMS v1-3.docx*

### Usage

(1) Edit details at end of **bankfile.py** with values to be included in the file
```
# Create bankfile with two payments
myfile = BankFile()
myfile.add_receipt(book_no="212156419026", amount="12345", name="CCMS", yearday="19100")
myfile.add_receipt(book_no="212156419056", amount="23456", name="CIS", yearday="19101")
myfile.add_end()
myfile.write()
print("Finished! Saved:", myfile.filename)
```
#### Parameters
**book_no** - payment book number    
**amount** - payment amount in pence (10000 for £100.00)     
**name** - applicant name (optional and no more than 18 characters)    
**yearday** - date of payment in format with first two digits representing the year and next three digits the day within the year,
e.g. 17001 for first day of 2017 and 17365 for last day of 2017.       

(2) Run bankfile.py to generate the file. Filename created automatically in `bankfile<dmy>.n` format. Some examples included in this repo.   
Note the files are created with \n line-ends (which is authentic) but Github upload unhelpfully converts them to \r\n.

### Finding Payment Book Numbers
**payment_book_info.sql** can be run in CIS database to get payment book numbers. The dso.migrated_flag can be used to identify cases migrated to CIS ("Y" indicates case migrated).
