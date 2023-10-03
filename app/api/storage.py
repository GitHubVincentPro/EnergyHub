@blueprint.route('/status')
def get_status():
# Récupérer l'état de la batterie depuis le modèle
# Serialiser et renvoyer
pass

@blueprint.route('/charge', methods=['POST'])
def post_charge():
# Récupérer les paramètres de charge depuis la requête
# Envoyer la commande de charge au modèle
# Renvoyer un message de confirmation
pass

@blueprint.route('/discharge')
def get_discharge():
# Simuler une décharge
# Revenir avec la quantité déchargée potentielle
pass