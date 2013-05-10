#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import sys
import io
import datetime
# import the Auth Helper class
import hello_analytics_api_v3_auth
from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError
globalOutputList = []
now = datetime.datetime.now()
day = now.day
if str(day).__len__() == 1:
  date1 = (now.strftime('20%y-%m-0')+str(day))
else:
  date1 = (now.strftime('20%y-%m-')+str(day))
date2 = date1
##filename = 'C:\\Users\\thambapillair\\Documents\\HutRelaunch'+ date1 +'.txt'
###filename = 'C:\\Users\\thambapillair\\Documents\\'+ raw_input('Enter preferred filename')+'.txt'
##myNewFile = open (filename , 'w+')
##myNewFile.write('Profile\tVisits\tTransactions\tRevenue\n')
checkList = ['Profile', 'A - TheHut.com']

def main(argv):
  # Step 1. Get an analytics service object.
  service = hello_analytics_api_v3_auth.initialize_service()
  accounts = service.management().accounts().list().execute()
  segment_id = 'gaid::304041085'
##  segments = service.management().segments().list().execute()
##  print segments
  for accountProfiles in range (1):
    for x in range (32,33): ##for x in range (countWebProperties(service,accounts,accountProfiles)):
      time.sleep(0.3)
      try:
        # Step 2. Get the user's first profile ID.
        profile_id = get_first_profile_id(service,accounts,accountProfiles,x)
##        print "profileID \t%s" %str(profile_id)

        if profile_id:
          # Step 3. Query the Core Reporting API.
          results = get_results(service, profile_id, segment_id)
          #print "I got the results"

          # Step 4. Output the results.
          print_results(results)
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
          return profiles.get('items')[0].get('id')
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
              return profiles.get('items')[0].get('id')
  return None


def get_results(service, profile_id, segment_id):
  # Use the Analytics Service Object to query the Core Reporting API
  return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=date1,
      end_date=date2,
      segment=segment_id,
      ##Useful segment ids: 729961158 (ipad)
      dimensions='ga:hour',
      metrics='ga:visits,ga:transactions').execute()

def print_results(results):
  # Writes results to a file called mynewfile in the documents folder.
  #print results
  try:
    binCode = checkList.index(results.get('profileInfo').get('profileName'))
  except:
    binCode = 0
  if binCode > 0:
    if results:
##      myNewFile.write ('%s' % results.get('profileInfo').get('profileName')[4:])
##      print results.get('rows')
##      for x in results.get('rows'):
##        for y in x:
##          try:
##            myNewFile.write(y+'\t')
##          except:
##            myNewFile.write ('\t0')

      globalOutputList.append((results.get('profileInfo').get('profileName'),results.get('rows')))

def countWebProperties(service,accounts,accountProfiles):
  firstAccountId = accounts.get('items')[accountProfiles].get('id')
  webproperties = service.management().webproperties().list(accountId=firstAccountId).execute()
  length = len(webproperties.get('items'))
  ##print len(webproperties.get('items'))
  return length


##if __name__ == '__main__':

main(sys.argv)
##print globalOutputList
##myNewFile.close()
