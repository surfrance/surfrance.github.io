		function searchWebcams() {
            const city = document.getElementById('city-input').value.trim();
            const container = document.getElementById('webcam-container');
            
            // Effacer les webcams précédentes
            container.innerHTML = '';

            if (!city) {
                container.innerHTML = '<p>Veuillez entrer un nom de ville.</p>';
                return;
            }

            // Simuler les webcams (vous devrez connecter une API réelle ici)
            const webcams = getWebcamsByCity(city);

            if (webcams.length === 0) {
                container.innerHTML = `<p>Aucune webcam trouvée pour "${city}".`;
            } else {
                webcams.forEach(webcam => {
                    const webcamDiv = document.createElement('div');
                    webcamDiv.className = 'webcam';
                    webcamDiv.innerHTML = `
                        <iframe src="${webcam.url}" frameborder="0" allowfullscreen>
                        <p>${webcam.name}
                    `;
                    container.appendChild(webcamDiv);
                });
            }
        }


		function getWebcamsByCity(city) {
    const webcamsDatabase = {
        "biarritz": [
            { name: "Côte des Basques", url: "https://pv.viewsurf.com/1802/Biarritz-Grande-Plage?i=Njg2NDo" }
        ],
        "hossegor": [
            { name: "La Nord", url: "https://pv.viewsurf.com/2340/Hossegor?i=ODE4MDp1bmRlZmluZWQ" },
            { name: "La Gravière", url: "https://example.com/webcam4" }
        ],
		"capbreton": [
            { name: "Plage Centrale", url: "https://films.viewsurf.com/capbreton01_live/media.jpg" }
        ],
		"cap-breton": [
            { name: "Plage Centrale", url: "https://films.viewsurf.com/capbreton01_live/media.jpg" }
        ],
		"biscarrosse": [
            { name: "La Nord", url: "https://pv.viewsurf.com/2364/Biscarrosse-Plage-Sud?i=ODI4NDp1bmRlZmluZWQ" }
		],
        "lacanau": [
            { name: "Plage Centrale", url: "https://pv.viewsurf.com/410/Lacanau-Plage-Nord-Surf-club?i=MjY5Mjo" }
        ],
        "lorient": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/lorient/guidel-fort-du-loch" }
        ],
		"guidel": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/lorient/guidel-fort-du-loch" }
        ],
		"ondre": [
            { name: "Plage des Minimes", url: "https://pv.viewsurf.com/722/Ondres?i=Mzk5Mjp1bmRlZmluZWQ" }
        ],
		"arradon": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/port-arradon/panoramique" }
        ],
		"arzon": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/arzon/port-du-crouesty/video" }
        ],
		"ileaumoines": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/port-blanc/ile-aux-moines/video" }
        ],
		"ile-au-moines": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/port-blanc/ile-aux-moines/video" }
        ],
		"ile au moines": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/port-blanc/ile-aux-moines/video" }
        ],
		"sarzeau": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/sarzeau/port-saint-jacques" }
        ],
		"vannes": [
            { name: "Plage des Minimes", url: "https://www.skaping.com/port-arradon/panoramique" }
        ],
        "seignosse": [
            { name: "Les Bourdaines", url: "https://pv.viewsurf.com/1244/Seignosse-Les-Bourdaines?i=NTMwNjo" }
        ],
		"paris": [
            { name: "Plage des Minimes", url: "https://www.skylinewebcams.com/fr/webcam/france/ile-de-france/paris/tour-eiffel.html" }
        ],
		"marseille": [
            { name: "Plage des Minimes", url: "https://www.hotel-carre-vieux-port.com/5b163d66-6e9f-4d1d-8c88-4086f7d1c9f1" }
        ],
		"nice": [
            { name: "Plage des Minimes", url: "https://pv.viewsurf.com/2274/Nice-promenade-des-anglais?i=Nzk5Mjo" }
        ],
    };
    return webcamsDatabase[city.toLowerCase()] || [];
}