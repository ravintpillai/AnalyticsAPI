using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class PaidSearchVisitSummary
    {

        public int visits { get; set; }
        public string gaAccount { get; set; }
        public DateTime gaDate { get; set; }
        public string medium { get; set; }
        public string source { get; set; }
        public string pagePath { get; set; }

        public PaidSearchVisitSummary(DataEntry gaDataEntry, Site site)
        {
        
            gaAccount = site.account;

            foreach (Dimension dimension in gaDataEntry.Dimensions)
            {
                switch (dimension.Name)
                {
                    case "ga:date": gaDate = DateTime.ParseExact(dimension.Value, "yyyyMMdd", null);
                        break;
                    case "ga:source": source = dimension.Value;
                        break;
                    case "ga:medium": medium = dimension.Value;
                        break;
                    case "ga:pagePath": pagePath = dimension.Value;
                        break;
                }
            }

            foreach (Metric metric in gaDataEntry.Metrics)
            {
                switch (metric.Name)
                {
  
                    case "ga:visits": visits = Convert.ToInt32(metric.Value);
                        break;                 
                }
            }
        }
    }
}
