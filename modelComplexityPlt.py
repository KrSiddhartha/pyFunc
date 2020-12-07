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