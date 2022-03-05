"""OAUTH-Like Flag Handler for CTFd.

Expects a flag in the format machine_flagname_TOKEN, and parses it so that all is handled cleanly.

Produced by Arcana Labs
For full license information see LICENSE.txt
"""

__version__ = "1.0.0"
from CTFd.plugins.flags import BaseFlag, FLAG_CLASSES
from CTFd.plugins import register_plugin_assets_directory
import pyotp


class IlluminarcFlag(BaseFlag):
    name = "Illuminated Arcana-style"
    templates = {  # Nunjucks templates used for key editing & viewing
        "create": "/plugins/illuminarc/assets/static/create.html",
        "update": "/plugins/illuminarc/assets/static/edit.html",
    }

    @staticmethod
    def compare(chal_key_obj, provided):
        shared_secret = chal_key_obj.content
        try:
            provided_elements = provided.split("_")
            provided_token = provided_elements[2]
        except IndexError:
            return False ## This is not a valid glag.

        totp = pyotp.totp.TOTP(shared_secret, digits=16, interval=86400)
        valid = totp.verify(provided_token, valid_window=1)

        return valid


def load(app):
    app.db.create_all()
    FLAG_CLASSES['illuminarc'] = IlluminarcFlag
    register_plugin_assets_directory(app, base_path='/plugins/illuminarc/assets')


