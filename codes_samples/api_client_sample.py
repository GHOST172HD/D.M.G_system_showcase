# ================= API CLIENT =================
class ApiClient:
    """Centralise toutes les requêtes HTTP avec le serveur."""

    def __init__(self, server_url):
        server_url = (server_url or "").strip()

        if server_url and not server_url.startswith(("http://", "https://")):
            server_url = f"http://{server_url}"

        self.server_url = server_url.rstrip("/")
        self.token = None
        self.user = None

    # ================= REQUEST CORE =================
    def request(self, method, endpoint, **kwargs):
        """
        Envoie une requête au serveur et retourne data.
        """
        url = f"{self.server_url}{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers(),
                timeout=12,
                **kwargs,
            )
        except requests.exceptions.ConnectionError as exc:
            raise RuntimeError(
                "Impossible de joindre le serveur. Vérifiez que le serveur est lancé, "
                "que l'IP est correcte et que le PC est sur le même réseau que le serveur."
            ) from exc
        except requests.exceptions.Timeout as exc:
            raise RuntimeError("Le serveur met trop de temps à répondre.") from exc

        try:
            payload = response.json()
        except ValueError as exc:

            raise RuntimeError(
                f"Réponse serveur invalide. Code HTTP : {response.status_code}. "
                "Regarde la console du serveur pour l'erreur exacte."
            ) from exc

        if not response.ok or not payload.get("success"):
            raise RuntimeError(payload.get("error", "Erreur, serveur inconnue."))

        return payload.get("data", {})