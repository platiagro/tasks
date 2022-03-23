from insights.analysis.cluster_analysis_no_schema import cluster_pivot

def outlier_insights(outliers_df, df, categorical_columns):
    outliers_df['cluster_group'] = 0
    
    numerical_grouping, categorical_grouping = cluster_pivot(outliers_df, df, categorical_columns)
    
    return numerical_grouping, categorical_grouping
    
    
    