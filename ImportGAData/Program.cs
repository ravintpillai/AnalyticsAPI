using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Configuration;
using log4net;
using log4net.Config;
using System.IO;
using System.Threading;
using System.Threading.Tasks;

namespace ImportGAData
{
    class Program
    {
        protected static readonly ILog log = LogManager.GetLogger(typeof(Program));
        private static int goBackDays = Convert.ToInt32(ConfigurationManager.AppSettings["goBackDays"].ToString());

        static int Main(string[] args)
        {
            string logFilePath = AppDomain.CurrentDomain.BaseDirectory + "log4net.config";
            FileInfo finfo = new FileInfo(logFilePath);
            log4net.Config.XmlConfigurator.ConfigureAndWatch(finfo); 
            
            DateTime fromDate = DateTime.Today;
            DateTime toDate = DateTime.Today;

            if (args.Length == 2) {
                fromDate = DateTime.ParseExact(args[0].ToString(), "yyyy-MM-dd", null);
                toDate = DateTime.ParseExact(args[1].ToString(), "yyyy-MM-dd", null);
            } else {
                fromDate = fromDate.AddDays(-goBackDays);
            }

            log.Debug("Start ImportGAData for dates " + fromDate.ToLongDateString() + " to " + toDate.ToLongDateString());
    
            try
            {                
                foreach (Site site in getSites())
                {
                    System.Console.WriteLine("Getting data for site : " + site.siteId + ", GA account : " + site.account);
       
                    // Only permitted 4 concurrent requests
                                        
                    Parallel.Invoke(() => { GetVisitSourceData(fromDate, toDate, site); },
                                    () => { GetVisitData(fromDate, toDate, site); },
                                    () => { GetVisitorData(fromDate, toDate, site); },
                                    () => { GetSearchData(fromDate, toDate, site); }
                                    );

                    Parallel.Invoke(() => { GetGeoSystemData(fromDate, toDate, site); },
                                    () => { GetSourceTimeData(fromDate, toDate, site); },
                                    () => { GetAdwordsCostData(fromDate, toDate, site); },
                                    () => { GetEventData(fromDate, toDate, site); }
                                    );
                    
                    Parallel.Invoke(() => { GetPaidSearchVisitData(fromDate, toDate, site); });
                     
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Error : " + e.ToString());
                log.Error("Exception in ImportGAData (quitting)", e);
                return 1;
            }

            log.Debug("End ImportGAData for dates " + fromDate.ToLongDateString() + " to " + toDate.ToLongDateString());

            return 0;
        }

        private static void GetPaidSearchVisitData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetPaidSearchVisitData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<PaidSearchVisitSummary> visits = gaService.getPaidSearchVisits(fromDate, toDate, site);

            foreach (PaidSearchVisitSummary visit in visits)
            {
                AnalyticsRepository.recordPaidSearchVisitSummary(visit);
            }
        }

        private static void GetEventData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetEventData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<SiteEvent> events = gaService.getEventData(fromDate, toDate, site);

            foreach (SiteEvent siteEvent in events)
            {
                AnalyticsRepository.recordAnalyticsEvent(siteEvent);
            }
        }

        private static void GetVisitSourceData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetVisitSourceData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<DetailedVisit> visits = gaService.getVisitSourceData(fromDate, toDate, site);

            foreach (DetailedVisit visit in visits)
            {
                AnalyticsRepository.recordAnalyticsVisitSource(visit);
            }
        }

        private static void GetVisitData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetVisitData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<Visit> visits = gaService.getVisitData(fromDate, toDate, site);

            foreach (Visit visit in visits)
            {
                AnalyticsRepository.recordAnalyticsVisit(visit);
            }
        }

        private static void GetVisitorData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetVisitorData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<Visitor> visitors = gaService.getVisitorData(fromDate, toDate, site);

            foreach (Visitor visitor in visitors)
            {
                AnalyticsRepository.recordAnalyticsVisitor(visitor);
            }
        }

        private static void GetSearchData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetSearchData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<Search> searchData = gaService.getSiteSearchData(fromDate, toDate, site);

            foreach (Search search in searchData)
            {
                AnalyticsRepository.recordAnalyticsSiteSearch(search);
            }
        }

        private static void GetGeoSystemData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetGeoSystemData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<GeoSystem> geoSystems = gaService.getGeoSystemData(fromDate, toDate, site);

            foreach (GeoSystem geoSystem in geoSystems)
            {
                AnalyticsRepository.recordAnalyticsGeoSystem(geoSystem);
            }
        }

        private static void GetSourceTimeData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetSourceTimeData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<SourceTime> gaSourceTimes = gaService.getSourceTimeData(fromDate, toDate, site);

            foreach (SourceTime sourceTime in gaSourceTimes)
            {
                AnalyticsRepository.recordAnalyticsSourceTime(sourceTime);
            }          
        }

        private static void GetAdwordsCostData(DateTime fromDate, DateTime toDate, Site site)
        {
            System.Console.WriteLine("GetAdwordsCostData for site : " + site.siteId + ", GA account : " + site.account);
            AnalyticsRepository analyticsRepository = new AnalyticsRepositoryImpl();
            GAService gaService = new GAService_Impl();

            List<AdwordsCost> adwordsCosts = gaService.getAdwordsData(fromDate, toDate, site);
            analyticsRepository.deleteAdwordsCostData(site, fromDate, toDate);
            foreach (AdwordsCost adwordsCost in adwordsCosts)
            {
                analyticsRepository.recordAdwordsCostData(adwordsCost);
            }
        }

        private static Site[] getSites()
        {
            AnalyticsRepository AnalyticsRepository = new AnalyticsRepositoryImpl();
            return AnalyticsRepository.getTHGSites();            
        }
    }
}
