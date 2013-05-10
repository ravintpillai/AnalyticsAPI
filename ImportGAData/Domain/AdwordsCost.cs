using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class AdwordsCost
    {
        public string source { get; set; }
        public string medium { get; set; }
        public string adwordsCampaign { get; set; }
        public double adCost { get; set; }
        public int transactionCount { get; set; }
        public int clickCount { get; set; }
        public string keywords { get; set; }
        public double transactionRevenue { get; set; }
        public string gaAccount { get; set; }
        public DateTime gaDate { get; set; }
       
        public AdwordsCost(DataEntry gaDataEntry, Site site)
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
                    case "ga:keyword": keywords = dimension.Value;
                        break;
                    case "ga:adwordsCampaignID": adwordsCampaign = dimension.Value;
                        break;
                    case "ga:date": gaDate = DateTime.ParseExact(dimension.Value, "yyyyMMdd", null);
                        break;
                }
            }

            foreach (Metric metric in gaDataEntry.Metrics)
            {
                switch (metric.Name)
                {
                    case "ga:adClicks": clickCount = Convert.ToInt32(metric.Value);
                        break;
                    case "ga:transactions": transactionCount = Convert.ToInt32(metric.Value);
                        break;
                    case "ga:adCost": adCost = Convert.ToDouble(metric.Value);
                        break;
                    case "ga:transactionRevenue": transactionRevenue = Convert.ToDouble(metric.Value);
                        break;                   
                }
            }
        }
    }
}
