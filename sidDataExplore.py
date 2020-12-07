class printFormat:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def freqTab(df, colName):
    freqC = pd.DataFrame(dat.cement.value_counts())
    freqC.columns = ['Freq']
    freqP = pd.DataFrame(dat.cement.value_counts('normalise')*100)
    freqP.columns = ['Perc']
    freqP.Perc = round(freqP.Perc,2)
    freqT = pd.merge(freqC, freqP, left_index=True, right_index=True)
    freqT[colName] = freqC.index
    freqT = freqT[[colName,'Freq','Perc']]
    freqT.reset_index(inplace=True, drop=True)
    
    return freqT


def calc_vif(X):
    vif = pd.DataFrame()
    vif["variables"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    return(vif)


def clusterAnalysisPlt(df, target):
    for var in df.drop([target,"GROUP"], axis=1).columns:
        plot = sns.lmplot(var,target,data=concat_data,hue='GROUP')
        plot.set(ylim = (-3,3))


def corrPlot(df):
    correlation = df.corr()
    mask = np.zeros_like(correlation, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    f, ax = plt.subplots(figsize=(20, 20))

    cmap = sns.diverging_palette(180, 20, as_cmap=True)
    sns.heatmap(correlation, mask=mask, cmap=cmap, vmax=1, vmin =-1, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

    plt.show()


def modelComplexityPlt(degree_Min,degree_Max,rmse_test,rmse_train,test_Score,train_Score):
    dfRMSE=pd.DataFrame({'Degree': range(degree_Min,degree_Max+1),
                         'RMSE_test': rmse_test,
                         'RMSE_train': rmse_train})
    dfRsq=pd.DataFrame({'Degree': range(degree_Min,degree_Max+1),
                        'test_R^2': test_Score,
                        'train_R^2': train_Score})
    
    figure(num=None, figsize=(20, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.subplot(1,2,1)
    plt.style.use('seaborn-darkgrid') # style
    palette = plt.get_cmap('Set1') # create a color palette
    num=0 # multiple line plot
    for column in dfRMSE.drop('Degree', axis=1):
        num+=1
        plt.plot(dfRMSE['Degree'], dfRMSE[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)
        plt.legend(loc=2, ncol=2)

        # Add titles
        plt.xlabel("Degree Polynomial")
        plt.ylabel("RMSE")

    plt.subplot(1,2,2)
    plt.style.use('seaborn-darkgrid') # style
    palette = plt.get_cmap('Set1') # create a color palette
    num=0 # multiple line plot
    for column in dfRsq.drop('Degree', axis=1):
        num+=1
        plt.plot(dfRsq['Degree'], dfRsq[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)
        plt.legend(loc=2, ncol=2)

        # Add titles
        plt.xlabel("Degree Polynomial")
        plt.ylabel("R^2 for Model")


def outlierIdenti(var_):
    q1=var_.quantile(0.25)
    q3=var_.quantile(0.75)
    iqr=q3-q1
    lower_whisker = q1-1.5*iqr
    upper_whisker = q3+1.5*iqr
    
    return [q1,q3,iqr,lower_whisker,upper_whisker]


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


def variableProfile(df, colName, varType="cat", outlierChk=True):
    df = df.copy()
    if(varType=="num"):
        print(df[colName].describe(), end="\n\n")
        
        plt.figure(figsize= (20,15))
        plt.subplot(3,1,1)
        plt.hist(df[colName], color='lightblue', edgecolor = 'black', alpha = 0.7)
        plt.xlabel(colName)
        
        plt.figure(figsize= (20,15))
        plt.subplot(3,1,2)
        sns.kdeplot(df[colName])
        plt.xlabel(colName)
        
        plt.figure(figsize= (20,15))
        plt.subplot(3,1,3)
        sns.boxplot(x= df[colName], color='lightblue')

        print(colName + " Skewness = " + str(round(stats.skew(df[colName][pd.notnull(df[colName])]), 3)), end="\n\n")

        plt.show()
        
        Q1,Q2,IQR,Lower_Whisker,Upper_Whisker = outlierIdenti(df[colName])
        upperOutCnt = sum(df[colName]>Upper_Whisker)
        lowerOutCnt = sum(df[colName]<Lower_Whisker)
        
        if(outlierChk==True):
            if((upperOutCnt>0) | (lowerOutCnt>0)):

                print(printFormat.RED +"Outliers present in " + colName + printFormat.END, end="\n\n")

                print(colName + " IQR = " + str(round(IQR,3)), end="\n\n")
                print(colName + " Lower outlier threshold = " + str(round(Lower_Whisker,3)), end="\n\n")
                print(colName + " Count of observations below lower outlier threshold = " + str(round(lowerOutCnt,3)), end="\n\n")
                print(colName + " Lower of observations below lower outlier threshold = " + str(round((lowerOutCnt/df.shape[0])*100, 2)), end="\n\n")
                print(colName + " Upper outlier threshold = " + str(round(Upper_Whisker,3)), end="\n\n")
                print(colName + " Count of observations over upper outlier threshold = " + str(round(upperOutCnt,3)), end="\n\n")
                print(colName + " Upper of observations over upper outlier threshold = " + str(round((upperOutCnt/df.shape[0])*100, 2)), end="\n\n\n\n")
                
                outlierTreatOptions(df, "Quantile-based Flooring and Capping")
                outlierTreatOptions(df, "median")
                outlierTreatOptions(df, "mean")
            else:
                print(printFormat.GREEN + "No outliers present in " + colName + printFormat.END, end="\n\n")

        
    if(varType=="cat"):
        distTab = pd.merge(pd.dfaFrame(df[colName].value_counts()).reset_index(),
         pd.dfaFrame(df[colName].value_counts("normalise")*100).reset_index(),
         on="index")
        distTab.columns = [colName, "Frequency", "Percentage"]
        print(distTab, end="\n\n")
        
        plt.figure(figsize= (15,7))
        plt.subplot(1,1,1)
        plt.hist(df[colName], color='lightblue', edgecolor = 'black', alpha = 0.7)
        plt.xlabel(colName)

        plt.show()

