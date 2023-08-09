import os
from google.cloud import secretmanager_v1
from dotenv import load_dotenv

load_dotenv()


class SecretManager:
    def __init__(self, project_id):
        self.client = secretmanager_v1.SecretManagerServiceClient()
        self.project_id = project_id
        self.enviroment = os.getenv("ENVIRONMENT", "dev")

    def get_secret(self, secret_name, secret_version=None):
        secret_version = secret_version or self.enviroment

        request = secretmanager_v1.AccessSecretVersionRequest(
            name="projects/{}/secrets/{}/versions/{}".format(
                self.project_id, secret_name, secret_version
            )
        )
        return self.client.access_secret_version(request).payload.data.decode("UTF-8")
