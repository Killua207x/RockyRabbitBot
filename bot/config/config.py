from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: 26446336
    API_HASH: dd1477d16488c89ccf3d4c73b2c2d477

    REF_LINK: str = "https://t.me/rocky_rabbit_bot/play?startapp=frId6624523270" # NOT WORKING RIGHT NOW !

    AUTO_TAP: bool = True
    TAP_COUNT: list[int] = [50, 75]
    DELAY_BETWEEN_TAPS: list[int] = [15, 20]
    SLEEP_BY_MIN_ENERGY: int = 1000


    AUTO_BOOST: bool = True
    AUTO_UPGRADE_BOOST: bool = True
    MAX_ENERGY_LVL: int = 5
    MULTI_TAP_LVL: int = 5
    PASSIVE_INCOME_LVL: int = 3

    AUTO_TASK: bool = True
    AUTO_ENIGMA: bool = True
    AUTO_SUPERSET: bool = True
    AUTO_EASTER: bool = True

    AUTO_UPGRADE_CARDS: bool = True
    AUTO_CLAIM_UPGRADE_CARDS: bool = True

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


