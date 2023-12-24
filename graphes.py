import matplotlib.pyplot as plt
import numpy as np

# Exemple de données (remplacez cela par vos propres données en bytes par seconde)


file_sizes_bytes = [13, 352613, 2270561, 5182801, 10879783, 29460736, 119425820, 285659587, 892347730, 1962803200]  # Taille des fichiers en bytes
upload_speed_s3 = [81.35057045112411, 2584565.850011359, 3709542.4780980004, 3825446.1238101707, 3798804.5909560495, 3913371.338801596, 4015344.8476636033, 4031805.8295990517, 4031666.09903287, 4013804.3745147963]  # Vitesse d'upload pour AWS S3 en bytes/s
download_speed_s3 = [65.49774050254298, 2273415.822279063, 3087734.7462674375, 3721960.2730817855, 3698685.2494490244, 3975833.8775890507, 3994842.204195208, 4040230.0579885095, 4046285.096024536, 4039437.2914599366]  # Vitesse de téléchargement pour AWS S3 en bytes/s
upload_speed_azure = [6.818980458600163,795715.0469730123,3033059.962789578,3004032.9659849373,2825457.7313360865,2099246.2058606492,2286186.5207464863,2301596.070467827,2776813.1725297645,2708436.3653774713]  # Vitesse d'upload pour Azure Blob Storage en bytes/s
download_speed_azure = [4.556617099505003, 655035.5478317561, 2656379.4302061247, 2974175.93214281, 3353402.946489062, 3234704.132008359, 3211866.891162038, 3240809.5074586975, 3159842.7179908897, 3091366.784859316]  # Vitesse de téléchargement pour Azure Blob Storage en bytes/s




# Convertir les tailles de fichiers en Mo pour l'échelle des y
file_sizes_MB = np.array(file_sizes_bytes) / (2**20)

# Créer une figure avec deux sous-graphiques (une colonne, deux lignes)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 10))

# Graphique d'upload
ax1.plot(file_sizes_MB, upload_speed_s3, marker='o', color='r', label='AWS S3 (Upload)')
ax1.plot(file_sizes_MB, upload_speed_azure, marker='o', color='b', label='Azure Blob (Upload)')
ax1.set_ylabel('Vitesse (bytes/s)')
ax1.legend()

# Graphique de download
ax2.plot(file_sizes_MB, download_speed_s3, marker='o', linestyle='--', color='r', label='AWS S3 (Download)')
ax2.plot(file_sizes_MB, download_speed_azure, marker='o', linestyle='--', color='b', label='Azure Blob (Download)')
ax2.set_xlabel('Taille des fichiers (Mo)')
ax2.set_ylabel('Vitesse (bytes/s)')
ax2.legend()

# Ajouter une deuxième échelle des y pour afficher la taille des fichiers
ax2_secondary = ax2.twinx()
ax2_secondary.set_ylabel('Taille des fichiers (Mo)', color='g')
ax2_secondary.plot(file_sizes_MB, file_sizes_MB, color='g', linestyle='--', linewidth=2)
ax2_secondary.tick_params(axis='y', labelcolor='g')

# Ajuster l'espacement entre les graphiques
plt.subplots_adjust(hspace=0.3)

# Afficher le graphique
plt.suptitle('Comparaison des performances entre AWS S3 et Azure Blob Storage')
plt.show()
