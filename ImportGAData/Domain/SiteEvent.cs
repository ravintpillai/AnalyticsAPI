using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class SiteEvent
    {
        public string category { get; set; }
        public string action { get; set; }
        public string label { get; set; }
        public int totalEvents { get; set; }
        public int uniqueEvents { get; set; }

        public string gaAccount { get; set; }
        public DateTime gaDate { get; set; }

        public SiteEvent(DataEntry gaDataEntry, Site site)
        {        
            gaAccount = site.account;

            foreach (Dimension dimension in gaDataEntry.Dimensions)
            {
                switch (dimension.Name)
                {
                    case "ga:date": gaDate = DateTime.ParseExact(dimension.Value, "yyyyMMdd", null);
                        break;
                    case "ga:eventCategory": category = dimension.Value;
                        break;
                    case "ga:eventAction": action = dimension.Value;
                        break;
                    case "ga:eventLabel": label = dimension.Value;
                        break;
                }
            }

            foreach (Metric metric in gaDataEntry.Metrics)
            {
                switch (metric.Name)
                {
                    case "ga:totalEvents": totalEvents = Convert.ToInt32(metric.Value);
                        break;
                    case "ga:uniqueEvents": uniqueEvents = Convert.ToInt32(metric.Value);
                        break;
                }
            }
        }
    }
}
