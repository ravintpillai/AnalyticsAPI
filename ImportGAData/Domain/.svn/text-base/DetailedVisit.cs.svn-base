using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class DetailedVisit : Visit
    {
  
        public string medium { get; set; }
        public int transactions { get; set; }

        public DetailedVisit(DataEntry gaDataEntry, Site site)
        {        
            gaAccount = site.account;

            foreach (Dimension dimension in gaDataEntry.Dimensions)
            {
                switch (dimension.Name)
                {
                    case "ga:date": gaDate = DateTime.ParseExact(dimension.Value, "yyyyMMdd", null);
                        break;
                    case "ga:medium": medium = dimension.Value;
                        break;
                }
            }

            foreach (Metric metric in gaDataEntry.Metrics)
            {
                switch (metric.Name)
                {
                    case "ga:visitors": uniqueVisitors = Convert.ToInt32(metric.Value);
                        break;
                    case "ga:visits": visits = Convert.ToInt32(metric.Value);
                        break;
                    case "ga:transactions": transactions = Convert.ToInt32(metric.Value);
                        break;  
                }
            }
        }
    }
}
