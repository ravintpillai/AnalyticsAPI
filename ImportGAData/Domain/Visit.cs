using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class Visit
    {

        public int uniqueVisitors { get; set; }
        public int visits { get; set; }
        public string gaAccount { get; set; }
        public DateTime gaDate { get; set; }

        public Visit()
        {
        }

        public Visit(DataEntry gaDataEntry, Site site) {
        
            gaAccount = site.account;

            foreach (Dimension dimension in gaDataEntry.Dimensions)
            {
                switch (dimension.Name)
                {
                    case "ga:date": gaDate = DateTime.ParseExact(dimension.Value, "yyyyMMdd", null);
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
                }
            }
        }
    }
}
