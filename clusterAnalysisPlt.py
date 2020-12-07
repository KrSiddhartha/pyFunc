def clusterAnalysisPlt(df, target):
    for var in df.drop([target,"GROUP"], axis=1).columns:
        plot = sns.lmplot(var,target,data=concat_data,hue='GROUP')
        plot.set(ylim = (-3,3))