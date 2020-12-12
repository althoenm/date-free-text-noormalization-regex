import re
filename = 'dates.txt'


def find_backslash_dates(fname):
    ''' Find all dates with XX/XX/XXXX format and return them in YYYY-MM-DD format '''
    with open(filename, 'r') as file:
    
        for line in file:
            match = re.search(r"(\d+)\t(.*)", line)
            id = match.group(1)
            all = re.findall(r"(\d{1,2})(/)?(\d{1,2})*(/)(\d{2,4})", line) 
            for s in all:
                day = s[2]
                month = s[0]
                year = s[4]
                divider = s[1] and s[3]
                
                
                if s[0] and s[1] == "":
                    month ==s[2]
                    day = "01"
                    year = s[4]
                    if int(month) > 12:
                        break
                    elif len(month) < 2:
                        month = f"0{month}"
                    print(f"{id}    {year}-{month}-{day}")
                elif divider == '/': 
                    divider = divider.replace('/','-')
                    if  2000 < int(year) < 2021:
                        if len(month) < 2:
                            month = f"0{month}"     
                        if len(day) < 2:
                            day = f"0{day}"

                    if  1900 < int(year) <= 1999: 
                        if len(month) < 2:
                            month = f"0{month}"     
                        if len(day) < 2:
                            day = f"0{day}"

                    elif 0 < int(year) < 99:
                        year = f"19{year}"
                        if len(month) < 2:
                            month = f"0{month}"     
                        if len(day) < 2:
                            day = f"0{day}"

                    print(f"{id}    {year}{divider}{month}{divider}{day}")

def find_dash_dates(fname):
    '''Find all dates with XX-XX-XXXX format and return them in desired YYYY-MM-DD format'''
    with open(filename, 'r') as file:

        for line in file:
            match = re.search(r"(\d+)\t(.*)", line)
            id = match.group(1)
            all = re.findall(r"(\d{1,2})(-)(\d{1,2})(-)(\d{2,4})", line) 
            for s in all: 
                month = s[0] 
                day = s[2]
                year = s[4]
                divider = s[1] and s[3]
                if  2000 < int(year) < 2021: 
                    if len(month) < 2:
                        month = f"0{month}"     
                    if len(day) < 2:
                        day = f"0{day}"

                if  1900 < int(year) <= 1999: 
                    if len(month) < 2:
                        month = f"0{month}"     
                    if len(day) < 2:
                        day = f"0{day}"

                elif 00 < int(year) < 100:  
                    year = f"19{year}"
                    if len(month) < 2:
                        month = f"0{month}"     
                    if len(day) < 2:
                        day = f"0{day}"
                print(f"{id}    {year}{divider}{month}{divider}{day}")

def find_month_year_dates(fname):
    '''Find all dates with name format and return them in desired YYYY-MM-DD format'''
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r"(\d+)\t(.*)", line)
            id = match.group(1)
            all = re.findall(r"(January|February|March|Marc|April|June|July|August|September|October|November|December|Decemeber),?(\s)(\d{4})", line) 
            for s in all:
                month = s[0] 
                year = s[2]
                divider = s[1] 
                day = "01" 
                if divider == ' ':
                    divider = divider.replace(' ','-')
                if 0 < int(year) < 100: 
                    year = f"19{year}"
                if month == 'January':
                    month = '01'
                if month == 'February':
                    month = '02'
                if month =='March':
                    month = '03'
                if month == 'April':
                    month = '04'
                if month == 'June':
                    month = '06'
                if month == 'July':
                    month = '07'
                if month == 'August':
                    month = '08'
                if month == 'September':
                    month = '09'
                if month == 'October':
                    month = '10'
                if month == 'November':
                    month = '11'
                if month == 'December':
                    month = '12'
                if month == 'Decemeber':
                    month ='12'
                print(f"{id}    {year}{divider}{month}{divider}{day}")

def find_short_month_year_dates(fname):
    '''Find all dates with name format and return them in desired YYYY-MM-DD format'''
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r"(\d+)\t(.*)", line)
            id = match.group(1)
            all = re.findall(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec),?(\s)(\d{4})", line)
            for s in all: 
                month = s[0] 
                year = s[2]
                divider = s[1] 
                day = "01" 
                if divider == ' ': 
                    divider = divider.replace(' ','-')
                if 0 < int(year) < 100: 
                    year = f"19{year}"
                if month == 'Jan':
                    month = '01'
                if month == 'Feb':
                    month = '02'
                if month =='Mar':
                    month = '03'
                if month == 'Apr':
                    month = '04'
                if month == 'May':
                    month = '05'
                if month == 'Jun':
                    month = '06'
                if month == 'Jul':
                    month = '07'
                if month == 'Aug':
                    month = '08'
                if month == 'Sep':
                    month = '09'
                if month == 'Oct':
                    month = '10'
                if month == 'Nov':
                    month = '11'
                if month == 'Dec':
                    month = '12'
            #print(f"Match {count}/500")
                print(f"{id}    {year}{divider}{month}{divider}{day}")
        
def find_month_day_year_dates(fname):
    '''Find all dates with name format and return them in desired YYYY-MM-DD format'''
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r"(\d+)\t(.*)", line)
            id = match.group(1)
            all = re.findall(r"(January|February|March|April|June|July|August|September|October|November|December).?(\s)(\d{1,2})(,)?(\s)(\d{2,4})", line) 
            for s in all: #iterate through all extracted dates, s = individual tuple for individual extracted date
                #count += 1 #add 1 to total count for each date extracted
                month = s[0] #change month to digits
                year = s[5]
                divider = s[1] and s[4] 
                day = s[2] #day not included in notes
                if divider == ' ': #Begin adjusting formatting to desired YYYY-MM-DD output
                    divider = divider.replace(' ','-')
                if 0 < int(year) < 100: #1900 years defined with two digits 
                    year = f"19{year}"
                if month == 'January':
                    month = '01'
                if month == 'February':
                    month = '02'
                if month =='March':
                    month = '03'
                if month == 'April':
                    month = '04'
                if month == 'June':
                    month = '06'
                if month == 'July':
                    month = '07'
                if month == 'August':
                    month = '08'
                if month == 'September':
                    month = '09'
                if month == 'October':
                    month = '10'
                if month == 'November':
                    month = '11'
                if month == 'December':
                    month = '12'
            #print(f"Match {count}/500")
                print(f"{id}    {year}{divider}{month}{divider}{day}")
                
def find_short_month_day_year_dates(fname):
    '''Find all dates with name format and return them in desired YYYY-MM-DD format'''
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r"(\d+)\t(.*)", line)
            id = match.group(1)
            all = re.findall(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\s)(\d{1,2})(,)(\s)(\d{2,4})", line) 
            for s in all: #iterate through all extracted dates, s = individual tuple for individual extracted date
                #count += 1 #add 1 to total count for each date extracted
                month = s[0] #change month to digits
                year = s[5]
                divider = s[1] and s[4] 
                day = s[2] #day not included in notes
                if divider == ' ': #Begin adjusting formatting to desired YYYY-MM-DD output
                    divider = divider.replace(' ','-')
                if 0 < int(year) < 100: #1900 years defined with two digits 
                    year = f"19{year}"
                if month == 'January':
                    month = '01'
                if month == 'February':
                    month = '02'
                if month =='March':
                    month = '03'
                if month == 'April':
                    month = '04'
                if month == 'May':
                    month = '05'
                if month == 'June':
                    month = '06'
                if month == 'July':
                    month = '07'
                if month == 'August':
                    month = '08'
                if month == 'September':
                    month = '09'
                if month == 'October':
                    month = '10'
                if month == 'November':
                    month = '11'
                if month == 'December':
                    month = '12'
            #print(f"Match {count}/500")
                print(f"{id}    {year}{divider}{month}{divider}{day}")

def find_month_comma_year_dates(fname):
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r"(\d+)\t(.*)", line)
            id = match.group(1)
            all = re.findall(r"(January|February|March|Marc|April|June|July|August|September|October|November|December)(,)(\s)(\d{2,4})", line) 
            for s in all: #iterate through all extracted dates, s = individual tuple for individual extracted date
                #count += 1 #add 1 to total count for each date extracted
                month = s[0] #change month to digits
                year = s[3]
                divider = s[2]
                day = "01" #day not included in notes
                if divider == ' ': #Begin adjusting formatting to desired YYYY-MM-DD output
                    divider = divider.replace(' ','-')
                if 0 < int(year) < 100: #1900 years defined with two digits 
                    year = f"19{year}"
                if month == 'January':
                    month = '01'
                if month == 'February':
                    month = '02'
                if month =='March':
                    month = '03'
                if month == 'Marc':
                    month = '03'
                if month == 'April':
                    month = '04'
                if month == 'May':
                    month = '05'
                if month == 'June':
                    month = '06'
                if month == 'July':
                    month = '07'
                if month == 'August':
                    month = '08'
                if month == 'September':
                    month = '09'
                if month == 'October':
                    month = '10'
                if month == 'November':
                    month = '11'
                if month == 'December':
                    month = '12'
            #print(f"Match {count}/500")
                print(f"{id}    {year}{divider}{month}{divider}{day}")

def find_year_dates(fname):
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r"(\d+)\t(.*)", line)
            id = match.group(1)
            all = re.findall(r"(January|February|March|April|June|July|August|September|October|November|December|Decemeber|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|/|,|\d|/)?\s\(?(\d{4})[A-Z]?", line) 
            for s in all: #iterate through all extracted dates, s = individual tuple for individual extracted date
                if s[0] == '':
                    month = '01'
                    day = '01' 
                    year = s[1]
                    if int(year) < 2021:
                        print(f"{id}    {year}-{month}-{day}")
                else:
                    break

if __name__ == '__main__':
    #x = find_backslash_dates(filename) and find_dash_dates(filename) and find_month_year_dates(filename) and find_short_month_year_dates(filename) and find_month_day_year_dates(filename) and find_short_month_day_year_dates(filename)

    find_backslash_dates(filename)
    find_dash_dates(filename)
    find_month_year_dates(filename)
    find_short_month_year_dates(filename)
    find_month_day_year_dates(filename)
    find_short_month_day_year_dates(filename)
    find_year_dates(filename)
    
#After match, identify constraint, do match on the match. Do error check
#Can have dashes be equivalent to slashes
#Make regular expression tighter
    

#fix problems with May