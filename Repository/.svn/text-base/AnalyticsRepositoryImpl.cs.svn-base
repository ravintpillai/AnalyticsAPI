using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Configuration;
using System.Data.SqlClient;
using System.Data;

namespace ImportGAData
{
    public class AnalyticsRepositoryImpl : AnalyticsRepository
    {
        private static readonly log4net.ILog log = log4net.LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);
        private static string connectionAnalytics = ConfigurationManager.ConnectionStrings["connectionAnalytics"].ConnectionString;

        public Site[] getTHGSites()
        {            
            List<Site> siteList = new List<Site>();
            SqlConnection conn = new SqlConnection();

            try
            {
                conn.ConnectionString = connectionAnalytics;
                conn.Open();

                SqlCommand sqlCommand = new SqlCommand();
                sqlCommand.Connection = conn;
                sqlCommand.CommandType = System.Data.CommandType.Text;
                sqlCommand.CommandText = "SELECT Site, Analytics_AccountID FROM [Analytics_Site_Account] a (NOLOCK) WHERE a.THG_Site = 1";

                SqlDataReader sqlDataReader = sqlCommand.ExecuteReader();

                while (sqlDataReader.Read())
                {
                    Site site = new Site();
                    site.account = sqlDataReader["Analytics_AccountID"].ToString();
                    site.siteId = Convert.ToInt32(sqlDataReader["Site"]);
                    siteList.Add(site);
                }

                sqlDataReader.Close();
                sqlCommand.Dispose();
            }
            catch (SqlException sqlex)
            {
                throw new Exception("Error in AnalyticsRepositoryImpl getting sites", sqlex);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }

            return siteList.ToArray();
        }

        public void recordPaidSearchVisitSummary(PaidSearchVisitSummary paidSearchVisitSummary)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"IF NOT EXISTS(SELECT (1) FROM Analytics_PaidSearch_Page (nolock) WHERE Analytics_Date = @Date AND Site = @Account AND Source = @Source AND Medium = @Medium AND PagePath = @PagePath)
	                                    INSERT INTO Analytics_PaidSearch_Page (Analytics_Date, Site, Source, Medium, PagePath, Visits)
		                                    VALUES (@Date, @Account, @Source, @Medium, @PagePath, @Visits)
                                    ELSE
	                                    UPDATE Analytics_PaidSearch_Page
	                                    SET Visits = @Visits
	                                    WHERE Analytics_Date = @Date AND Site = @Account AND Source = @Source AND Medium = @Medium AND PagePath = @PagePath";

                cmd.Parameters.Add("@Date", SqlDbType.DateTime);
                cmd.Parameters["@Date"].Value = paidSearchVisitSummary.gaDate;

                cmd.Parameters.Add("@Account", SqlDbType.NVarChar);
                cmd.Parameters["@Account"].Value = truncate(paidSearchVisitSummary.gaAccount, 15);

                cmd.Parameters.Add("@Source", SqlDbType.NVarChar);
                cmd.Parameters["@Source"].Value = truncate(paidSearchVisitSummary.source, 50);

                cmd.Parameters.Add("@Medium", SqlDbType.NVarChar);
                cmd.Parameters["@Medium"].Value = truncate(paidSearchVisitSummary.medium, 50);

                cmd.Parameters.Add("@PagePath", SqlDbType.NVarChar);
                cmd.Parameters["@PagePath"].Value = truncate(paidSearchVisitSummary.pagePath, 255);

                cmd.Parameters.Add("@Visits", SqlDbType.Int);
                cmd.Parameters["@Visits"].Value = paidSearchVisitSummary.visits;

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordPaidSearchVisitSummary", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void recordAnalyticsEvent(SiteEvent siteEvent)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"IF NOT EXISTS(SELECT (1) FROM Analytics_Event (nolock) WHERE Analytics_Date = @Date AND Site = @Account AND Category = @Category AND Action = @Action AND Label = @Label)
	                                    INSERT INTO Analytics_Event (Analytics_Date, Site, Category, Action, Label, TotalEvents, UniqueEvents)
		                                    VALUES (@Date, @Account, @Category, @Action, @Label, @TotalEvents, @UniqueEvents)
                                    ELSE
	                                    UPDATE Analytics_Event
	                                    SET TotalEvents = @TotalEvents,
		                                    UniqueEvents = @UniqueEvents
	                                    WHERE Analytics_Date = @Date AND Site = @Account AND Category = @Category AND Action = @Action AND Label = @Label";

                cmd.Parameters.Add("@Date", SqlDbType.DateTime);
                cmd.Parameters["@Date"].Value = siteEvent.gaDate;

                cmd.Parameters.Add("@Account", SqlDbType.NVarChar);
                cmd.Parameters["@Account"].Value = truncate(siteEvent.gaAccount, 15);

                cmd.Parameters.Add("@Category", SqlDbType.NVarChar);
                cmd.Parameters["@Category"].Value = truncate(siteEvent.category, 50);

                cmd.Parameters.Add("@Action", SqlDbType.NVarChar);
                cmd.Parameters["@Action"].Value = truncate(siteEvent.action, 50);

                cmd.Parameters.Add("@Label", SqlDbType.NVarChar);
                cmd.Parameters["@Label"].Value = truncate(siteEvent.label, 255);

                cmd.Parameters.Add("@TotalEvents", SqlDbType.Int);
                cmd.Parameters["@TotalEvents"].Value = siteEvent.totalEvents;

                cmd.Parameters.Add("@UniqueEvents", SqlDbType.Int);
                cmd.Parameters["@UniqueEvents"].Value = siteEvent.uniqueEvents;

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordAnalyticsEvent", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void recordAnalyticsVisitSource(DetailedVisit visit)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"IF NOT EXISTS(SELECT (1) FROM analytics_source_visits_site (nolock) WHERE Analytics_Date = @Date AND Site = @Account AND Medium = @Medium)
	                                    INSERT INTO analytics_source_visits_site (Analytics_Date, Site, Medium, UniqueVisitors, Visits, Transactions)
		                                    VALUES (@Date, @Account, @Medium, @UniqueVisitors, @Visits, @Transactions)
                                    ELSE
	                                    UPDATE analytics_source_visits_site
	                                    SET UniqueVisitors = @UniqueVisitors,
		                                    Visits = @Visits,
                                            Transactions = @Transactions
	                                    WHERE Analytics_Date = @Date AND Site = @Account AND Medium = @Medium";

                cmd.Parameters.Add("@Date", SqlDbType.DateTime);
                cmd.Parameters["@Date"].Value = visit.gaDate;

                cmd.Parameters.Add("@Account", SqlDbType.NVarChar);
                cmd.Parameters["@Account"].Value = truncate(visit.gaAccount, 15);

                cmd.Parameters.Add("@Medium", SqlDbType.NVarChar);
                cmd.Parameters["@Medium"].Value = truncate(visit.medium, 50);

                cmd.Parameters.Add("@UniqueVisitors", SqlDbType.Int);
                cmd.Parameters["@UniqueVisitors"].Value = visit.uniqueVisitors;

                cmd.Parameters.Add("@Visits", SqlDbType.Int);
                cmd.Parameters["@Visits"].Value = visit.visits;

                cmd.Parameters.Add("@Transactions", SqlDbType.Int);
                cmd.Parameters["@Transactions"].Value = visit.transactions;

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordAnalyticsVisitSource", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void recordAnalyticsVisit(Visit visit)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"IF NOT EXISTS(SELECT (1) FROM analytics_visits_site (nolock) WHERE Analytics_Date = @Date AND Site = @Account)
	                                    INSERT INTO analytics_visits_site (Analytics_Date, Site, UniqueVisitors, Visits)
		                                    VALUES (@Date, @Account, @UniqueVisitors, @Visits)
                                    ELSE
	                                    UPDATE analytics_visits_site
	                                    SET UniqueVisitors = @UniqueVisitors,
		                                    Visits = @Visits
	                                    WHERE Analytics_Date = @Date AND Site = @Account";

                cmd.Parameters.Add("@Date", SqlDbType.DateTime);
                cmd.Parameters["@Date"].Value = visit.gaDate;

                cmd.Parameters.Add("@Account", SqlDbType.NVarChar);
                cmd.Parameters["@Account"].Value = truncate(visit.gaAccount, 255);

                cmd.Parameters.Add("@UniqueVisitors", SqlDbType.Int);
                cmd.Parameters["@UniqueVisitors"].Value = visit.uniqueVisitors;

                cmd.Parameters.Add("@Visits", SqlDbType.Int);
                cmd.Parameters["@Visits"].Value = visit.visits;

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordAnalyticsVisitor", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void recordAnalyticsVisitor(Visitor visitor)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"IF NOT EXISTS(SELECT (1) FROM analytics_visitor (nolock) WHERE TransactionID = @TransactionID)
	                                    INSERT INTO analytics_visitor (LandingPagePath, TransactionID, DaysSinceLastVisit, PageDepth, VisitCount, IsNewVisitor)
		                                    VALUES (@LandingPagePath, @TransactionID, @DaysSinceLastVisit, @PageDepth, @VisitCount, @IsNewVisitor)
                                    ELSE
	                                    UPDATE analytics_visitor
	                                    SET LandingPagePath = @LandingPagePath,
		                                    DaysSinceLastVisit = @DaysSinceLastVisit,
                                            PageDepth = @PageDepth,
                                            VisitCount = @VisitCount,
                                            IsNewVisitor = @IsNewVisitor
	                                    WHERE TransactionID = @TransactionID";

                cmd.Parameters.Add("@LandingPagePath", SqlDbType.NVarChar);
                cmd.Parameters["@LandingPagePath"].Value = truncate(visitor.landingPagePath, 255) ;

                cmd.Parameters.Add("@DaysSinceLastVisit", SqlDbType.Int);
                cmd.Parameters["@DaysSinceLastVisit"].Value = visitor.daysSinceLastVisit;

                cmd.Parameters.Add("@PageDepth", SqlDbType.Int);
                cmd.Parameters["@PageDepth"].Value = visitor.pageDepth;

                cmd.Parameters.Add("@TransactionID", SqlDbType.NVarChar);
                cmd.Parameters["@TransactionID"].Value = truncate(visitor.orderNumber, 255);

                cmd.Parameters.Add("@VisitCount", SqlDbType.Int);
                cmd.Parameters["@VisitCount"].Value = visitor.visitCount;

                cmd.Parameters.Add("@IsNewVisitor", SqlDbType.Bit);
                cmd.Parameters["@IsNewVisitor"].Value = visitor.isNewVisitor;

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordAnalyticsVisitor", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void recordAnalyticsSiteSearch(Search siteSearch)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"IF NOT EXISTS(SELECT (1) FROM analytics_search (nolock) WHERE TransactionID = @TransactionID)
	                                    INSERT INTO analytics_search (TransactionID, SiteSearchUsed, VisitLength)
		                                    VALUES ( @TransactionID, @SiteSearchUsed, @VisitLength)
                                    ELSE
	                                    UPDATE analytics_search
	                                    SET SiteSearchUsed = @SiteSearchUsed,
		                                    VisitLength = @VisitLength
	                                    WHERE TransactionID = @TransactionID";

                cmd.Parameters.Add("@VisitLength", SqlDbType.Int);
                cmd.Parameters["@VisitLength"].Value = siteSearch.visitLength;

                cmd.Parameters.Add("@TransactionID", SqlDbType.NVarChar);
                cmd.Parameters["@TransactionID"].Value = truncate(siteSearch.orderNumber, 255);

                cmd.Parameters.Add("@SiteSearchUsed", SqlDbType.Bit);
                cmd.Parameters["@SiteSearchUsed"].Value = siteSearch.searchUsed;

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordAnalyticsSiteSearch", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void recordAnalyticsGeoSystem(GeoSystem geoSystem)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"IF NOT EXISTS(SELECT (1) FROM Analytics_Geo_System (nolock) WHERE TransactionID = @TransactionID)
	                                    INSERT INTO Analytics_Geo_System (City, Country, Language, TransactionID, isMobile)
		                                    VALUES (@City, @Country, @Language, @TransactionID, @IsMobile)
                                    ELSE
	                                    UPDATE Analytics_Geo_System
	                                    SET City = @City,
		                                    Country = @Country,
		                                    Language = @Language,
		                                    IsMobile = @IsMobile
	                                    WHERE TransactionID = @TransactionID";

                cmd.Parameters.Add("@City", SqlDbType.NVarChar);
                cmd.Parameters["@City"].Value = truncate(geoSystem.city, 255);

                cmd.Parameters.Add("@Country", SqlDbType.NVarChar);
                cmd.Parameters["@Country"].Value = truncate(geoSystem.country, 255);

                cmd.Parameters.Add("@Language", SqlDbType.NVarChar);
                cmd.Parameters["@Language"].Value = truncate(geoSystem.language, 255);

                cmd.Parameters.Add("@TransactionID", SqlDbType.NVarChar);
                cmd.Parameters["@TransactionID"].Value = truncate(geoSystem.orderNumber, 255);

                cmd.Parameters.Add("@IsMobile", SqlDbType.Bit);
                cmd.Parameters["@IsMobile"].Value = geoSystem.isMobile;

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordAnalyticsGeoSystem", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void recordAnalyticsSourceTime(SourceTime sourceTime)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"IF NOT EXISTS(SELECT (1) FROM analytics_source_time (nolock) WHERE TransactionID = @TransactionID)
	                                    INSERT INTO analytics_source_time (Campaign, Keyword, Medium, Source, TransactionID, DaysToTransaction, VisitsToTransaction, TrafficType, Analytics_AccountID)
		                                    VALUES (@Campaign, @Keyword, @Medium, @Source, @TransactionID, @DaysToTransaction, @VisitsToTransaction, null, @AccountID)
                                    ELSE
	                                    UPDATE analytics_source_time
	                                    SET Campaign = @Campaign,
		                                    Keyword = @Keyword,
		                                    Medium = @Medium,
		                                    Source = @Source,
		                                    DaysToTransaction = @DaysToTransaction,
		                                    VisitsToTransaction = @VisitsToTransaction,
		                                    TrafficType = null,
                                            Analytics_AccountID = @AccountID
	                                    WHERE TransactionID = @TransactionID";

                cmd.Parameters.Add("@Campaign", SqlDbType.NVarChar);
                cmd.Parameters["@Campaign"].Value = truncate(sourceTime.campaign, 255);

                cmd.Parameters.Add("@Keyword", SqlDbType.NVarChar);
                cmd.Parameters["@Keyword"].Value = truncate(sourceTime.keyword, 255);

                cmd.Parameters.Add("@Source", SqlDbType.NVarChar);
                cmd.Parameters["@Source"].Value = truncate(sourceTime.source, 255);

                cmd.Parameters.Add("@Medium", SqlDbType.NVarChar);
                cmd.Parameters["@Medium"].Value = truncate(sourceTime.medium, 255);

                cmd.Parameters.Add("@TransactionID", SqlDbType.NVarChar);
                cmd.Parameters["@TransactionID"].Value = truncate(sourceTime.orderNumber,255);

                cmd.Parameters.Add("@DaysToTransaction", SqlDbType.NVarChar);
                cmd.Parameters["@DaysToTransaction"].Value = Convert.ToInt32(sourceTime.daysToTransaction);

                cmd.Parameters.Add("@VisitsToTransaction", SqlDbType.NVarChar);
                cmd.Parameters["@VisitsToTransaction"].Value = Convert.ToInt32(sourceTime.daysToTransaction);

                cmd.Parameters.Add("@AccountID", SqlDbType.NVarChar);
                cmd.Parameters["@AccountID"].Value = truncate(sourceTime.gaAccount, 50);

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordAnalyticsSourceTime", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void deleteAdwordsCostData(Site site, DateTime fromDate, DateTime toDate) {

            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"DELETE FROM Analytics_Adwords_Cost
                    WHERE GA_Account = @account AND Date >= @fromDate AND Date <= @toDate";

                cmd.Parameters.Add("@account", SqlDbType.VarChar);
                cmd.Parameters["@account"].Value = site.account;

                cmd.Parameters.Add("@fromDate", SqlDbType.DateTime);
                cmd.Parameters["@fromDate"].Value = fromDate;

                cmd.Parameters.Add("@toDate", SqlDbType.DateTime);
                cmd.Parameters["@toDate"].Value = toDate;

                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in deleteAdwordsCostData", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        public void recordAdwordsCostData(AdwordsCost adwordsCost)
        {
            SqlConnection conn = new SqlConnection(connectionAnalytics);

            try
            {
                conn.Open();

                SqlCommand cmd = new SqlCommand();
                cmd.Connection = conn;

                cmd.CommandText = @"INSERT INTO Analytics_Adwords_Cost (GA_Account, Date, 
                    GA_Medium, GA_Source, GA_Adwords_Campaign, GA_Ad_Cost, GA_Transactions, 
                    GA_Revenue, GA_Keywords, GA_Clicks) 
                    VALUES (@accountId, @date, @gamedium, @gasource, @gaAdwordscampaign, @gacost, 
                    @gatransactions, @gatransactionrev, @gakeywords, @gaclicks)";


                cmd.Parameters.Add("@accountId", SqlDbType.NVarChar);
                cmd.Parameters["@accountId"].Value = truncate(adwordsCost.gaAccount,20);

                cmd.Parameters.Add("@date", SqlDbType.DateTime);
                cmd.Parameters["@date"].Value = adwordsCost.gaDate;

                cmd.Parameters.Add("@gasource", SqlDbType.NVarChar);
                cmd.Parameters["@gasource"].Value = truncate(adwordsCost.source, 50) ;

                cmd.Parameters.Add("@gamedium", SqlDbType.NVarChar);
                cmd.Parameters["@gamedium"].Value = truncate(adwordsCost.medium, 50);

                cmd.Parameters.Add("@gaAdwordscampaign", SqlDbType.NVarChar);
                cmd.Parameters["@gaAdwordscampaign"].Value = truncate(adwordsCost.adwordsCampaign, 50);

                cmd.Parameters.Add("@gacost", SqlDbType.Money);
                cmd.Parameters["@gacost"].Value = adwordsCost.adCost;

                cmd.Parameters.Add("@gatransactions", SqlDbType.Int);
                cmd.Parameters["@gatransactions"].Value = adwordsCost.transactionCount;

                cmd.Parameters.Add("@gatransactionrev", SqlDbType.Money);
                cmd.Parameters["@gatransactionrev"].Value = adwordsCost.transactionRevenue;

                cmd.Parameters.Add("@gakeywords", SqlDbType.NVarChar);
                cmd.Parameters["@gakeywords"].Value = truncate(adwordsCost.keywords, 255);

                cmd.Parameters.Add("@gaclicks", SqlDbType.Int);
                cmd.Parameters["@gaclicks"].Value = adwordsCost.clickCount;
                
                cmd.ExecuteNonQuery();
                cmd.Dispose();
            }
            catch (SqlException sqle)
            {
                log.Error("Error in recordAdwordsCostData", sqle);
            }
            finally
            {
                if (conn != null)
                {
                    if (conn.State == System.Data.ConnectionState.Open)
                    {
                        conn.Close();
                    }
                }
            }
        }

        private string truncate(string str, int maxLength)
        {
            if (str == null) return null;
            return str.Substring(0, Math.Min(maxLength, str.Length));
        }
    }
}
