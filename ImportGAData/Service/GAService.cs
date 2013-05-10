using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ImportGAData
{
    interface GAService
    {
        List<SourceTime> getSourceTimeData(DateTime fromDate, DateTime toDate, Site site);
        List<AdwordsCost> getAdwordsData(DateTime fromDate, DateTime toDate, Site site);
        List<GeoSystem> getGeoSystemData(DateTime fromDate, DateTime toDate, Site site);
        List<Search> getSiteSearchData(DateTime fromDate, DateTime toDate, Site site);
        List<Visitor> getVisitorData(DateTime fromDate, DateTime toDate, Site site);
        List<Visit> getVisitData(DateTime fromDate, DateTime toDate, Site site);
        List<DetailedVisit> getVisitSourceData(DateTime fromDate, DateTime toDate, Site site);
        List<SiteEvent> getEventData(DateTime fromDate, DateTime toDate, Site site);
        List<PaidSearchVisitSummary> getPaidSearchVisits(DateTime fromDate, DateTime toDate, Site site);
    }
}
