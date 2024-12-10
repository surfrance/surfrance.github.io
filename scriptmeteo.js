function goBack() {
	if (window.history.length > 1) {
		history.back();
	} else {
		window.location.href = "Fiche-M�t�o.html"; // Remplacez par votre URL par d�faut
	}
}
function afficherHeure() {
    const maintenant = new Date();
    const heures = String(maintenant.getHours()).padStart(2, '0');
    const minutes = String(maintenant.getMinutes()).padStart(2, '0');
    const secondes = String(maintenant.getSeconds()).padStart(2, '0');
    document.getElementById('horloge').textContent = `${heures}:${minutes}:${secondes}`;
}
// Mettre � jour l'heure toutes les secondes
setInterval(afficherHeure, 1000);

// Afficher l'heure imm�diatement au chargement
afficherHeure();
// Fonction pour partager la page
function sharePage() {
    if (navigator.share) {
        navigator.share({
            title: 'M�t�o � Crozon',
            text: 'D�couvrez les pr�visions m�t�orologiques � Crozon !',
            url: window.location.href,
        }).catch((error) => console.error('Erreur de partage', error));
    } else {
        alert("L'API de partage n'est pas disponible. Copiez ce lien pour partager : " + window.location.href);
    }
}