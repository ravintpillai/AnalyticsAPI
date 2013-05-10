using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class Visitor
    {
        public string landingPagePath { get; set; }
        public int daysSinceLastVisit { get; set; }
        public int pageDepth { get; set; }
        public int visitCount { get; set; }
        public string orderNumber { get; set; }
        public Boolean isNewVisitor { get; set; }

        public Visitor(DataEntry gaDataEntry) {
            foreach (Dimension dimension in gaDataEntry.Dimensions)
            {
                switch (dimension.Name)
                {
                    case "ga:daysSinceLastVisit": daysSinceLastVisit = Convert.ToInt32(dimension.Value);
                        break;
                    case "ga:pageDepth": pageDepth = Convert.ToInt32(dimension.Value);
                        break;
                    case "ga:visitCount": visitCount = Convert.ToInt32(dimension.Value);
                        break;
                    case "ga:visitorType": isNewVisitor = (dimension.Value == "New Visitor");
                        break;
                    case "ga:landingPagePath": landingPagePath = dimension.Value;
                        break;
                    case "ga:transactionId": orderNumber = dimension.Value;
                        break;
                }
            }
        }
    }
}
