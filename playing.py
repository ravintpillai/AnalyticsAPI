import AnalyticsAuth
import collectArguments
import dimensions_and_metrics

dateList = collectArguments.getDates()
dimensionString = collectArguments.collectArguments(dimensions_and_metrics.dimensions)
metricString = collectArguments.collectArguments(dimensions_and_metrics.metrics)
dimensionList = collectArguments.collectLists(dimensionString)
metricList = collectArguments.collectLists(metricString)
segment_id = collectArguments.getSegments()
filters = collectArguments.getFilters()

arguments = AnalyticsAuth.Arguments(dateList,dimensionList,metricList,filters,segment_id)
results = AnalyticsAuth.Results(arguments)
