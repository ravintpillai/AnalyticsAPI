import time
import sys
import io
import segmentIds
import dimensions_and_metrics
import collectArguments
import hello_analytics_api_v3_auth
from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError
import datetime
from datetime import datetime
service = hello_analytics_api_v3_auth.initialize_service()
accounts = service.management().accounts().list().execute()
this_number = 0

def get_results(profile_id, date):
    return service.data().ga().get(
        ids=profile_id,
        start_date=date,
        end_date=date,
        dimensions='ga:browser,ga:browserVersion',
        metrics='ga:visits,ga:transactions').execute()

def bring_sites_in():
    inputFile = open('g:\\.Customer Insight\\Analytics\\AnalyticsAPI\\Sites.csv','r')
    sites_profile_ids_array = []
    for line in inputFile:
        sites_profile_ids_array.append(line.strip('\n').split(','))
    return sites_profile_ids_array

def prepare_results_for_writing(results):
    global this_number
    try:
        for x in range (len(results['rows'])):
            my_new_result.append(results['rows'][x])
            my_new_result[this_number].append('ga:'+results['profileInfo']['profileId'])
            this_number+=1
    except:
        print 'failed',this_number

def get_profile_ids_for_query():
    new_list = []
    for sites_data in range (1,len(sites)):
        new_list.append(sites[sites_data][2])
    return new_list

def collect_all_results():
    global date
    global profile_ids
    for x in profile_ids:
        results = get_results(x,date)
        prepare_results_for_writing(results)

def write_all_results():
    outputFile = open('g:\\.Customer Insight\\#AnalyticsAPI\\browser_data.txt','w+')
    for x in my_new_result:
        for y in x:
            outputFile.write(y)
            outputFile.write('\t')
        outputFile.write('\n')
    outputFile.close()

def get_date():
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    Year = datetime.now().strftime('%Y')
    Month = datetime.now().strftime('%m')
    Day = datetime.now().strftime('%d')
    if int(Day) == 1:
        if Month == 1:
            YesterYear = int(Year)-1
            YesterMonth = 12
            YesterDay = 31
        else:
            YesterYear = Year
            YesterMonth = int(Month)-1
            YesterDay = months(YesterMonth)
		
    else:
        YesterYear = Year
        YesterMonth = Month
        YesterDay = int(Day) - 1

    if YesterMonth < 10:
        YesterMonth = '0'+str(YesterMonth)
    else:
        YesterMonth = str(YesterMonth)

    if YesterDay < 10:
        YesterDay = '0' + str(YesterDay)
    else:
        YesterDay = str(YesterDay)

    return str(YesterYear)+'-'+str(YesterMonth)+ '-' + str(YesterDay)
date = get_date()
my_new_result = []

sites = bring_sites_in()
profile_ids = get_profile_ids_for_query()
collect_all_results()
write_all_results()
