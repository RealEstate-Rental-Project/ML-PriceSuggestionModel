@Library('Jenkins-shared-library') _

mlModelPipeline(
    appName: 'ml-pricesuggestionmodel',
    hfRepo: 'saaymo/ml-pricesuggestionmodel',
    modelFiles: [
        // Modèles pour les prédictions quotidiennes (Daily)
        [name: 'daily/model_daily.joblib', targetDir: 'daily'],
        [name: 'daily/preprocessor_daily.joblib', targetDir: 'daily'],
        
        // Modèles pour les prédictions mensuelles (Monthly)
        [name: 'monthly/property_price_model.joblib', targetDir: '.'],
        [name: 'monthly/preprocessor.joblib', targetDir: '.']
    ]
)
