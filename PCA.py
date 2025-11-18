# %%
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import pandas as pd
# %% 
X = [[2,3,3],[4,2,5], [6,4,7]]
# %%
class PCA():
    def fit(self, X):
        A = np.array(X)
        if A.shape[1] < 1:
            raise ValueError('a matriz precisa ter pelo menos 1 coluna')
        cov_matrix = np.cov(A.T)
        if cov_matrix.shape[0] != cov_matrix.shape[1]:
            raise ValueError('a matriz precisa ter as mesmas dimensoes')
        auto_values, autovector = np.linalg.eig(cov_matrix)
        auto_values_sum = np.sum(auto_values)
        self.auto_values_per_sum = auto_values/auto_values_sum
        
        self.out = {
                'componente':np.arange(len(self.auto_values_per_sum)),
                'variancia %':np.round(self.auto_values_per_sum*100,3)
            }
        print(self.out)
        return pd.DataFrame(self.out)
    def plot_pca(self):
        plt.figure(figsize=(10,8))
        plt.title('Variancia entre os componentes')
        sns.barplot(x=self.out['componente'], y=self.out['variancia %'])
        plt.xlabel('numero de componentes')
        plt.ylabel('variancia %')
        plt.tight_layout()
        plt.show()
# %%
obj = PCA()
obj.fit(X)
# %%
obj.plot_pca()
# %%
