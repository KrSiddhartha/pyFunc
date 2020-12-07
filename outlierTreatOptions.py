def outlierTreatOptions(df, treatMethodPrint=""):
    df2 = df.copy()
    df2[colName] = np.where(df2[colName] <df2[colName].quantile(0.1), df2[colName].quantile(0.1),df2[colName])
    df2[colName] = np.where(df2[colName] >df2[colName].quantile(0.9), df2[colName].quantile(0.9),df2[colName])

    print(printFormat.BOLD + "If we treat outliers with " + treatMethodPrint + printFormat.END, end="\n\n")
    
    print(df2[colName].describe(), end="\n\n")

    fig = plt.figure(figsize= (20,15))
    fig.suptitle('Treated VS Original', fontsize=16)
    plt.subplot(3,2,1)
    plt.hist(df2[colName], color='lightblue', edgecolor = 'black', alpha = 0.7)
    plt.xlabel(colName)

    plt.subplot(3,2,2)
    plt.hist(df[colName], color='lightblue', edgecolor = 'black', alpha = 0.7)
    plt.xlabel(colName)

    plt.subplot(3,2,3)
    sns.kdeplot(df2[colName])
    plt.xlabel(colName)

    plt.subplot(3,2,4)
    sns.kdeplot(df[colName])
    plt.xlabel(colName)

    plt.subplot(3,2,5)
    sns.boxplot(x= df2[colName], color='lightblue')

    plt.subplot(3,2,6)
    sns.boxplot(x= df[colName], color='lightblue')

    print(colName + " Skewness = " + str(round(stats.skew(df2[colName][pd.notnull(df2[colName])]), 3)), end="\n\n\n\n")

    plt.show()