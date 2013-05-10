using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Google.GData.Analytics;

namespace ImportGAData
{
    public class Search
    {
        public int visitLength { get; set; }        
        public string orderNumber { get; set; }
        public Boolean searchUsed { get; set; }

        public Search(DataEntry gaDataEntry)
        {
            foreach (Dimension dimension in gaDataEntry.Dimensions)
            {
                switch (dimension.Name)
                {
                    case "ga:visitLength": visitLength = Convert.ToInt32(dimension.Value);
                        break;
                    case "ga:searchUsed": searchUsed = (dimension.Value == "Visits With Site Search");
                        break;
                    case "ga:transactionId": orderNumber = dimension.Value;
                        break;
                }
            }
        }
    }
}
