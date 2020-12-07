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
