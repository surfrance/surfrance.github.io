		function getSiteByCity(city) {
            const sitesDatabase = {
                "vannes": "meteohossegor.html",
                "la torche": "LaTorche.html",
                "crozon": "meteocrozon.html",
                "biarritz": "meteobiarritz.html",
                "lorient": "meteolorient.html",
				"guidel": "meteoguidel.html"
                // Ajoutez d'autres villes ici
            };
            return sitesDatabase[city.toLowerCase()] || null;
        }

        function searchCity() {
            const cityInput = document.getElementById("cityInput").value.trim().toLowerCase();
            const siteUrl = getSiteByCity(cityInput);

            const errorDiv = document.getElementById("error");
            errorDiv.textContent = ""; // Réinitialiser les messages d'erreur

            if (siteUrl) {
                // Redirige directement vers le site
                window.location.href = siteUrl;
            } else {
                // Affiche une erreur si la ville n'est pas trouvée
                errorDiv.textContent = "";
            }
        }