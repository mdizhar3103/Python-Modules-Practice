# Log File Analysis

def openLogFile(logfile):
    with open(logfile, 'r') as log_file:
        for log_entry in log_file:
            yield log_entry


# Regular Expression (https://regexr.com/)
# https://gchq.github.io/CyberChef/#recipe=Regular_expression('User%20defined','%5E(?P%3Ctimestamp%3E%5B0-9%5D%7B2%7D:%5B0-9%5D%7B2%7D:%5B0-9%5D%7B2%7D)',true,false,false,false,false,false,'Highlight%20matches')&input=NTI6Mjg6MzE
# ?P<comment> = this is like a comment 
# time (10:14:56) = ([0-9]{2}\:[0-9]{2}\:[0-9]{2})
# \s = for space
# username_with_hyphen (md1-izhar) = ([a-zA-Z0-9\-]+)   # + signifies atleast one character match in subset
# ip = ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})
