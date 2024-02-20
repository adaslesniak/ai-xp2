from Data import scaled_data
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA



data = scaled_data(1200)

# Apply PCA
pca = PCA(n_components=2)  # We use 2 principal components for visualization
pca_result = pca.fit_transform(data)

def display_original():
    # Plotting original data
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(data['Speed'], data['Mass'], c=data['Momentum'], cmap='viridis')
    plt.colorbar(label='Momentum')
    plt.xlabel('Speed')
    plt.ylabel('Mass')
    plt.title('Original Data (Speed vs. Mass)')

def display_pca():
    # PCA result plot
    plt.subplot(1, 2, 2)
    plt.scatter(pca_result[:, 0], pca_result[:, 1], c=data['Momentum'], cmap='viridis')
    plt.colorbar(label='Momentum')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA Result')

#display_original()
display_pca()
plt.tight_layout()
plt.show()
x = input()

