using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Configuration;
using Google.Analytics;
using Google.GData.Analytics;
using Google.GData.Client;
using Google.GData.Extensions;

namespace ImportGAData
{
    public class GAService_Impl : GAService
    {
        private static readonly log4net.ILog log = log4net.LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);
        private static String userId = ConfigurationManager.AppSettings["userId"].ToString();
        private static String password = ConfigurationManager.AppSettings["pwd"].ToString();
        private static String applicationName = ConfigurationManager.AppSettings["applicationName"].ToString();
        private static String analyticsApiURL = ConfigurationManager.AppSettings["analyticsAPIUrl"].ToString();
        private static int requestPause = Convert.ToInt32(ConfigurationManager.AppSettings["requestPause"].ToString());

        private static int numberOfGARecordsToRetrievePerRequest = 10000;

        public List<PaidSearchVisitSummary> getPaidSearchVisits(DateTime fromDate, DateTime toDate, Site site)
        {
            List<PaidSearchVisitSummary> visits = new List<PaidSearchVisitSummary>();

            int startIndex = 1;
            Boolean isMore;

            DataFeed feed = null;
            do
            {
                isMore = false;

                try
                {

                    feed = getGADataFeed(site, fromDate, toDate,
                                        "ga:medium,ga:date,ga:pagePath,ga:source",
                                        "ga:visits",
                                        "ga:medium==ppc,ga:medium==cpc,ga:medium==PPC,ga:medium==CPC", "", startIndex);

                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            PaidSearchVisitSummary visit = new PaidSearchVisitSummary(singleEntry, site);
                            visits.Add(visit);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getPaidSearchVisits", rEx);
                }


                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return visits;
        }

        public List<SiteEvent> getEventData(DateTime fromDate, DateTime toDate, Site site)
        {
            List<SiteEvent> events = new List<SiteEvent>();

            int startIndex = 1;
            Boolean isMore;

            DataFeed feed = null;
            do
            {
                isMore = false;

                try
                {

                    feed = getGADataFeed(site, fromDate, toDate,
                                        "ga:eventCategory,ga:eventAction,ga:eventLabel,ga:date",
                                        "ga:totalEvents,ga:uniqueEvents",
                                        "ga:eventCategory==Availability,ga:eventCategory==Search,ga:eventAction==Click", "", startIndex);

                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            SiteEvent siteEvent = new SiteEvent(singleEntry, site);
                            events.Add(siteEvent);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getEventData", rEx);
                }

                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return events;
        }

        public List<DetailedVisit> getVisitSourceData(DateTime fromDate, DateTime toDate, Site site)
        {
            List<DetailedVisit> visits = new List<DetailedVisit>();

            int startIndex = 1;
            Boolean isMore;

            DataFeed feed = null;
            do
            {
                isMore = false;

                try
                {

                    feed = getGADataFeed(site, fromDate, toDate,
                                        "ga:medium,ga:date",
                                        "ga:visitors,ga:visits,ga:transactions",
                                        "", "", startIndex);

                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            DetailedVisit visit = new DetailedVisit(singleEntry, site);
                            visits.Add(visit);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getVisitData", rEx);
                }


                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return visits;
        }

        public List<Visit> getVisitData(DateTime fromDate, DateTime toDate, Site site)
        {
            List<Visit> visits = new List<Visit>();

            int startIndex = 1;
            Boolean isMore;

            DataFeed feed = null;
            do
            {
                isMore = false;

                try
                {

                    feed = getGADataFeed(site, fromDate, toDate,
                                        "ga:date",
                                        "ga:visitors,ga:visits",
                                        "", "", startIndex);

                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            Visit visit = new Visit(singleEntry, site);
                            visits.Add(visit);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getVisitData", rEx);
                }


                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return visits;
        }

        public List<Visitor> getVisitorData(DateTime fromDate, DateTime toDate, Site site)
        {
            List<Visitor> visitors = new List<Visitor>();

            int startIndex = 1;
            Boolean isMore;

            DataFeed feed = null;
            do
            {
                isMore = false;

                try
                {

                    feed = getGADataFeed(site, fromDate, toDate,
                                        "ga:daysSinceLastVisit,ga:pageDepth,ga:visitCount,ga:visitorType,ga:landingPagePath,ga:transactionId",
                                        "ga:transactions",
                                        "", "", startIndex);

                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            Visitor visitor = new Visitor(singleEntry);
                            visitors.Add(visitor);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getVisitorData", rEx);
                }

                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return visitors;
        }

        public List<Search> getSiteSearchData(DateTime fromDate, DateTime toDate, Site site)
        {

            List<Search> searchData = new List<Search>();

            int startIndex = 1;
            Boolean isMore;

            DataFeed feed = null;
            do
            {
                isMore = false;

                try
                {
 
                    feed = getGADataFeed(site, fromDate, toDate,
                                        "ga:visitLength,ga:transactionId,ga:searchUsed",
                                        "ga:transactions",
                                        "", "", startIndex);

                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            Search search = new Search(singleEntry);
                            searchData.Add(search);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getSiteSearchData", rEx);
                }

                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return searchData;
        }

        public List<GeoSystem> getGeoSystemData(DateTime fromDate, DateTime toDate, Site site)
        {
            List<GeoSystem> geoSystems = new List<GeoSystem>();

            int startIndex = 1;
            Boolean isMore;

            DataFeed feed = null;
            do
            {
                isMore = false;
                try
                {

                    feed = getGADataFeed(site, fromDate, toDate,
                                        "ga:city,ga:country,ga:isMobile,ga:language,ga:transactionId",
                                        "ga:transactions",
                                        "", "", startIndex);

                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            GeoSystem geoSystem = new GeoSystem(singleEntry);
                            geoSystems.Add(geoSystem);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getGeoSystemData", rEx);
                }

                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return geoSystems;
        }

        public List<SourceTime> getSourceTimeData(DateTime fromDate, DateTime toDate, Site site)
        {
            List<SourceTime> sourceTimes = new List<SourceTime>();

            int startIndex = 1;
            Boolean isMore;

            DataFeed feed = null;
            do
            {
                isMore = false;

                try
                {
                    feed = getGADataFeed(site, fromDate, toDate,
                                        "ga:campaign,ga:keyword,ga:medium,ga:source,ga:daysToTransaction,ga:transactionId,ga:visitsToTransaction",
                                        "ga:transactions",
                                        "", "", startIndex);
                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            SourceTime sourceTime = new SourceTime(singleEntry, site);
                            sourceTimes.Add(sourceTime);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getSourceTimeData", rEx);
                }

                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return sourceTimes;
        }

        public List<AdwordsCost> getAdwordsData(DateTime fromDate, DateTime toDate, Site site)
        {
            List<AdwordsCost> adwordsCosts = new List<AdwordsCost>();

            int startIndex = 1;
            Boolean isMore;
            
            DataFeed feed = null;
            do
            {
                isMore = false;                                
               
                try
                {
                    feed = getGADataFeed(site, fromDate, toDate, 
                                        "ga:source,ga:medium,ga:keyword,ga:adwordsCampaignId,ga:date",
                                        "ga:adClicks,ga:adCost,ga:transactions,ga:transactionRevenue",
                                        "ga:medium==ppc,ga:medium==cpc,ga:medium==PPC,ga:medium==CPC", "", startIndex);

                    if (feed != null)
                    {
                        foreach (DataEntry singleEntry in feed.Entries)
                        {
                            AdwordsCost adwordsCost = new AdwordsCost(singleEntry, site);
                            adwordsCosts.Add(adwordsCost);
                            isMore = true;
                        }
                    }
                }
                catch (Exception rEx)
                {
                    log.Error("Error in getAdwordsData", rEx);
                }

                if (isMore) startIndex += numberOfGARecordsToRetrievePerRequest;
            } while (isMore);

            return adwordsCosts;
        }

        private DataFeed getGADataFeed(Site site,
            DateTime fromDay,
            DateTime toDay,
            string dimensions,
            string metrics,
            string filters,
            string sort,
            int startIndex)
        {
            AnalyticsService asv = new AnalyticsService(applicationName);
            asv.setUserCredentials(userId, password);

            DataQuery query = new DataQuery(analyticsApiURL);
            query.Ids = site.account;
            query.Dimensions = dimensions;
            query.Metrics = metrics;
            query.Filters = filters;
            query.Sort = sort;
            query.NumberToRetrieve = numberOfGARecordsToRetrievePerRequest;
            query.StartIndex = startIndex;
            query.GAStartDate = String.Format("{0:yyyy-MM-dd}", fromDay);
            query.GAEndDate = String.Format("{0:yyyy-MM-dd}", toDay);

            log.Debug("Querying Google API : " + query.Uri.ToString());

            DataFeed feed = asv.Query(query);

            System.Threading.Thread.Sleep(requestPause); // wait between requests

            return feed;
        }
    }
}
