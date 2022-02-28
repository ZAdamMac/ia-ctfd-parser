# Qualified-OAUTH Challenge for CTFd
Used for the Illuminated Arcana project by Arcana Labs. Allows for the creation of periodically-rotated flags for long-running CTFs.

## Installation
Requires: 
- CTFd >= 3.4.1
- pyotp >= 2.6.0

1. Clone this repo to `CTFd/plugins`. The folder `must` be named "illuminarc" so that CTFd can serve the files in the assets dir.
2. Seed the appropriate values into your target images.
3. Create the necessary challenges within CTFd.