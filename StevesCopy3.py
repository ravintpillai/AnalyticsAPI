#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import sys
import io
import segmentIds
import dimensions_and_metrics
import collectArguments
#import the Auth Helper class
import hello_analytics_api_v3_auth
from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError
globalOutputList = []
dateList = collectArguments.getDates()
date1 = dateList[0]
date2 = dateList[1]
filename = collectArguments.getFilename()
myNewFile = open (filename , 'w+')
checkList = ['Profile', 'H - SendIt', 'A - Zavvi', 'A - TheHut.com', 'H - zavvi.es', 'H - mybag.com', 'J - iwantoneofthose.com', 'H - zavvi.nl', 'H - allsole.com', 'www.hqhair.com/', 'ttp://www.myprotein.com/uk/', 'www.mankind.co.uk', 'www.beautyexpert.co.uk', 'www.lookfantastic.com', 'www.lookmantastic.com', 'www.myvitamins.com', 'www.lookfantastic.net', 'www.myprotein.com/ie/pages/home', 'www.myprotein.com/it/pages/home', 'www.myprotein.com/es/pages/home', 'www.myprotein.com/fr/pages/home']
activeWebsites = {"UA-59323-77": "AllSole", "UA-59323-83":"HQHair","UA-59323-75":"Iwoot","UA-59323-61":"MyBag", "UA-59323-24":"Sendit","UA-59323-4":"TheHut","UA-59323-37":"Zavvi","UA-59323-58":"Zaavi.es","UA-59323-76":"Zavvi.nl","UA-9345964-1":"LookFantastic","UA-18807547-1":"Lookfantastic.net","UA-10211190-1":"lookmantastic","UA-19257214-1":"http://www.myprotein.com/de/pages/home","UA-19256573-1":"http://www.myprotein.com/es/pages/home","UA-19256640-1":"http://www.myprotein.com/fr/pages/home","UA-19256474-1":"http://www.myprotein.com/ie/pages/home","UA-19256561-1":"http://www.myprotein.com/it/pages/home","UA-479953-1":"http://www.myprotein.com/uk","UA-2620226-2":"http://www.beautyexpert.co.uk","UA-2620226-1":"http://www.mankind.co.uk","UA-18594156-35": "http://www.myvitamins.com"}
dimensionString = collectArguments.collectArguments(dimensions_and_metrics.dimensions)
metricString = collectArguments.collectArguments(dimensions_and_metrics.metrics)
dimensionList = dimensionString.split(',')
metricList = metricString.split(',')
#myNewFile.write('Profile\tDesktop Transactions\tDesktop Visits\tDesktop Revenue\tDesktop Conversion Rate\tMobile Transactions\tMobile Visits\tMobile Revenue\tMobile Conversion Rate\tMobile Percentage of Revenue\n')


def main(argv):

  # Step 1. Get an analytics service object.
  service = hello_analytics_api_v3_auth.initialize_service()
  
  accounts = service.management().accounts().list().execute()
  #accounts is a dictionary that includes some administrative
  #info such as username and email (in this case thehutinsight), but also includes a mapping
  #of 'items' to a list of dictionaries. The list has an entry for
  #each website in the users analytics. That entry is a dictionary mapping
  #a set of variables including 'name' to e.g. 'www.thehut.com' and 'id' to e.g. 59323
  counter = 0
  segmentName = raw_input('Please Enter your preferred Segment Name (Hit Enter for All Visits)\n')
  try:
    segment_id = 'gaid::'+segmentIds.segments_Dictionary[segmentName]
  except:
    print "Oh dear, That Segment doesn't exist. Please try again or hit enter for no segments"
    segment_id = 'gaid::'+segmentIds.segments_Dictionary[segmentName]
 
  for accountProfiles in range (13):
    for x in range (countWebProperties(service,accounts,accountProfiles)):
      time.sleep(0.3)
      try:
        # Step 2. Get the user's first profile ID.
        helperList = get_first_profile_id(service,accounts,accountProfiles,x)
        profile_id = helperList[0]

        if profile_id:
          try:
            activeWebsites[helperList[1]]
          # Step 3. Query the Core Reporting API.
            results = get_results(service, profile_id, segment_id)
          except(KeyError):
            results = None

          # Step 4. Output the results.
          print_results(results,counter)
          if results:
            counter += 1
         #print "I printed the results"
              
      except TypeError, error:
        # Handle errors in constructing a query.
        print ('There was an error in constructing your query : %s' % error)

      except HttpError, error:
        # Handle API errors.
        print ('Arg, there was an API error : %s : %s' %
               (error.resp.status, error._get_reason()))

      except AccessTokenRefreshError:
        # Handle Auth errors.
        print ('The credentials have been revoked or expired, please re-run '
               'the application to re-authorize')

def get_first_profile_id(service,accounts,accountProfiles,x):
  # Get a list of all Google Analytics accounts for this user
  ##print service.management().accounts().list()

  if accounts.get('items'):
    # Get the first Google Analytics account
    firstAccountId = accounts.get('items')[accountProfiles].get('id')
##    print "firstAccountID \t%s" %str(firstAccountId)

    # Get a list of all the Web Properties for the first account
    webproperties = service.management().webproperties().list(accountId=firstAccountId).execute()
    try:
      if webproperties.get('items'):
        # Get the first Web Property ID
        firstWebpropertyId = webproperties.get('items')[x].get('id')

        # Get a list of all Profiles for the first Web Property of the first Account
        profiles = service.management().profiles().list(
            accountId=firstAccountId,
            webPropertyId=firstWebpropertyId).execute()

        if profiles.get('items'):
          # return the first Profile ID
          return [profiles.get('items')[0].get('id'),firstWebpropertyId]
    except:
      if webproperties.get('items'):
  # Get the first Web Property ID
        firstWebpropertyId = webproperties.get('items')[0].get('id')

  # Get a list of all Profiles for the first Web Property of the first Account
        profiles = service.management().profiles().list(
            accountId=firstAccountId,
            webPropertyId=firstWebpropertyId).execute()

        if profiles.get('items'):
          # return the first Profile ID
          return [profiles.get('items')[0].get('id'),firstWebpropertyId]
  return [None,None]


def get_results(service, profile_id, segment_id):
  # Use the Analytics Service Object to query the Core Reporting API
  return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=date1,
      end_date=date2,
      segment=segment_id,
      ##Useful segment ids: 729961158 (ipad)
      dimensions=dimensionString,
      metrics=metricString).execute()

def print_results(results,counter):
  # Writes results to a file called mynewfile in the documents folder.
  #Print Headers
  if results:
    print counter
    if counter == 0:
      for lists1 in results.get('rows'):
        for z in range (0,len(dimensionList)-1):
          for metric in range (0,len(metricList)):
            myNewFile.write('\t'+dimensionList[z]+'='+str(lists1[z])+','+dimensionList[z+1]+'='+lists1[z+1]+str(metricList[metric]))
      myNewFile.write('\n')
    counter += 1
  #Print results
  try:
    binCode = checkList.index(results.get('profileInfo').get('profileName'))
  except:
    binCode = 0
  if binCode > 0:
    if results:
      myNewFile.write ('%s' % results.get('profileInfo').get('profileName'))
      for lists in results.get('rows'):
        #print lists
        for k in range (len(metricList),len(lists)):
          try:
           myNewFile.write ('\t%s' %lists[k])
          except:
           myNewFile.write ('\t0')
      myNewFile.write('\n')

    globalOutputList.append((results.get('profileInfo').get('profileName'),results.get('rows')))
##  else:
##    print 'No results found'

def countWebProperties(service,accounts,accountProfiles):
  firstAccountId = accounts.get('items')[accountProfiles].get('id')
  webproperties = service.management().webproperties().list(accountId=firstAccountId).execute()
  length = len(webproperties.get('items'))
  ##print len(webproperties.get('items'))
  return length


##if __name__ == '__main__':

main(sys.argv)
print globalOutputList
myNewFile.close()
