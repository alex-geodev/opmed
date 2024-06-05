# Unzip vosk model
ZIP_FILE = backend/models/vosk-model-small-en-us-0.15.zip
OUTPUT_DIR = backend/models

all: unzip

unzip:
	unzip -o $(ZIP_FILE) -d $(OUTPUT_DIR)

clean:
	rm -rf $(OUTPUT_DIR)/vosk-model-small-en-us.0.15

.PHONY: all unzip clean
