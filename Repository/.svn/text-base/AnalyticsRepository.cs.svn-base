using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ImportGAData
{
    interface AnalyticsRepository
    {
        Site[] getTHGSites();
        void recordPaidSearchVisitSummary(PaidSearchVisitSummary paidSearchVisitSummary);
        void recordAnalyticsEvent(SiteEvent siteEvent);
        void recordAnalyticsVisitSource(DetailedVisit visit);
        void recordAnalyticsVisit(Visit visit);
        void recordAnalyticsVisitor(Visitor visitor);
        void recordAnalyticsSiteSearch(Search siteSearch);
        void recordAnalyticsGeoSystem(GeoSystem geoSystem);
        void recordAnalyticsSourceTime(SourceTime sourceTime);
        void recordAdwordsCostData(AdwordsCost adwordsCost);
        void deleteAdwordsCostData(Site site, DateTime fromDate, DateTime toDate);
    }
}
