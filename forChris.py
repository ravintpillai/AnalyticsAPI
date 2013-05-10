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
filename = 'G:\\Krustopher\\'+ raw_input('Enter preferred filename')+'.txt'
myNewFile = open (filename , 'w+')
myNewFile.write('Profile\tDesktop Transactions\tDesktop Visits\tDesktop Revenue\tDesktop Conversion Rate\tMobile Transactions\tMobile Visits\tMobile Revenue\tMobile Conversion Rate\tMobile Percentage of Revenue\n')
checkList = ['Profile', 'H - SendIt', 'A - Zavvi', 'A - TheHut.com', 'H - zavvi.es', 'H - mybag.com', 'J - iwantoneofthose.com', 'H - zavvi.nl', 'H - allsole.com', 'www.hqhair.com/', 'ttp://www.myprotein.com/uk/', 'www.mankind.co.uk', 'www.beautyexpert.co.uk', 'www.lookfantastic.com', 'www.lookmantastic.com', 'www.myvitamins.com', 'www.lookfantastic.net', 'www.myprotein.com/ie/pages/home', 'www.myprotein.com/it/pages/home', 'www.myprotein.com/es/pages/home', 'www.myprotein.com/fr/pages/home']
activeWebsites = {"UA-59323-77": "AllSole", "UA-59323-83":"HQHair","UA-59323-75":"Iwoot","UA-59323-61":"MyBag", "UA-59323-24":"Sendit","UA-59323-4":"TheHut","UA-59323-37":"Zavvi","UA-59323-58":"Zaavi.es","UA-59323-76":"Zavvi.nl","UA-9345964-1":"LookFantastic","UA-18807547-1":"Lookfantastic.net","UA-10211190-1":"lookmantastic","UA-19257214-1":"http://www.myprotein.com/de/pages/home","UA-19256573-1":"http://www.myprotein.com/es/pages/home","UA-19256640-1":"http://www.myprotein.com/fr/pages/home","UA-19256474-1":"http://www.myprotein.com/ie/pages/home","UA-19256561-1":"http://www.myprotein.com/it/pages/home","UA-479953-1":"http://www.myprotein.com/uk","UA-2620226-2":"http://www.beautyexpert.co.uk","UA-2620226-1":"http://www.mankind.co.uk","UA-18594156-35": "http://www.myvitamins.com"}
print activeWebsites
idChecker = ""

def main(argv):

  # Step 1. Get an analytics service object.
  service = hello_analytics_api_v3_auth.initialize_service()
  #I believe this is a token to get access
  accounts = service.management().accounts().list().execute()
  #accounts is a dictionary that includes some administrative
  #info such as username and email (in this case thehutinsight), but also includes a mapping
  #of 'items' to a list of dictionaries. The list has an entry for
  #each website in the users analytics. That entry is a dictionary mapping
  #a set of variables including 'name' to e.g. 'www.thehut.com' and 'id' to e.g. 59323
  segment_id = 'gaid::'+raw_input('Please enter your preferred segment id. If you want no segments, enter -1 ')
  ##segments = service.management().segments().list().execute()
  for accountProfiles in range (13):
    #The step above asks the script to repeat the call for as many times as there are 'account profiles'.
    for x in range (countWebProperties(service,accounts,accountProfiles)):
      #The step above asks the script to repeat the call for as many times as there are unique Websites in the Account Profile
      time.sleep(0.1)
      #Sleeps to get round the user limit rate exceeded exception

      try:
        # Step 2. Get the user's profile ID.
        profile_id = get_first_profile_id(service,accounts,accountProfiles,x)
        #print "profileID \t%s" %str(profile_id)

        if profile_id:
          ##Need to write something here which checks the profile id
          ##is available in a list of legitimate profile ids.
          ##For now, before the user selects anything,
          ##set the legitimate profile id's to be the id's associated
          ##with the websites in the Checklist
           # Step 3. Query the Core Reporting API.
           results = get_results(service, profile_id, segment_id)
          # Step 4. Output the results.
           print_results(results)

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
  #For example, for the Profile where the hut, iwoot, allsole etc are stored this is 59323.
  #The profile is called 'www.thehut.com' but doesn't just include thehut!

  # Get a list of all the Web Properties for the first account
  webproperties = service.management().webproperties().list(accountId=firstAccountId).execute()
  # Web properties is a dictionary a lot like accounts but for a given accountID. E.g. 59323 gives
  #each of the sites available under www.thehut.com in analytics.)
    if webproperties.get('items'):
    #webproperties.get('items') gives a list of dictionaries
    #where each dicitionary in the list corresponds to
    #a website.
      # Get the first Web Property ID
      firstWebpropertyId = webproperties.get('items')[x].get('id')
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
      #print "Useful segment ids: 729961158 (ipad)"
      dimensions='ga:isMobile',
      metrics='ga:transactions,ga:visits,ga:transactionRevenue').execute()

def print_results(results):
  # Writes results to a file called mynewfile in the documents folder.
  try:
    binCode = checkList.index(results.get('profileInfo').get('profileName'))
  except:
    binCode = 0
  if binCode > 0:
    if results:
      myNewFile.write ('%s' % results.get('profileInfo').get('profileName'))
      try:
        myNewFile.write ('\t%s' % results.get('rows')[0][1])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t%s' % results.get('rows')[0][2])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t%s' % results.get('rows')[0][3])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t'+str(100*(float(results.get('rows')[0][1])/float(results.get('rows')[0][2])))+'%')
      except:
        myNewFile.write('\t0')
      try:
        myNewFile.write ('\t%s' % results.get('rows')[1][1])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t%s' % results.get('rows')[1][2])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t%s' % results.get('rows')[1][3])
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write('\t'+str((100*float(results.get('rows')[1][1])/float(results.get('rows')[1][2])))+'%')
      except:
        myNewFile.write ('\t0')
      try:
        myNewFile.write ('\t'+str((100*float(results.get('rows')[1][3])/(float(results.get('rows')[0][3])+float(results.get('rows')[1][3]))))+'%'+'\n')
      except:
        myNewFile.write ('\t0\n')

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
