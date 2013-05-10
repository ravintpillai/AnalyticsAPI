#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import sys
import io
# import the Auth Helper class
import hello_analytics_api_v3_auth

from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError
globalOutputList = []
date1 = raw_input('Enter Start Date as YYYY-MM-DD ')
date2 = raw_input('Enter End Date as YYYY-MM-DD ')
filename = 'C:\\Users\\cookes\\Documents\\'+ raw_input('Enter preferred filename ')+'.txt'
myNewFile = open (filename , 'w+')
myNewFile.write('Profile\tTransactions\tVisits\tRevenue\tConversion Rate\n')
checkList = ['Profile', 'ttp://www.myprotein.com/uk/',  'www.myprotein.com/ie/pages/home', 'www.myprotein.com/it/pages/home', 'www.myprotein.com/es/pages/home', 'www.myprotein.com/fr/pages/home', 'www.myprotein.com/de/pages/home','H - SendIt', 'A - Zavvi', 'A - TheHut.com', 'H - zavvi.es', 'H - mybag.com', 'J - iwantoneofthose.com', 'H - zavvi.nl', 'H - allsole.com', 'www.hqhair.com/', 'www.mankind.co.uk', 'www.beautyexpert.co.uk', 'www.lookfantastic.com', 'www.lookmantastic.com', 'www.myvitamins.com', 'www.lookfantastic.net']

def main(argv):

  ## print x
  ##print "Hey-ho merry-o ring a ding a dillo what the chuff"
  # Step 1. Get an analytics service object.
  service = hello_analytics_api_v3_auth.initialize_service()
  accounts = service.management().accounts().list().execute()
  segment_id = 'gaid::'+raw_input('Please enter your preferred segment id. If you want no segments, enter -1 ')
  if segment_id == 'gaid::peerius' :
    segment_id = 'gaid::906552862'
  
##  segments = service.management().segments().list().execute()
##  print segments
  for accountProfiles in range (13):
    for x in range (countWebProperties(service,accounts,accountProfiles)):
      time.sleep(0.1)
      try:
        # Step 2. Get the user's first profile ID.
        profile_id = get_first_profile_id(service,accounts,accountProfiles,x)
##        print "profileID \t%s" %str(profile_id)

        if profile_id:
          # Step 3. Query the Core Reporting API.
          results = get_results(service, profile_id, segment_id)
          #print results
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
  ##print "I am trying to get first profile ID"

  ##print service.management().accounts().list()
  ##if accountProfiles == 0:
   ## print accounts.get('items')[accountProfiles]
   ## print accounts.get('items')[accountProfiles+1]
  ##print accounts.get('items')[1]
  ##print accounts.get('items')[1].get('id')

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
      ##Useful segment ids: 729961158 (ipad), 906552862 (people clicking peerius)
      ##dimensions='ga:isMobile',
      metrics='ga:transactions,ga:visits,ga:transactionRevenue').execute()

def print_results(results):
  # Writes results to a file called mynewfile in the documents folder.
  #print results
  try:
    binCode = checkList.index(results.get('profileInfo').get('profileName'))
  except:
    binCode = 0
  if binCode > 0:
    if results:
      myNewFile.write ('%s' % results.get('profileInfo').get('profileName'))
      try:
        myNewFile.write ('\t%s' % results.get('rows')[0][0])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t%s' % results.get('rows')[0][1])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t%s' % results.get('rows')[0][2])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t'+str(100*(float(results.get('rows')[0][0])/float(results.get('rows')[0][1])))+'%\n')
      except:
        myNewFile.write ('\t0\n')
##      try:
##        myNewFile.write ('\t%s' % results.get('rows')[1][1])
##      except:
##        myNewFile.write ('\t0')
##      try:
##        myNewFile.write ('\t%s' % results.get('rows')[1][2])
##      except:
##        myNewFile.write ('\t0')
##      try:
##        myNewFile.write ('\t%s' % results.get('rows')[1][3])
##      except:
##        myNewFile.write ('\t0')
##      try:
##        myNewFile.write('\t'+str((100*float(results.get('rows')[1][1])/float(results.get('rows')[1][2])))+'%')
##      except:
##        myNewFile.write ('\t0')
##      try:
##        myNewFile.write ('\t'+str((100*float(results.get('rows')[1][3])/(float(results.get('rows')[0][3])+float(results.get('rows')[1][3]))))+'%'+'\n')
##      except:
##        myNewFile.write ('\t0\n')

    globalOutputList.append((results.get('profileInfo').get('profileName'),results.get('rows')))
##  else:
##    print 'No results found'

def countWebProperties(service,accounts,accountProfiles):
  firstAccountId = accounts.get('items')[accountProfiles].get('id')
  webproperties = service.management().webproperties().list(accountId=firstAccountId).execute()
  length = len(webproperties.get('items'))
  ##print (webproperties.get('items'))
  return length


##if __name__ == '__main__':

main(sys.argv)
print globalOutputList
myNewFile.close()
