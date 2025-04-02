# DO NOT change anything except within the function
from approvedimports import *

def cluster_and_visualise(datafile_name:str, K:int, feature_names:list):
    """Function to get the data from a file, perform K-means clustering and produce a visualisation of results.

    Parameters
        ----------
        datafile_name: str
            path to data file

        K: int
            number of clusters to use
        
        feature_names: list
            list of feature names

        Returns
        ---------
        fig: matplotlib.figure.Figure
            the figure object for the plot
        
        axs: matplotlib.axes.Axes
            the axes object for the plot
    """
    # ====> insert your code below here
    # Read the data file
    data = np.genfromtxt(datafile_name, delimiter=',')
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=K, n_init=10)
    cluster_ids = kmeans.fit_predict(data)
    
    # Create visualization
    num_features = data.shape[1]
    fig, ax = plt.subplots(num_features, num_features, figsize=(12, 12))
    
    # Generate scatterplot matrix
    for i in range(num_features):
        for j in range(num_features):
            if i != j:
                # Scatter plot for different feature pairs
                ax[i,j].scatter(data[:,j], data[:,i], c=cluster_ids, s=30, cmap='viridis')
            else:
                # Histogram on diagonal
                ax[i,j].hist(data[:,i], bins=20, color='skyblue', edgecolor='black')
            
            # Set axis labels
            if i == num_features-1:
                ax[i,j].set_xlabel(feature_names[j], fontsize=8)
            if j == 0:
                ax[i,j].set_ylabel(feature_names[i], fontsize=8)
    
    # Add title with your UWE username (REPLACE 'abc123' with your actual username)
    fig.suptitle(f"Visualisation of {K} clusters by p28-gurung", y=1.02, fontsize=14)
    
    # Save visualization
    plt.tight_layout()
    plt.savefig('myVisualisation.jpg')
    
    return fig, ax
    # <==== insert your code above here
