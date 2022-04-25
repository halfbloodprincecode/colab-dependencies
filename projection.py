from sklearn.manifold import TSNE

def tsne(X, n_components=2):
  return TSNE(n_components=n_components, verbose=0, random_state=123).fit_transform(X);
