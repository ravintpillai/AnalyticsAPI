##this is a module to provide the available dimensions and metrics. It can be updated to include new dimantions and metrics simply by including the name
##of the variable excluding the ga: bit, in the appropriate list, dimensionName for dimensions or metricName for metrics.
##I typed the lists by hand since I couldn't find a way to export the lists. Therefore, there may be some spelling errors.
##Dimensions and metrics included in the initialization of the variables are done with simple shortcuts because these dimensions are called frequently.
#There is a very small probability that this initialization of the variables could cause them to break, if and only if
#Google were to bring in a new dimension/metric with the same name as one of the keys used in the initialization,
#and a user tried to add the same key twice

dimensions = {'mob':'ga:isMobile','w':'ga:week', 'm':'ga:month','h':'ga:hour','d':'ga:day','c':'ga:country','s':'ga:source', 'med':'ga:medium'}
dimensionName = ["visitorType", "visitCount", "daysSinceLastVisit", "referralPath", "campaign", "source", "medium", "keyword", "adContent", "browser", "browserVersion", "operatingSystem", "operatingSystemVersion", "isMobile", "mobileDeviceBranding", "mobileDeviceModel", "mobileInputSelector", "mobileInputSelector", "mobileDeviceInfo","continent","subContinent","country","region","metro","city","latitude","longitude","networkDomain","networkLocation","flashVersion","javaEnabled","language","screenColors","screenResolution","hostname","pagePath","pagePathLevel1","pagePathLevel2","pagePathLevel3","pagePathLevel4","pageTitle","landingPagePath","secondPagePath","exitPagePath","previousPagePath","nextPagePath","pageDepth","searchUsed","searchKeyword","searchKeywordRefinement","searchCategory","searchStartPage","searchDestinationPage","eventCategory","eventAction","eventLabel","transactionId","affiliation","visitsToTransaction","daysToTransaction","productSku","productName","productCategory","date","year","month","week","day","hour","nthMonth","nthWeek","nthDay","dayOfWeek"]
for x in dimensionName:
    dimensions[x] = 'ga:'+x
metrics = {'r':'ga:transactionRevenue'}
metricName = ["visitors","newVisits","percentNewVisits","visits","bounces","entranceBounceRate","visitBounceRate","timeOnSite","avgTimeOnSite","organicSearches","impressions","adClicks","adCost","CPM","CPC","CTR","costPerTransaction","costPerGoalConversion","costPerConversion","RPC","ROI","margin","goal(0)Starts","goal(1)Starts","goal(2)Starts","goal(3)Starts","goal(4)Starts","goal(5)Starts","goal(0)Completions","goal(1)Completions","goal(2)Completions","goal(3)Completions","goal(4)Completions","goal(5)Completions","goal(0)Value","goal(1)Value","goal(2)Value","goal(3)Value","goal(4)Value","goal(5)Value","goal(0)ValueAll","goalValueAll","goalValuePerVisit","goalConversionRateAll","goal(0)Abandons","goal(1)Abandons","goal(2)Abandons","goal(3)Abandons","goal(4)Abandons","goal(5)Abandons","goalAbandonsAll","goalAbandonRateAll","socialActivities","entrances","entranceRate","pageviews","pageviewsPerVisit","uniquePageviews","timeOnPage","avgTimeOnPage","exits","exitRate","searchResultViews","searchUniques","avgSearchResultViews","searchVisits","percentVisitsWithSearch","searchDepth","avgSearchDepth","searchRefinements","searchDuration","avgSearchDuration","searchExits","searchExitRate","searchGoalConversionRateAll","goalValueAllPerSearch","pageLoadTime","pageLoadSample","avgPageLoadTime","domainLookupTime","pageDownloadTime","avgPageDownloadTime","redirectionTime","avgRedirectionTime","serverConnectionTime","avgServerConnectionTime","serverResponseTime","avgServerReponseTime","speedMetricsSample", "appviews","uniqueAppviews","appviewsPerVisit","totalEvents","uniqueEvents","eventValue","avgEventValue","visitsWithEvent","eventsPerVisitWithEvent","transactions","transactionsPerVisit","transactionRevenue","revenuePerTransaction","transactionRevenuePerVisit","transactionShipping","transactionTax","totalValue","itemQuantity","uniquePurchases","revenuePerItem","itemRevenue","itemsPerPurchase","socialInteractions","uniqueSocialInteractions","socialInteractionsPerVisit","userTimingValue","userTimingSample","avgUserTimingValue","exceptions","fatalExceptions"]
for y in metricName:
    metrics[y] = 'ga:'+y

dimensionLengths = {'ga:month':12,'ga:isMobile':2}
