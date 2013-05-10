using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class GeoSystem
    {
        public string city { get; set; }
        public string country { get; set; }
        public string language { get; set; }            
        public string orderNumber { get; set; }
        public Boolean isMobile { get; set; }

        public GeoSystem(DataEntry gaDataEntry)
        {
            foreach (Dimension dimension in gaDataEntry.Dimensions)
            {
                switch (dimension.Name)
                {
                    case "ga:city": city = dimension.Value;
                        break;
                    case "ga:country": country = dimension.Value;
                        break;
                    case "ga:language": language = dimension.Value;
                        break;
                    case "ga:isMobile": isMobile = (dimension.Value == "Yes");
                        break;
                    case "ga:transactionId": orderNumber = dimension.Value;
                        break;
                }
            }
        }
    }
}
