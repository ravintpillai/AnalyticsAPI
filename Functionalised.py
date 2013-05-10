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
#date1 = raw_input('Enter Start Date as YYYY-MM-DD ')
#date2 = raw_input('Enter End Date as YYYY-MM-DD ')
checkList = ['Profile', 'H - SendIt', 'A - Zavvi', 'A - TheHut.com', 'H - zavvi.es', 'H - mybag.com', 'J - iwantoneofthose.com', 'H - zavvi.nl', 'H - allsole.com', 'www.hqhair.com/', 'ttp://www.myprotein.com/uk/', 'www.mankind.co.uk', 'www.beautyexpert.co.uk', 'www.lookfantastic.com', 'www.lookmantastic.com', 'www.myvitamins.com', 'www.lookfantastic.net', 'www.myprotein.com/ie/pages/home', 'www.myprotein.com/it/pages/home', 'www.myprotein.com/es/pages/home', 'www.myprotein.com/fr/pages/home']
activeWebsites = {"UA-59323-77": "AllSole", "UA-59323-83":"HQHair","UA-59323-75":"Iwoot","UA-59323-61":"MyBag", "UA-59323-24":"Sendit","UA-59323-4":"TheHut","UA-59323-37":"Zavvi","UA-59323-58":"Zaavi.es","UA-59323-76":"Zavvi.nl","UA-9345964-1":"LookFantastic","UA-18807547-1":"Lookfantastic.net","UA-10211190-1":"lookmantastic","UA-19257214-1":"http://www.myprotein.com/de/pages/home","UA-19256573-1":"http://www.myprotein.com/es/pages/home","UA-19256640-1":"http://www.myprotein.com/fr/pages/home","UA-19256474-1":"http://www.myprotein.com/ie/pages/home","UA-19256561-1":"http://www.myprotein.com/it/pages/home","UA-479953-1":"http://www.myprotein.com/uk","UA-2620226-2":"http://www.beautyexpert.co.uk","UA-2620226-1":"http://www.mankind.co.uk","UA-18594156-35": "http://www.myvitamins.com"}

def getArguments():
  dateList = collectArguments.getDates()
  date1 = dateList[0]
  date2 = dateList[1]
  filename = collectArguments.getFilename()
#filename = 'C:\\Users\\thambapillair\\Documents\\'+ raw_input('Enter preferred filename')+'.txt'
  dimensionString = collectArguments.collectArguments(dimensions_and_metrics.dimensions)
  metricString = collectArguments.collectArguments(dimensions_and_metrics.metrics)
  #print metricString
  dimensionList = collectArguments.collectLists(dimensionString)
#metricList = metricString.split(',')
  metricList = collectArguments.collectLists(metricString)
  #print dimensionList,metricList
  segment_id = collectArguments.getSegments()
  #for z in range (0,len(dimensionList)-1):
    #print metricList[z]
    #print z
  returnList = [date1,date2,dimensionString,metricString,dimensionList,metricList,filename,segment_id]
  return returnList
#myNewFile.write('Profile\tDesktop Transactions\tDesktop Visits\tDesktop Revenue\tDesktop Conversion Rate\tMobile Transactions\tMobile Visits\tMobile Revenue\tMobile Conversion Rate\tMobile Percentage of Revenue\n')


def mainHelper(argv,date1, date2, dimensionString, metricString, dimensionList, metricList,myNewFile,segment_id):
  # Step 1. Get an analytics service object.
  service = hello_analytics_api_v3_auth.initialize_service()
  accounts = service.management().accounts().list().execute()
  #accounts is a dictionary that includes some administrative
  #info such as username and email (in this case thehutinsight), but also includes a mapping
  #of 'items' to a list of dictionaries. The list has an entry for
  #each website in the users analytics. That entry is a dictionary mapping
  #a set of variables including 'name' to e.g. 'www.thehut.com' and 'id' to e.g. 59323
  counter = 0
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
            results = get_results(service, profile_id, segment_id, date1, date2, dimensionString, metricString)
          except(KeyError):
            results = None

          # Step 4. Output the results.
          print_results(results,counter,dimensionList, metricList,myNewFile)
          if results:
            counter += 1
         #print "I printed the results"
              
      except (TypeError):
        # Handle errors in constructing a query.
        print ('There was an error in constructing your query : %s' % error)

      except (HttpError):
        # Handle API errors.
        print ('Arg, there was an API error : %s : %s' %
               (error.resp.status, error._get_reason()))

      except (AccessTokenRefreshError):
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


def get_results(service, profile_id, segment_id, date1, date2, dimensionString, metricString):
  # Use the Analytics Service Object to query the Core Reporting API
  print (segment_id,type(segment_id))
  return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=date1,
      end_date=date2,
      segment=segment_id,
      ##Useful segment ids: 729961158 (ipad)
      dimensions=dimensionString,
      metrics=metricString).execute()

def print_results(results,counter,dimensionList,metricList,myNewFile):
  # Writes results to a file called mynewfile in the documents folder.
  #Print Headers
  if results:
    #print counter
    if counter == 0:
      for lists1 in results.get('rows'):
        for z in range (0,max(len(dimensionList)-1,1)):
          for metric in range (0,len(metricList)):
            try:
              myNewFile.write('\t'+dimensionList[z]+'='+str(lists1[z])+','+dimensionList[z+1]+'='+lists1[z+1]+str(metricList[metric]))
              #print dimensionList,'dimensionList',lists1,'lists1',metricList,'metricList'
            except IndexError:
              myNewFile.write('\t'+str(metricList[metric]))
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
        for k in range (len(dimensionList),len(lists)):
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

def printResults2(globalOutputList,dimensionList):
  for x in range (0,len(globalOutputList)):
    print (dimensionList, globalOutputList[x][1])
    print (len(globalOutputList[x][1][1]))
    for y in range (len(dimensionList),len(globalOutputList[x][1][1])):
      for z in globalOutputList[x][1]:
                    print (z[y])
  

##if __name__ == '__main__':
def main():
  arguments = getArguments()
  #print arguments
  myNewFile = open (arguments[6] , 'w+')
  mainHelper(sys.argv,arguments[0],arguments[1],arguments[2],arguments[3],arguments[4],arguments[5],myNewFile,arguments[7])
  #printResults2(globalOutputList,arguments[4])
  #print globalOutputList
  myNewFile.close()

main()
