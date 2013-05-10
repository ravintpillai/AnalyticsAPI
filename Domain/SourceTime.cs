using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class SourceTime
    {
        public string campaign { get; set; }
        public string keyword { get; set; }
        public string medium { get; set; }
        public string source {get; set;}                 
        public string orderNumber { get; set; }
        public int daysToTransaction { get; set; }
        public int visitsToTransaction { get; set; }
        public DateTime analyticsDate { get; set; }
        public string gaAccount { get; set; }

        public SourceTime(DataEntry gaDataEntry, Site site)
        {
            gaAccount = site.account;

            foreach (Dimension dimension in gaDataEntry.Dimensions)
            {
                switch (dimension.Name)
                {
                    case "ga:source": source = dimension.Value;
                        break;
                    case "ga:medium": medium = dimension.Value;
                        break;
                    case "ga:keyword": keyword = dimension.Value;
                        break;
                    case "ga:campaign": campaign = dimension.Value;
                        break;
                    case "ga:daysToTransaction": daysToTransaction = Convert.ToInt32(dimension.Value);
                        break;
                    case "ga:visitsToTransaction": visitsToTransaction = Convert.ToInt32(dimension.Value);
                        break;
                    case "ga:transactionId": orderNumber = dimension.Value;
                        break;
                }
            }
        }
    }
}
