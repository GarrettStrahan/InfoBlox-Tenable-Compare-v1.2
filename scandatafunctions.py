import json, os, yaml, xlsxwriter, ipaddress, itertools, re, math
import datetime as dt
from tenable.sc import TenableSC

# FUNCTIONS TO CREATE
#Make a new function to add up IP addresses from CIDR ranges and IP ranges.









def merge_the_list_of_lists(list) -> list:
    #one of the different functions to try to remove list of list
    flat = []
    for i in list:
        for j in i:
            flat.append(j)
    return flat

def merge_the_list_of_lists2(list) -> list:
    #one of the different functions to try to remove list of list
    flat = []
    for i in list:
        flat.append(i)
    return flat

def merge_the_list_of_lists3(lists) -> list:
    #one of the different functions to try to remove list of list
    flat = itertools.chain.from_iterable(lists)
    print(list(flat))

    return list(flat)

data = ['CMG - Nessus Scanner 1', 'CMG - Nessus Scanner 2', 'Fidelis Care - Campus - prd-secapp0314', 'Fidelis Care - Campus - prd-secapp0315', 'Fidelis Care - Campus - prd-secapp0316', 'Fidelis Care - Campus - prd-secapp0317', 'Fidelis Care - Data Center - prd-secapp0310', 'Fidelis Care - Data Center - prd-secapp0311', 'Fidelis Care - Data Center - prd-secapp0312', 'Fidelis Care - Data Center - prd-secapp0313', 'HealthSmart Scanner', 'Nessus Scanner 01', 'Nessus Scanner 02', 'Nessus Scanner 03', 'Nessus Scanner 04', 'Nessus Scanner 05', 'Nessus Scanner 06', 'Nessus Scanner 07', 'Nessus Scanner 08', 'Nessus Scanner 09', 'Nessus Scanner 10', 'Nessus Scanner 11', 'Nessus Scanner 12', 'Nessus Scanner 13', 'Nessus Scanner 14', 'Nessus Scanner 15', 'Nessus Scanner 16', 'Nessus Scanner 49', 'Nessus Scanner 50', 'Nessus Scanner 54', 'Nessus Scanner 55', 'Nessus Scanner 56', 'Nessus Scanner 57', 'Nessus Scanner 58', 'Nessus Scanner 59', 'Nessus Scanner 60', 'Nessus Scanner 61', 'Nessus Scanner 62', 'Nessus Scanner 63', 'Nessus Scanner 64', 'Nessus Scanner 65', 'Nessus Scanner 78', 'Tenable.io Scanner', 'USMM - Nessus Scanner 1', 'USMM - Nessus Scanner 2', "['Ptnseapct13', 'Ptnseapct14', 'Tenable.io', 'dtnseapct01', 'dtnseapct02', 'dtnseapct03', 'minessus01-pva', 'mivvcs01-pva.caidan.local', 'ptnseapct01', 'ptnseapct02', 'ptnseapct03', 'ptnseapct04', 'ptnseapct05', 'ptnseapct06', 'ptnseapct07', 'ptnseapct08', 'ptnseapct09', 'ptnseapct10', 'ptnseapct11', 'ptnseapct12', 'ptnseapct15', 'ptnseapct16']", "['Nessus Scanner 17', 'Nessus Scanner 18', 'Nessus Scanner 19', 'Nessus Scanner 20', 'Nessus Scanner 21', 'Nessus Scanner 22', 'Nessus Scanner 23', 'Nessus Scanner 24', 'Nessus Scanner 25', 'Nessus Scanner 26', 'Nessus Scanner 27', 'Nessus Scanner 28', 'Nessus Scanner 29', 'Nessus Scanner 30', 'Nessus Scanner 31', 'Nessus Scanner 32', 'Nessus Scanner 33', 'Nessus Scanner 34', 'Nessus Scanner 35', 'Nessus Scanner 36', 'Nessus Scanner 37', 'Nessus Scanner 38', 'Nessus Scanner 39', 'Nessus Scanner 40', 'Nessus Scanner 41', 'Nessus Scanner 42', 'Nessus Scanner 43', 'Nessus Scanner 44', 'Nessus Scanner 45', 'Nessus Scanner 46', 'Nessus Scanner 47', 'Nessus Scanner 48', 'Nessus Scanner 51', 'Nessus Scanner 52', 'Nessus Scanner 77', 'Tenable.io Scanner']", "['Fidelis Care - Campus - prd-secapp0314', 'Fidelis Care - Campus - prd-secapp0315', 'Fidelis Care - Campus - prd-secapp0316', 'Fidelis Care - Campus - prd-secapp0317', 'Fidelis Care - Data Center - prd-secapp0310', 'Fidelis Care - Data Center - prd-secapp0311', 'Fidelis Care - Data Center - prd-secapp0312', 'Fidelis Care - Data Center - prd-secapp0313', 'Nessus Scanner 53', 'Nessus Scanner 67', 'Tenable.io Scanner']"]

def flatten_list(data): #Function to try to elimate list of lists, variable issue
    flat_list = []
    # iterating over the data
    for element in data:
        # checking for list
        if type(element) == list:
            # calling the same function with current element as new argument
            flatten_list(element)
        else:
            flat_list.append(element)

    return flat_list

# data2 = flatten_list(data)
data2 = merge_the_list_of_lists3(data)
print(f"data = {data2}")


def remove_dot_in_list(ofl_scr) -> list:
    #The puporse of this function is to remove all the . dot symbols, the interrupter is picking the strings with dots as a float variable which is crashing xslxwriter.
    new_ofl_scr = []
    temp_name = "test"
    x = 0
    for ofl_scr1 in ofl_scr:
        temp_name = "test"
        temp_name = str(ofl_scr[x])
        temp_name.replace('.', '')
        new_ofl_scr.append(temp_name)
        x = x + 1
    return new_ofl_scr


def ip_combiner(ofl_ip_List, ofl_ip_List2, ofl_ip_List3, ofl_ip_List4, ofl_ip_List5, ofl_ip_List6) -> list:
#This will add up all the ip_list to give you a total ip list # for each scanner
    x = 0
    iptotal = []
    for new_ip_list in ofl_ip_List:
        iptotal.append(ofl_ip_List[x] + ofl_ip_List2[x] + ofl_ip_List3[x] + ofl_ip_List4[x] + ofl_ip_List5[x] + ofl_ip_List6[x])
        x = x + 1

    return iptotal



def make_timestamp() -> str:
    """
    Generates a TenableSC friendly string for the start date/time of a scan.
    Date is variable, time time is always 10PM Central.
    :return: Date/Time string.
    """
    return f"TZID=America/Chicago:{dt.datetime.today().strftime('%Y.%m.%d.')}T220000" #Centene HQ is in MO so we are using Chicago instead of EST


def get_extra_scanzone_names(sc: TenableSC, scan_zone_IDs) -> list:
#This gets the scan zone names in scan zone areas levels 2-6
#This Will work if there is no extra scan zone in that tier, PLEASE CONFIRM AND STATE IN THIS COMMENT SECTION, THERE IS NO TRY/EXCEPT CLAUSE
    list = []
    x = 0
    print(f"scanner_IDs = {scan_zone_IDs}")
    for new_scanner_IDs in scan_zone_IDs:
        if scan_zone_IDs[x] == 0:
            list.append("None!")
            print("The IF statement worked")
            x = x + 1
        else:
            scanners = sc.scan_zones.details(scan_zone_IDs[x], fields=['name'])
            print(f"scanners has this data inside it {scanners} and the type is ", type(scanners))
            scanners = dict(scanners)
            scanners.pop("id")
            print(f"scanners NOW has this data inside it {scanners} and the type is ", type(scanners))
            scanners = str(scanners)
            scanners = scanners.replace("{'name': '", "")
            scanners = scanners.replace("'}", "")
            print(f"scanners NOW has this data inside it when using replace: {scanners} and the type is ",
                  type(scanners))
            list.append(scanners)
            x = x + 1
    return list

def get_extra_scanzone_namesWLC(sc: TenableSC, scan_zone_IDs) -> list:
#This gets the scan zone names in scan zone areas levels 2-6
#This Will work if there is no extra scan zone in that tier, PLEASE CONFIRM AND STATE IN THIS COMMENT SECTION, THERE IS NO TRY/EXCEPT CLAUSE
    list = []
    x = 0
    print(f"scanner_IDs = {scan_zone_IDs}")
    for new_scanner_IDs in scan_zone_IDs:
        if scan_zone_IDs[x] == 0:
            list.append("None!")
            print("The IF statement worked")
            x = x + 1
        else:
            scanners = sc.scan_zones.details(scan_zone_IDs[x], fields=['name'])
            print(f"scanners has this data inside it {scanners} and the type is ", type(scanners))
            scanners = dict(scanners)
            print(f"WLC, Scanners is this long, length = {len(scanners)}")
            scanners.pop("id")
            print(f"scanners NOW has this data inside it {scanners} and the type is ", type(scanners))
            scanners = str(scanners)
            scanners = scanners.replace("{'name': '", "")
            scanners = scanners.replace("'}", "")
            print(f"scanners NOW has this data inside it when using replace: {scanners} and the type is ",
                  type(scanners))
            list.append(scanners)
            x = x + 1
    return list


def get_all_2nd_scanzone_ids(sc, scanner_IDs) -> list:
    #Will work if no 2nd level Scan Zone
    #This will get ALL the scqanzone ID #s
    x = 0
    newScannerlist = []

    try:
        for temp_IDs in scanner_IDs:
            print(f"x = {x}")
            newScannerlist.append(get_2nd_scanzone_id(sc, scanner_IDs[x]))
            x = x + 1
    except:
        for new_tempIDs in scanner_IDs:
            newScannerlist.append("0")
        print("You are in except clause, meaning there is no 2nd scan zone for this scanner!")

    print(f"Here is the list of 2nd scanner_IDs: {newScannerlist}")
    return newScannerlist

def get_2nd_scanzone_id(sc: TenableSC, scanner_ID) -> int:
    #Will work if no 2nd level Scan Zone
    #This gets a specific scanzone ID and it works with the function get_all_2nd_scanzone_ids
    list = ["test1", "test2"]

    try:
        for zone in sc.scanners.details(scanner_ID)['zones']:
            list.append(zone['id'])
        second_scn_zone = list[3]

        print("There is a 4th scan zone in this scanner!")
    except:
        second_scn_zone = 0
        second_scn_zone = int(second_scn_zone)
        print("You are in except clause, meaning there is no 2nd scan zone for this scanner!")
        print(f"second_scn_zone = {second_scn_zone} and type = ", type(second_scn_zone))

    print(f"At the end of the function get_2nd_scanzone_id, the Variable list = {second_scn_zone}, and the type is ", type(second_scn_zone))
    return second_scn_zone


def get_3rd_scanzone_id(sc: TenableSC, scanner_ID) -> int:
    #Will work if no 3rd level scan zone exists
    #Get a single 3rd scan zone ID. this is for
    list = ["test1", "test2"]
    try:
        for zone in sc.scanners.details(scanner_ID)['zones']:
            list.append(zone['id'])
        third_scn_zone = list[4]

        print("There is a 3rd scan zone in this scanner!")
    except:
        third_scn_zone = 0
        third_scn_zone = int(third_scn_zone)
        print("You are in except clause, meaning there is no 3rd scan zone for this scanner!")
        print(f"third_scn_zone = {third_scn_zone} and type = ", type(third_scn_zone))

    print(f"At the end of the function get_3rd_scanzone_id, the Variable list = {third_scn_zone}, and the type is ", type(third_scn_zone))
    return third_scn_zone

def get_all_3rd_scanzone_ids(sc, scanner_IDs) -> list:
#This will work if there is no 3rd level scan zone area in that Tier
#This gets all the 3rd level scan zone IDs
    x = 0
    newScannerlist = [5, 9]
    try:
        for temp_IDs in scanner_IDs:
            print(f"x = {x}")
            newScannerlist.append(get_3rd_scanzone_id(sc, scanner_IDs[x]))
            x = x +1
    except:
        for temp_IDs in scanner_IDs:
            print(f"x = {x}")
            newScannerlist.append('0')
            x = x +1
    del newScannerlist[0]
    del newScannerlist[0]
    print(f"Here is the list of 3rd scanner_IDs: {newScannerlist}")
    return newScannerlist


def get_4th_scanzone_id(sc: TenableSC, scanner_ID) -> int:
#this gets a single scan zone ID and works with get_all_4th_scanzone_ids() function
#this should work if there is no 4th level scan zone
    list = ["test1", "test2"]
    try:
        for zone in sc.scanners.details(scanner_ID)['zones']:
            list.append(zone['id'])
        fourth_scn_zone = list[5]
        print("There is a 4th scan zone in this scanner!")
    except:
        fourth_scn_zone = 0
        fourth_scn_zone = int(fourth_scn_zone)
        print("You are in except clause, meaning there is no 4th scan zone for this scanner!")
        print(f"fourth_scn_zone = {fourth_scn_zone} and type = ", type(fourth_scn_zone))

    print(f"At the end of the function get_4th_scanzone_id, the Variable list = {fourth_scn_zone}, and the type is ", type(fourth_scn_zone))
    return fourth_scn_zone


def get_all_4th_scanzone_ids(sc, scanner_IDs) -> list:
#This gets all the scan zone IDs for the 4th level of scan zone IDs
#This Will work with non-4th level scan zone tiers
    x = 0
    newScannerlist = [5, 9]
    try:
        for temp_IDs in scanner_IDs:
            print(f"x = {x}")
            newScannerlist.append(get_4th_scanzone_id(sc, scanner_IDs[x]))
            x = x +1
    except:
        for temp_IDs in scanner_IDs:
            print(f"x = {x}")
            newScannerlist.append('0')
            x = x + 1
    del newScannerlist[0]
    del newScannerlist[0]
    print(f"Here is the list of 4th scanner_IDs: {newScannerlist}")
    return newScannerlist


def get_all_5th_scanzone_ids(sc, scanner_IDs) -> list:
#This gets all the scan zone IDs for the 5th level of scan zone IDs
#This Will work with non-5th scan zone tiers
    x = 0
    newScannerlist = [5, 9]

    try:
        for temp_IDs in scanner_IDs:
            print(f"x = {x}")
            newScannerlist.append(get_5th_scanzone_id(sc, scanner_IDs[x]))
            x = x + 1
    except:
        for temp_IDs in scanner_IDs:
            print(f"x = {x}")
            print("You are in except clause, meaning there is no 5th scan zone for this scanner!")
            newScannerlist[x].append("0")
            x = x + 1

    del newScannerlist[0]
    del newScannerlist[0]
    print(f"Here is the list of 4th scanner_IDs: {newScannerlist}")
    return newScannerlist


def get_5th_scanzone_id(sc: TenableSC, scannerID) -> int:
#This Will work if there is no 5th level scan zone area
#This gets a single scan zone ID and works with get_all_5th_scanzone_ids() function.

    list = ["test1", "test2"]

    try:
        for zone in sc.scanners.details(scannerID)['zones']:
            list.append(zone['id'])
        fifth_scn_zone = list[6]
        print("There is a 5th scan zone in this scanner!")
    except:
        fifth_scn_zone = 0
        fifth_scn_zone = int(fifth_scn_zone)
        print("You are in except clause, meaning there is no 5th scan zone for this scanner!")
        print(f"fifth_scn_zone = {fifth_scn_zone} and type = ", type(fifth_scn_zone))

    print(f"At the end of the function get_5th_scanzone_id, the Variable fifth_scn_zone = {fifth_scn_zone}, and the type is ", type(fifth_scn_zone))
    return fifth_scn_zone


def get_6th_scanzone_id(sc: TenableSC, scannerID) -> int:
    #This Will work even if there is no 6th scan zone ID
    #This gets a single scanzone_ID and works with get_all_6th_scanzone_ids() function.
    list = ["test1", "test2"]
    try:
        for zone in sc.scanners.details(scannerID)['zones']:
            list.append(zone['id'])
        sixth_scn_zone = list[7]
        print("There is a 6th scan zone in this scanner!")
    except:
        sixth_scn_zone = 0
        sixth_scn_zone = int(sixth_scn_zone)
        print("You are in except clause, meaning there is no 6th scan zone for this scanner!")
        print(f"sixth_scn_zone = {sixth_scn_zone} and type = ", type(sixth_scn_zone))

    print(f"At the end of the function get_6th_scanzone_id, the Variable sixth_scn_zone = {sixth_scn_zone}, and the type is ", type(sixth_scn_zone))
    return sixth_scn_zone


def get_all_6th_scanzone_ids(sc, scanner_IDs) -> list:
#This will work with if there is no 6th level scan zone IDs
#This gets all the 6th level scan zone IDs
    x = 0
    newScannerlist = [5, 9]

    try:
        for temp_IDs in scanner_IDs:
            print(f"x = {x}")
            newScannerlist.append(get_6th_scanzone_id(sc, scanner_IDs[x]))
            x = x + 1
    except:
        print("You are in the except clause, meaning there is no 6th scan zone IDs")
        for temp_IDs in scanner_IDs:
            newScannerlist[x].append("0")
            x = x + 1

    del newScannerlist[0]
    del newScannerlist[0]
    print(f"Here is the list of 4th scanner_IDs: {newScannerlist}")
    return newScannerlist


def get_scanner_list_names(sc: TenableSC) -> list:
#    Get a list of scanner's names from TenableSc
#    :param sc: The TenableSC console on which to look.
#    :return: A list of Scanner Names

    scanners = sc.scanners.list() #This function gets json data for all the scanners
    print(f"get_scanner_list scanners has this data {scanners}")
    parsedName = []
    x = 0

    for i in scanners:
        if scanners[x]['name']: #Search for the scanner name in the json response from tenable
            parsedName.append(scanners[x]['name']) #This function gets the Scanner names and puts them into a list variable.
            x = x + 1

    print(f"get_scanner_list returns with this data {parsedName}")
    return parsedName


def get_scanner_id(sc: TenableSC) -> list:
    #    Get a list of scan IDs for a TenableSc console based on scan name.
    #    :param sc: The TenableSC console on which to look.
    #    :return: A list of Scanners

    scanners = sc.scanners.list()
    ids = []
    x = 0
    print(f"get_scanner_id has this data {scanners}")
    for i in scanners:
        if scanners[x]['id']:
            ids.append(scanners[x]['id'])
            x = x + 1

    print(f"get_scanner_id returns with this data {ids}")
    return ids


def get_scanner_zone_id(sc: TenableSC, id) -> list:
#    :param sc: The TenableSC console on which to look.
#    :param id: Scanner ID #s
#    :return: A list of Scanner's zone IDs
    x = 0
    # ids = ["deleteme", "delete"]
    ids = []

    for idnumber in id:
        scanners = sc.scanners.details(id[x], fields=['zones']) #check on the first variable
        print(f"In get_scanner_zoneid function loop, variable scanners = {scanners} and the type is ", type(scanners))
        scanners = str(scanners)
        scanners = scanners.split()
        print(f"scanners[4] = {scanners[4]}") #DING DING DING This is the scan zone ID #
        scanners = scanners[4]
        scanners = scanners.replace(",", " ")
        print(f"In get_scanner_zoneid function loop, ALTERED variable scanners = {scanners} and the type is ", type(scanners))
        x= x + 1
        print(scanners)
        print("len return = ")
        scanners = scanners[1:]
        scanners = scanners[:-2]
        print(f"scanners = {scanners}")
        print(len(scanners))
        print(scanners.isnumeric())
        ids.append(scanners)

        print(f"get_scanner_zone_id, Variable: scanners, {scanners} and the type is ", type(scanners))
        print(f"get_scanner_zone_id, Variable: ids, {ids} and the type is ", type(ids), " This is what is returned")

        return ids


def turn_scanner_id_2_scan_zone(sc: TenableSC, ids) -> list:
#   :param sc: The Tenables required variable to login to Tenable servers and do its magic.
#   :param rco_ids: The list of ids for the scanners.
#   This function turns the IDs into a list of scan_zone names, it does this by getting a dictionary value back from sc.scanners.details(x) then scans for the dictionary value of "zones" then converts this data to a string type and then splits it by white characters then you take the 3rd key in this which is the scan zone name then strips off the worthless characters.
#   :return: A list of the counted IP addresses.

    v = 0
    scan_zone_name = [] #this was needed to allow the python interrupter to know this is a list, otherwise it was crashing.

    for new_ids in ids: #purpose of this is to go through the list of ids get the scanner dictionary values then convert it to actual name then put that value into variable list scan_zone_name, cant be this one
        new_int = ids[v]
    #    print(f"Variable: new_int. The value of this = {new_int} The type is : ", type(new_int))
    #    print(f"Variable: ids. The value of this = {ids} The type is : ", type(ids))
        scanners = sc.scanners.details(new_int)
        scan_zone_name_temp = liststripper(scanners) #THIS SCAN_ZONE_TEMP WILL TAKE THE RESULTS AND APPEND IT TO scan_zone_name
        scan_zone_name.append(scan_zone_name_temp) #this attaches all the temp scan zone name information to the variable we are returning.

    #    print(f"Variable: scan_zone_name_temp. The value of this = {scan_zone_name_temp} The type is : ", type(scan_zone_name_temp))
    #    print(f"Variable: scan_zone_name. The value of this = {scan_zone_name} The type is : ", type(scan_zone_name))
        print(f"v= {v}")
        v = v + 1 #this loop counter is for your convience to know where you are in the loop AND for going through the list of IDs.

    print(f"The list variable scan_zone_name has these values {scan_zone_name}")
    print(f"Out of the Loop, here is the value of scan_zone_name {scan_zone_name} and type = ", type(scan_zone_name))

    return scan_zone_name

def checkforgarbage(list_with_garbage) -> list:
    remove1 = ' "'
    remove2 = " '"
    remove3 = "'"
    remove4 = '"'

    new_list = [s.replace(remove1, "") for s in list_with_garbage]
    new_list = [s.replace(remove2, "") for s in list_with_garbage]
    new_list = [s.replace(remove3, '') for s in list_with_garbage]
    new_list = [s.replace(remove4, '') for s in list_with_garbage]
#get rid of, start of line:
# "
# '
#end of line
#'"
#'
    return new_list


def checkforgarbage2(list_with_garbage) -> list:
    remove1 = ' "'
    remove2 = " '"
    remove3 = "'"
    remove4 = '"'


    for s in list_with_garbage:
        new_list = s.replace(remove1, "")
        new_list = s.replace(remove2, "")
        new_list = s.replace(remove3, "")
        new_list = s.replace(remove4, "")

    return new_list

def checkforgarbage3(list_with_garbage) -> list:
    remove1 = r' "'
    remove2 = r" '"
    remove3 = r"'"
    remove4 = r'"'


    for s in list_with_garbage:
        new_list = s.replace(remove1, "")
        new_list = s.replace(remove2, "")
        new_list = s.replace(remove3, "")
        new_list = s.replace(remove4, "")

    return new_list


def remove_duplicates(list):
    return list(dict.fromkeys(list))


def remove_empty_strings_from_list(list) -> list: #The job is to remove any elements in lists that have nothing in the elements.
    print("remove_empty_strings_from_list(list) function is running")
    while ("" in list):
        list.remove("")
    return list


def get_scan_zone_IPs(sc: TenableSC, scan_zone_IDs) -> list:
    #   :param sc: The Tenables required variable to login to Tenable servers and do its magic
    #   :param ids: The list of ids for the Scan Zone Areas needed to get the IP address information
    #   This function turns the IDs into a list of scan_zone names, it does this by getting a dictionary value back from sc.scanners.details(x) then scans for the dictionary value of "zones" then converts this data to a string type and then splits it by white characters then you take the 3rd key in this which is the scan zone name then strips off the worthless characters
    #    :return: ip_list which has all the ip addresses listed.
    x = 0
    ip_list = []

    try:
        for new_ids in scan_zone_IDs: #purpose of this is to go through the list of ids get the scanner's IP lists
            print(f"new_ids = {new_ids} and the type is", type(new_ids))
            scanners = sc.scan_zones.details(new_ids, fields=['ipList'])
            # print(f"What is in new_ids: {new_ids}")
            print(f"BEFORE: What is in scanners HADOUKEN: {scanners}")
            scanners = str(scanners)
            scanners = scanners[12:] #this strips off the first 11 junk characters from the string.
            scanners = scanners[:-13] #this strips off the last 12 junk characters from the string.
            print(f"AFTER: What is in scanners HADOUKEN: {scanners}")
            scanners.replace(",", ", ") #EXPERIMENTAL!!!!!!! Tiger Punch lol
            print(f"AFTER space change: What is in scanners HADOUKEN: {scanners}")
            # ip_list.append(ipcounted) #this is for vlads Script, there is no need to count as far as I believe.
            x = x + 1

    except:
        if scan_zone_IDs[x] == 0:
            ip_list.append('0')
            x = x + 1
        if scan_zone_IDs[x] == 'None!':
            ip_list.append(('0'))
            x = x + 1

    return scanners

def iprangeConvert(ip_list):
    #   :param ip_list: The list of IP information for the function to calculate the IP addresses in a counted format.
    #   This function turns the IP addresses into a counted number.
    #    :returns result_set, which is the counted number of IP addresses.

    result_set = set()
    # I found this in some places, and it's stupid, so I just remove it
    if '239.0.0.0/8' in ip_list:
        ip_list.remove('239.0.0.0/8')
    # Now start to iterate over the provided list
    for item in ip_list:
        try:
            # If this cidr makes it into the list, just remove it otherwise it will take forever to return.
            if item == '0.0.0.0/0':
                ip_list.remove('0.0.0.0/0')
            elif item == '0.0.0.0-255.255.255.255':
                ip_list.remove('0.0.0.0-255.255.255.255')
            # Similarly, if a full RF1918 block is in the list, just remove it because it's probably wrong and it will take ages.
            elif item in ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16']:
                ip_list.remove(item)
            # If some ranges is passed in with an invalid IP, having more than 3 characters, remove it from the list (I saw this somewhere)
            elif '-' in item and len(item.split('-')[0].split('.')[0]) > 3:
                ip_list.remove(item)
            # If the item in the list has a '-', its an IP range
            elif '-' in item:
                item = item.split('-')
                # Added this logic because I noticed that sometimes people didn't include the network and broadcast addresses. This is to normalize that.
                if item[0].split('.')[3] == '1' and item[-1].split('.')[3] == '254':
                    item[0] = '.'.join(item[0].split('.')[:3]) + '.0'
                    item[-1] = '.'.join(item[-1].split('.')[:3]) + '.255'
                # Grab the first ip in the range, and last ip in the range and pass it to the findIPs() function to get all the IPs in that range
                startip = ipaddress.IPv4Address(item[0])
                endip = ipaddress.IPv4Address(item[-1])
                ips = findIPs(startip, endip)
                result_set.update(ips)
            # If the item has a / in it, it's a cidr notated block. Also, sometimes people were providing IP addresses as if they were adding it to a NIC using the format
            # 10.1.1.5/24 which is incorrect for this use case, so I assume they intended to add just that single IP. So I just take the IP and strip the cidr bit
            elif '/' in item and (int(item.split('.')[3].split('/')[0]) > 0) and (
                    int(item.split('.')[3].split('/')[1]) <= 24):
                result_set.add(item.split('/')[0])
            # I saw this CIDR which is wrong, so im skipping that for now and getting all possible IPs in the cidr
            elif '/' in item and item != '192.168.1.0/23':
                result_set.update([str(ip) for ip in ipaddress.IPv4Network(item)])
            # If its this stupid cidr, format it to make sense.
            elif item == '192.168.1.0/23':
                startip = ipaddress.IPv4Address('192.168.0.0')
                endip = ipaddress.IPv4Address('192.168.2.255')
                cidr = [ipaddr for ipaddr in ipaddress.summarize_address_range(startip, endip)][0]
                ips = [str(ip) for ip in ipaddress.IPv4Network(str(cidr))]
                result_set.update(ips)
            else:
                result_set.add(item)
        except:
            # print(item)
            continue
    results.update(result_set)
    # return all the IPs calculated
    return result_set

results = set()


def liststripper(scanners): #This works with turn_scanner_id_2_scan_zone to simplify its original purpose
    #   :param scanners: The list of scan zone area names with junk in it.
    #   This function cleans up the scan zone area names into a human readable format.
    #    :returns scan_zone_name, a list of scan zone area names that is in human readable format.

    scanner_data = []

    if scanners['zones']:  #looks for the zone field
        scanner_data.append(scanners['zones']) #takes the dictionary key and puts it into scanner_data variable

    print(f"scanner_data has these values {scanner_data}. The type is : ", type(scanner_data))
    new_scanner_data = scanner_data[0]
    new_scanner_data2 = str(new_scanner_data)
    new_scanner_data2 = str.split(new_scanner_data2) #changing this to the same variable see if it works. data3 to data2
#    print(new_scanner_data2)
    scan_zone_name = new_scanner_data2[3] #changing this to data3 to data2
    scan_zone_name = scan_zone_name.rstrip("',") #cleans up the string data.
    scan_zone_name = scan_zone_name.lstrip("'") #cleans up the string data.
#    print(f"now Variable: scan_zone_name = {scan_zone_name}. The type is : ", type(scan_zone_name))
    return scan_zone_name


#These functions below before the !!!!!! line is OFL only functions, well they used to be. Now they are used in WLC as well. Something must have change in WLC
#The reason these functions are needed is that when you do a scanner information pull request from Tenables it gives you the disabled Scanners as well and if you do that the data in Scan Zone Area ID + IP + name is blank and will cause a crash

def ofl_get_scanner_zone_id(sc: TenableSC, id) -> list:
#    :param sc: The TenableSC console on which to look.
#    :param id: Scanner ID #s
#    :return: A list of Scanner's zone IDs
    print("OFL_GET_SCANNER_ZONE_ID FUNCTION IS RUNNING")
    x = 0
    ids = [] #This is to make sure ids is a list and script does not crash and not does not become a string

    for idnumber in id:
        scanners = sc.scanners.details(id[x], fields=['zones']) #check on the first variable
        print(f"OFL!!! In get_scanner_zoneid function loop, variable scanners = {scanners} and the type is ", type(scanners))
        scanners = str(scanners) #turns the dictionary variable into a string
        scanners = scanners.split() #turns the string into a list
        try: #without this statement the python interrupter will crash, the reason OFL has a bunch of scanners that are user disabled that contain no scan zone areas, no data in scan zone area = crash.
            scanners = scanners[4] #this string element contains the scan zone ID.
            scanners = scanners.replace(",", " ") #cleans up the data
            scanners = scanners[1:] #remove the first character from the string
            scanners = scanners[:-2]  #remove the last two character from the string
        except:
            scanners = 4 #this is so the program does not crash, it will put bogus IP information in the disabled scanners but we don't care about these scanners.

        print(f"OFL!!! In get_scanner_zoneid function loop, ALTERED variable scanners = {scanners} and the type is ", type(scanners))
        x= x + 1
        print(f"OFL!!! scanners = {scanners}")
        ids.append(scanners)

    print(f"get_scanner_zone_id, Variable: scanners, {scanners} and the type is ", type(scanners))
    print(f"get_scanner_zone_id, Variable: ids, {ids} and the type is ", type(ids), " This is what is returned")

    return ids


def ofl_turn_scanner_id_2_scan_zone(sc: TenableSC, ids) -> list:
#   :param sc: The Tenables required variable to login and do its magic
#   :param rco_ids: The list of ids for the scanners
#   This function turns the IDs into a list of scan_zones, it does this by getting a dictionary value back from sc.scanners.details(x) then scans for the dictionary value of "zones" then converts this data to a string type and then splits it by white characters then you take the 3rd key in this which is the scan zone name then strips off the worthless characters
#    :return: A list of Scanners

    print("OFL_TURN_SCANNER_ID_2_SCAN_ZONE FUNCTION IS RUNNING")
    v = 0
    # scan_zone_name = ["removeme1", "removeme2"] #original
    scan_zone_name = []

    for new_ids in ids: #purpose of this is to go through the list of ids get the scanner dictionary values then convert it to actual name then put that value into variable list scan_zone_name, cant be this one
        new_int = ids[v]
        # print(f"Variable: new_int. The value of this = {new_int} The type is : ", type(new_int))
        # print(f"Variable: ids. The value of this = {ids} The type is : ", type(ids))
        scanners = sc.scanners.details(new_int)
        scan_zone_name_temp = ofl_liststripper(scanners) #THIS SCAN_ZONE_TEMP WILL TAKE THE RESULTS AND APPEND IT TO scan_zone_name
        scan_zone_name.append(scan_zone_name_temp)

        # print(f"Variable: scan_zone_name_temp. The value of this = {scan_zone_name_temp} The type is : ", type(scan_zone_name_temp))
        # print(f"Variable: scan_zone_name. The value of this = {scan_zone_name} The type is : ", type(scan_zone_name))
        print(f"v= {v}")
        v = v + 1

    # print(f"The list variable scan_zone_name has these values {scan_zone_name}")
    print(f"Out of the Loop, here is the value of scan_zone_name {scan_zone_name} and type = ", type(scan_zone_name))

    return scan_zone_name

#Also a OFL only function
def ofl_liststripper(scanners):
   #This works with turn_scanner_id_2_scan_zone to simplify its original purpose, I seem to get different results from OFL from the list variables. So this function is only for OFL, ill need to create a ofl_turn_scanner_id_2_scan_zone(x, x)

    scanner_data = []

    if scanners['zones']:  #looks for the zone field
        scanner_data.append(scanners['zones']) #takes the dictionary key and puts it into scanner_data variable

    print(f"scanner_data has these values {scanner_data}  The type is : ", type(scanner_data))
    new_scanner_data = scanner_data #new_scanner_data = scanner_data[0] ORIGINALLY
    new_scanner_data2 = str(new_scanner_data)
    new_scanner_data2 = str.split(new_scanner_data2) #changing this to the same variable see if it works. data3 to data2
#    print(new_scanner_data2)
    scan_zone_name = str(new_scanner_data2)#[3] #changing this to data3 to data2

    if scan_zone_name == "['[]']": #this is for the disabled scanners that do not have scan zone area data
        print("We found a match with no scan zone area data")
        scan_zone_name = ["Delete me", "Get rid of me", "Garbage", "Disabled Scanner"] #this is to fill in the empty scan zone data or else it crashes.
    else:
        scan_zone_name = str.split(scan_zone_name)

    scan_zone_name = scan_zone_name[3] #this element in the list is the scan zone name information

    scan_zone_name = scan_zone_name.replace(",", "") #removing all the junk characters
    scan_zone_name = scan_zone_name.replace("'", "") #removing all the junk characters
    scan_zone_name = scan_zone_name.replace('"', "") #removing all the junk characters
    scan_zone_name.rstrip(",") #This is not working, try later
    scan_zone_name.lstrip("'") #This is not working, try later
    return scan_zone_name


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#ALL THE FUNCTIONS BELOW ARE PROBABLY NOT GOING TO BE USED BUT KEPT JUST IN CASE I NEED THEM AT A FUTURE DATE
'''
def get_scan_zones(sc: TenableSC, ids) -> list:
    """
    Retrieves the list of scan zone definitions.
    :param sc: The TenableSC console on which to look.
    :return: A list of scan IDs
    """
    print("We are in get_scan_zones function")
    #    zones = []
    #    scans = sc.scan_zones.list()
    for zone in sc.scan_zones.details(ids):  # this will go through the lists of data and output to the screen
        #       if name in scan['name']:
        #           ids.append(scan['id'])
        print(
            "We are in get_scan_zones loop function, next line will output scan zone data. This information will not be outputted to your terminal screen")
        print(zone)  # outputing the zone data
        print("END OF DATA AND ZONE DATA, AFTER THIS IS A NEW DATA FIELD!")
    return zone  # this will put the data into rco_zones (1st), ofl_zones (2nd), & buf_zones (3rd)

def get_scan_ids(sc: TenableSC, name: str) -> list:
    """
    Get a list of scan IDs for a TenableSc console based on scan name.
    :param sc: The TenableSC console on which to look.
    :param name: The scan name as a string
    :return: A list of scan IDs
    """
    ids = []
    scans = sc.scans.list()
    for scan in scans['usable']:
        if name in scan['name']:
            ids.append(scan['id'])
    return ids

def get_scan_details(sc: TenableSC, scan_id: int) -> dict:
    """
    Gather the scan configuration details by scan ID.
    :param sc: The TenableSC console on which the scan resides.
    :param scan_id: The scan ID as an integer.
    :return: A dictionary of the scan's details, see "fields" for what dict contains.
    """
    scan_details = sc.scans.details(scan_id, fields=['name', 'rolloverType', 'maxScanTime', 'settings', 'schedule'])
    return scan_details
#If You Need Them, un-comment this area
    
    '''

''' not in use
def debugging(sc: TenableSC): #NOT USING THIS #debugging purposes #THIS GETS THE SCAN ZONE IDs WITH REGULAR EXPRESSION, YOUR NOT USING THIS ONE!!!
    r = 31
    # x = 0
    ids = ["test1", "test2"]
    fields = ['zones']
    scanners = sc.scanners.details(31, ['zones'])
    print(f"scanners = {scanners}")
    scanners = str(scanners)
    scanners = scanners.replace("'", "")
    scanners = scanners.replace(":", "")
    scanners = scanners.replace(" ", "")
    print(f"scanners = {scanners}")

    scanners2 = scanners
    scanners2 = re.findall(r'[i][d]\d\d', scanners2)
    scanners2 = scanners2[1:]  # this strips off the first 11 junk characters from the string.
    print(f"scanners2 = {scanners2}")
    print(f"DEBUGGER! with zones field, scanner = {scanners2}", type(scanners))
'''

#Not using these below functions any longer but ill keep them just in case I want to use them, problem is that the returning object thinks its a int instead of a string and when interate through and make sure turn them all into a string it still thinks it is.

# def combineScanZoneName_ScanZoneID_IP(scan_zone_name, scan_zone_ID, ipNumber) -> list:
# #   combines Scan Zone Area Name + Scan Zone Area ID # + IP count for that Scan Zone Area
# # This is causing you too much trouble, removing it soon!!!
#     x = 0
#     for temp_SCN in scan_zone_name:
#         scan_zone_name[x] = scan_zone_name[x] + "/" + scan_zone_ID + "/" + ipNumber
#
#     return  scan_zone_name
#
#
# def combineScannerName_ScannerID(scannerName, scannerID) -> list:
#     #Getting rid of this function, shortly.
#     #This is Not in use, BUT IT IS FOR THE SCANNER FIELD, PUT IT TO USE WHEN YOU GET TIME!
#     #This combines Scanner Name with its Scanner ID # to be able to put in one field in a spreadsheet
#     x = 0
#     print("combineScannerName_ScannerID function is running")
#     for tempScName in scannerName:
#         scannerName[x] = scannerName[x] + " / " + scannerName[x]
#         x = x + 1
#     return scannerName
#
#
# def combineScanZoneName_ScanZoneID(scanzonename, scanzoneID, ipNumber) -> list: #You wont need different function calls for different scan zone area names
#     #this function causes more problems than it solves! GET RID OF IT!
#     #this combines Scanner Zone Name with its Scanner Zone ID # to be able to put in one field in a spreadsheet
#     x = 0
#     # print("combineScanZoneName1_ScanZoneID1 function is running")
#     # print(f"scanzonename[0] = {scanzonename[0]} and the type is ", type(scanzonename[0]), " and the len is ", len(scanzonename))
#     # print(f"scanzoneID[0] = {scanzoneID[0]} and the type is ", type(scanzoneID[0]), " and the len is ", len(scanzoneID))
#     # print(f"ipNumber[0] = {ipNumber[0]} and the type is ", type(ipNumber[0]), " and the len is ", len(ipNumber))
#
#     print(f"scanzonename = ************ {scanzonename}")
#
#
#     newreturn = ["test", "test2"]
#     newname = []
#
#     for tempScZName in scanzonename:
#         newipNumber = str(ipNumber[x])
#         newscanzoneID = str(scanzoneID[x])
#         newipNumber.rjust(1)
#         newipNumber.ljust(1)
#         newscanzoneID.rjust(1)
#         newscanzoneID.ljust(1)
#         print(f"newipNumber = {newipNumber} and the type is ", type(newipNumber))
#
#         newname = scanzonename[x] + "/" + newscanzoneID + "/" + newipNumber
#         print(f"x = {x} AND newreturn = {newreturn}")
#         newreturn.append(newname)
#
#         x = x + 1
#     return newreturn