from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from statsmodels.compat import lzip
from statsmodels.stats.api import het_breuschpagan
from statsmodels.api import qqplot
from seaborn import histplot
from matplotlib.pyplot import subplots, show
from numpy import array, zeros


class ModeleLineaire():

    def __init__(self, X, y,
                 num_imputer=SimpleImputer(strategy='median'),
                 num_transformer=MinMaxScaler(),
                 cat_transformer=OneHotEncoder(handle_unknown='ignore', drop='first'),
                 test_size=0.3):

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size)

        num_cols = X._get_numeric_data().columns.values.tolist()
        cat_cols = list(set(X.columns)-set(X._get_numeric_data().columns))

        num_pipeline = Pipeline([
            ('imputer', num_imputer),
            ('scaler', num_transformer)])

        self.preprocessor = ColumnTransformer([
            ('num_transformer', num_pipeline, num_cols),
            ('cat_transformer', cat_transformer, cat_cols)])

        pipeline = make_pipeline(self.preprocessor, LinearRegression())

        self.pipe = pipeline.fit(self.X_train, self.y_train)


    def show_scores(self, cv=5, scoring='r2'):
        for i, r2 in enumerate(cross_val_score(self.pipe, self.X_train, self.y_train, cv=cv, scoring=scoring)):
            print(f'{i+1}. r2 = {round(r2,2)}')
        print('Moyenne des r2 :', round(cross_val_score(self.pipe, self.X_train, self.y_train, cv=cv, scoring=scoring).mean(),2))
        print('Score du test :', round(self.pipe.score(self.X_test, self.y_test),2))

    def tts(self): return self.X_train, self.X_test, self.y_train, self.y_test

    def prediction(self, X=0):
        if type(X) == int: return self.pipe.predict(self.X_test)
        return self.pipe.predict(X)

    def residuals(self): return self.prediction() - self.y_test

    def het(self): return het_breuschpagan(self.residuals(), self.preprocessor.fit_transform(self.X_test))

    def plot(self):

        def test_homo():
            names = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
            test = self.het()
            p_value = lzip(names, test)[1][1]
            if p_value > 0.05: return f"p-value = {round(p_value,2)} > 0.05 :\nNous ne pouvons pas rejeter l'hypothèse nulle.\nC'est homoscédastique"
            return f"p-value = {round(p_value,2)} <= 0.05 :\nNous pouvons rejeter l'hyptohèse nulle.\nC'est hétéroscédastique"

        def remove_spine(axe):
            axe.spines.right.set_visible(False)
            axe.spines.top.set_visible(False)

        residus = self.residuals()

        fontdict = {'fontsize': '16',
                    'fontweight': 'bold',
                    'color': "black"}

        fig, ((ax1,ax2),
              (ax3,ax4)) = subplots(figsize=(15, 10),nrows=2, ncols=2)

        ax1.set_title('Condition de normalité des erreurs', fontdict)
        histplot(residus, ax = ax1, kde = True)
        ax1.set_xlabel('Résidus')
        remove_spine(ax1)

        ax2.set_title("Visualisation de l'homoscedasticité", fontdict)
        ax2.scatter(self.y_test, residus, c="red")
        ax2.plot(array(range(40,90)),zeros(50), c="black")
        ax2.set_xlabel('y observé')
        ax2.set_ylabel('Résidus')
        remove_spine(ax2)

        sentence = test_homo()
        ax2.annotate(sentence,ha='left',fontsize=10,fontstyle='italic', xy=(75, 4),
                     xytext=(65, 9),color='black',fontweight="extra bold", bbox=dict(color="white"),
                     arrowprops=dict(color="#1d2d35",linewidth="2",arrowstyle="->", connectionstyle="angle3"))

        ax3.set_title('QQ plot', fontdict)
        qqplot(residus, line='s', ax= ax3)
        remove_spine(ax3)

        ax4.set_visible(False)

        show()
