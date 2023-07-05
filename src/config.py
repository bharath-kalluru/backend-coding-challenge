from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


def get_secret(secret_name: str) -> str:
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url="<your-key-vault-url>", credential=credential)
    secret = secret_client.get_secret(secret_name)
    return secret.value


# Configuration settings for the application
ENVIRONMENT = "dev"  # Set the environment (dev, qa, prod) based on your deployment

if ENVIRONMENT == "dev":
    SECRET_KEY = get_secret("DEV_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = get_secret("DEV_SQLALCHEMY_DATABASE_URI")
elif ENVIRONMENT == "qa":
    SECRET_KEY = get_secret("QA_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = get_secret("QA_SQLALCHEMY_DATABASE_URI")
elif ENVIRONMENT == "prod":
    SECRET_KEY = get_secret("PROD_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = get_secret("PROD_SQLALCHEMY_DATABASE_URI")
else:
    raise ValueError(f"Invalid environment: {ENVIRONMENT}")
