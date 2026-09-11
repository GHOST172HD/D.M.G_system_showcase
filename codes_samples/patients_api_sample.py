# ================= PATIENTS =================
def list_patients(self, search=""):
    """Récupère la liste des patients."""
    data = self.request("GET", "/api/patients", params={"search": search})
    return data.get("patients", [])

def create_patient(self, patient_data):
    """Envoie le formulaire complet d'un patient au serveur."""
    return self.request("POST", "/api/patients", json=patient_data)

def get_patient(self, patient_id):
    """Récupère le dossier complet d'un patient."""
    return self.request("GET", f"/api/patients/{patient_id}")

def update_patient(self, patient_id, data):
    """Modifie les informations d'un patient."""
    return self.request("PUT", f"/api/patients/{patient_id}", json=data)

def delete_patient(self, patient_id):
    """Supprime un patient."""
    return self.request("DELETE", f"/api/patients/{patient_id}")

def get_patient_photo(self, patient_id):
    """Télécharge la photo du patient. Retourne None si aucune photo."""
    url = f"{self.server_url}/api/patients/{patient_id}/photo"

    try:
        response = requests.get(url, headers=self.headers(), timeout=12)
    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError("Impossible de charger la photo du patient.") from exc
    except requests.exceptions.Timeout as exc:
        raise RuntimeError("Le serveur met trop de temps à envoyer la photo.") from exc

    if response.status_code == 404:
        return None

    if not response.ok:
        raise RuntimeError("Erreur lors du chargement de la photo.")

    return response.content