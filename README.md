# Qualified-OAUTH Challenge for CTFd
Used for the Illuminated Arcana project by Arcana Labs. Allows for the creation of periodically-rotated flags for long-running CTFs.

## Installation
Requires: 
- CTFd >= 3.4.1
- pyotp >= 2.6.0

1. Clone this repo to `CTFd/plugins`. The folder `must` be named "illuminarc" so that CTFd can serve the files in the assets dir.
2. Seed the appropriate values into your target images.
3. Create the necessary challenges within CTFd.

## Usage
Select "illuminarc" flag type from the necessary menus when setting up new flags in challenges and add just the content of a base32-encoded shared secret for the TOTP flag.

The resulting flag will validate if: the correct secret is used to generate a TOTP password for the current 24 hour period, and the flag is expressed in the format category_challenge_<FLAG_TOKEN>. The first two parts of the flag are actually outright ignored currently but are required for appropriate string parsing.
