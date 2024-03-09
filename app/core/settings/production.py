from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):

    title: str = "Prod event service"

    class Config(AppSettings.Config):
        env_file = ".env.prod"
